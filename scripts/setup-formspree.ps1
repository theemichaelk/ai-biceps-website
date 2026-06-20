#Requires -Version 5.1
<#
.SYNOPSIS
  Configure Formspree for TSBR website forms and rebuild HTML.

.DESCRIPTION
  Three ways to configure:
  1. Pass -Endpoint "https://formspree.io/f/xxxxx" (from Formspree dashboard → Integration tab)
  2. Set FORMSPREE_DEPLOY_KEY in .env and run without -Endpoint (uses formspree.json + CLI deploy)
  3. Interactive prompt if neither is provided

.EXAMPLE
  .\scripts\setup-formspree.ps1 -Endpoint "https://formspree.io/f/mabcdefg"
.EXAMPLE
  # After adding FORMSPREE_DEPLOY_KEY to .env:
  .\scripts\setup-formspree.ps1 -Deploy
#>
param(
    [string]$Endpoint,
    [switch]$Deploy,
    [switch]$Test
)

$ErrorActionPreference = "Stop"
$Root = Split-Path $PSScriptRoot -Parent
Set-Location $Root

function Write-EnvValue {
    param([string]$Key, [string]$Value)
    $envPath = Join-Path $Root ".env"
    $lines = @()
    if (Test-Path $envPath) {
        $lines = Get-Content $envPath -Encoding UTF8
    }
    $found = $false
    $out = foreach ($line in $lines) {
        if ($line -match "^\s*$([regex]::Escape($Key))\s*=") {
            $found = $true
            "$Key=$Value"
        } else { $line }
    }
    if (-not $found) { $out += "$Key=$Value" }
    $out | Set-Content $envPath -Encoding UTF8
    Write-Host "  Updated .env → $Key"
}

function Test-FormspreeEndpoint {
    param([string]$Url)
    Write-Host "Testing endpoint (dry POST)..."
    try {
        $body = @{
            name = "TSBR Setup Test"
            business = "Test Co"
            _subject = "TSBR Formspree Setup Test"
            message = "Automated setup verification — safe to ignore."
        }
        $resp = Invoke-WebRequest -Uri $Url -Method POST -Body $body -UseBasicParsing -TimeoutSec 20
        Write-Host "  Response: $($resp.StatusCode) $($resp.StatusDescription)" -ForegroundColor Green
        return $true
    } catch {
        $code = $_.Exception.Response.StatusCode.value__
        if ($code -eq 422 -or $code -eq 200 -or $code -eq 302) {
            Write-Host "  Endpoint accepted submission (HTTP $code)." -ForegroundColor Green
            return $true
        }
        Write-Host "  Warning: $($_.Exception.Message)" -ForegroundColor Yellow
        return $false
    }
}

Write-Host "`n=== TSBR Formspree Setup ===" -ForegroundColor Cyan

# --- Deploy via CLI if requested ---
if ($Deploy -or (-not $Endpoint -and $env:FORMSPREE_DEPLOY_KEY)) {
    if (-not $env:FORMSPREE_DEPLOY_KEY -and (Test-Path (Join-Path $Root ".env"))) {
        Get-Content (Join-Path $Root ".env") | ForEach-Object {
            if ($_ -match '^\s*FORMSPREE_DEPLOY_KEY\s*=\s*(.+)$') {
                $env:FORMSPREE_DEPLOY_KEY = $Matches[1].Trim().Trim('"').Trim("'")
            }
        }
    }
    if ($env:FORMSPREE_DEPLOY_KEY) {
        Write-Host "Deploying formspree.json via Formspree CLI..."
        $deployOut = npx --yes @formspree/cli@latest deploy -k $env:FORMSPREE_DEPLOY_KEY 2>&1 | Out-String
        Write-Host $deployOut
        if ($deployOut -match '(https://formspree\.io/f/[a-zA-Z0-9]+)') {
            $Endpoint = $Matches[1]
            Write-Host "  Detected endpoint: $Endpoint" -ForegroundColor Green
        } else {
            Write-Host @"

Deploy completed. Copy your form endpoint from the Formspree dashboard:
  https://formspree.io → Your project → tsbr-inquiries → Integration tab
Then run:
  .\scripts\setup-formspree.ps1 -Endpoint "https://formspree.io/f/YOUR_ID"

"@ -ForegroundColor Yellow
        }
    }
}

# --- Interactive or direct endpoint ---
if (-not $Endpoint) {
    Write-Host @"

No Formspree endpoint configured yet.

Quick setup:
  1. Sign in at https://formspree.io (use hello@tsbrenterprises.com)
  2. Create a project → Add form OR run: .\scripts\setup-formspree.ps1 -Deploy
     (requires FORMSPREE_DEPLOY_KEY in .env — find it under Settings → Deploy key)
  3. Copy the form endpoint (https://formspree.io/f/xxxxx)

"@ -ForegroundColor Yellow
    $Endpoint = Read-Host "Paste your Formspree endpoint URL (or press Enter to skip)"
    if (-not $Endpoint) {
        Write-Host "Skipped. Forms will use mailto fallback until endpoint is set." -ForegroundColor Yellow
        exit 0
    }
}

if ($Endpoint -notmatch '^https://formspree\.io/f/[a-zA-Z0-9]+$') {
    throw "Invalid endpoint format. Expected https://formspree.io/f/xxxxxxxx"
}

Write-EnvValue -Key "TSBR_FORMSPREE_ENDPOINT" -Value $Endpoint

if ($Test) { Test-FormspreeEndpoint -Url $Endpoint | Out-Null }

Write-Host "`nRebuilding site..."
python _build.py
if ($LASTEXITCODE -ne 0) { throw "Build failed" }

$contact = Get-Content (Join-Path $Root "contact.html") -Raw
if ($contact -match [regex]::Escape($Endpoint)) {
    Write-Host "`nFormspree configured successfully." -ForegroundColor Green
    Write-Host "  Endpoint: $Endpoint"
    Write-Host "  Next: restrict form to tsbrenterprises.com in Formspree → Form settings → Restrict to Domain"
} else {
    Write-Host "`nBuild complete but endpoint not found in contact.html — check _config.py." -ForegroundColor Yellow
}