#!/usr/bin/env python3
"""HTTP audit of all sitemap pages on local preview server."""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8080"
ROOT = Path(__file__).resolve().parent.parent
issues = []

tree = ET.parse(ROOT / "sitemap.xml")
ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
paths = []
for loc in tree.findall(".//sm:loc", ns):
    path = loc.text.replace("https://tsbrenterprises.com", "").lstrip("/")
    paths.append(path or "/")

href_re = re.compile(r'(?:href|src)=["\']([^"\'#?]+)["\']', re.I)
img_re = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.I)

for path in paths:
    url = urljoin(BASE + "/", path)
    try:
        with urlopen(Request(url, headers={"User-Agent": "TSBR-Audit/1.0"}), timeout=20) as resp:
            status = resp.status
            html = resp.read().decode("utf-8", errors="replace")
    except Exception as exc:
        issues.append(f"FETCH FAIL {path}: {exc}")
        continue
    if status != 200:
        issues.append(f"HTTP {status}: {path}")
        continue
    if 'id="main"' not in html:
        issues.append(f"MISSING #main: {path}")
    for m in img_re.finditer(html):
        src = m.group(1).strip()
        if src.startswith(("http://", "https://", "data:")):
            continue
        img_url = urljoin(url, src)
        try:
            with urlopen(Request(img_url, headers={"User-Agent": "TSBR-Audit/1.0"}), timeout=15) as ir:
                if ir.status >= 400:
                    issues.append(f"BROKEN IMG [{path}]: {src} -> {ir.status}")
        except Exception as exc:
            issues.append(f"BROKEN IMG [{path}]: {src} ({exc})")
    for m in href_re.finditer(html):
        ref = m.group(1).strip()
        if ref.startswith(("mailto:", "tel:", "javascript:", "#")):
            continue
        if ref.startswith(("http://", "https://", "//")):
            parsed = urlparse(ref)
            if parsed.netloc and "tsbrenterprises.com" not in parsed.netloc and "localhost" not in parsed.netloc:
                continue
        link_url = urljoin(url, ref)
        if "localhost" not in link_url and "127.0.0.1" not in link_url:
            continue
        try:
            with urlopen(Request(link_url, headers={"User-Agent": "TSBR-Audit/1.0"}), timeout=15) as lr:
                if lr.status >= 400:
                    issues.append(f"BROKEN LINK [{path}]: {ref} -> {lr.status}")
        except Exception as exc:
            issues.append(f"BROKEN LINK [{path}]: {ref} ({exc})")

print(f"Checked {len(paths)} sitemap URLs at {BASE}")
print(f"ISSUES: {len(issues)}")
for i in issues:
    print(i)
sys.exit(1 if issues else 0)