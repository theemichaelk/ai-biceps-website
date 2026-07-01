# The Stone Builders Rejected (TSBR Enterprises)

Texas B2B local SEO & Google Business Profile agency website.

### Build
```bash
python _build.py
```
Regenerates all HTML from `_content.py` (rich content), `_content_extra.py` (supplementary blocks), and `_build.py` (templates).

### Preview
```bash
python -m http.server 8080
```
Open http://localhost:8080

### Configuration
Copy `.env.example` to `.env` and fill in values. `_config.py` loads `.env` automatically.

| Variable | Purpose |
|----------|---------|
| `TSBR_FORMSPREE_ENDPOINT` | Formspree form URL (e.g. `https://formspree.io/f/xxxxx`) |
| `FORMSPREE_DEPLOY_KEY` | Formspree CLI deploy key (alternative to pasting endpoint) |
| `TSBR_GA_MEASUREMENT_ID` | Google Analytics 4 ID (e.g. `G-XXXXXXXXXX`) |

### Formspree setup
```powershell
.\scripts\setup-formspree.ps1 -Endpoint "https://formspree.io/f/YOUR_ID"
# OR with CLI deploy key in .env:
.\scripts\setup-formspree.ps1 -Deploy
```

### Deploy
```powershell
.\scripts\deploy.ps1 -Method preview   # local preview
.\scripts\deploy.ps1 -Method copy       # copy to deploy.config.json path
.\scripts\deploy.ps1 -Method ftp        # FTP upload
```

### Visual audit
```powershell
.\scripts\deploy.ps1 -Method preview    # in one terminal
cd scripts && npm install && npm run visual-audit
```

### Business Info
- **Founder:** Mike Kaswatuka
- **Address:** 518 Brynmawr Ct, Arlington, TX 76014
- **Phone:** (682) 206-4178
- **Email:** hello@tsbrenterprises.com

Rebuilt 2026 — Obsidian Command theme, full Texas B2B content silo.
