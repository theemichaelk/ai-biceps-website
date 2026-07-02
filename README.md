# The Stone Builders Rejected (TSBR Enterprises)

Texas Local SEO agency website — **Lever theme** (synced from S3 reference).

### Local preview
```powershell
python -m http.server 8080
```
Open http://localhost:8080

### Deploy (Cloudflare Pages)
```powershell
$env:CLOUDFLARE_API_TOKEN="your-token"
$env:CLOUDFLARE_ACCOUNT_ID="your-account-id"
npx wrangler pages deploy . --project-name tsbr-enterprises --branch main
```

### Site structure
- `index.html` — Lever single-page homepage (hero, skills, services, team, newsletter, contact)
- `lever/assets/` — Lever theme CSS, JS, images, video
- `blog/` — Blog section (Bootstrap theme)
- `error.html` — 404 page

### Legacy Python build
Previous Obsidian Command theme generator files (`_build.py`, `_content.py`, etc.) and old HTML pages are kept for reference under `_legacy/` and in the Python modules at repo root.