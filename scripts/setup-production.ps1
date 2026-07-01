#Requires -Version 5.1
<#
.SYNOPSIS
  One-shot production setup: forms, analytics, build, Cloudflare Pages deploy.

.EXAMPLE
  .\scripts\setup-production.ps1
  .\scripts\setup-production.ps1 -GaMeasurementId "G-XXXXXXXXXX"
#>
param(
    [string]$GaMeasurementId = "",
    [string]$FormEndpoint = "https://formsubmit.co/hello@tsbrenterprises.com",
    [string]$PagesProject = "tsbr-enterprises",
    [switch]$SkipDeploy
)

$ErrorActionPreference = "Stop"
$Root = Split-Path $PSScriptRoot -Parent
Set-Location $Root

function Write-EnvValue {
    param([string]$Key, [string]$Value)
    $envPath = Join-Path $Root ".env"
    $lines = @()
    if (Test-Path $envPath) { $lines = Get-Content $envPath -Encoding UTF8 }
    $found = $false
    $out = foreach ($line in $lines) {
        if ($line -match "^\s*$([regex]::Escape($Key))\s*=") {
            $found = $true
            "$Key=$Value"
        } else { $line }
    }
    if (-not $found) { $out += "$Key=$Value" }
    $out | Set-Content $envPath -Encoding UTF8
    Write-Host "  .env -> $Key" -ForegroundColor DarkGray
}

Write-Host "`n=== TSBR Production Setup ===" -ForegroundColor Cyan

# Load existing .env
$envFile = Join-Path $Root ".env"
if (Test-Path $envFile) {
    Get-Content $envFile | ForEach-Object {
        if ($_ -match '^\s*([^#=]+?)\s*=\s*(.+)$') {
            $k = $Matches[1].Trim(); $v = $Matches[2].Trim().Trim('"').Trim("'")
            if ($k -and $k -notin @('PATH','HOME')) { Set-Item -Path "env:$k" -Value $v }
        }
    }
}

if (-not $GaMeasurementId -and $env:TSBR_GA_MEASUREMENT_ID) {
    $GaMeasurementId = $env:TSBR_GA_MEASUREMENT_ID
}

if (-not $GaMeasurementId) {
    Write-Host "`nGA4: No measurement ID found." -ForegroundColor Yellow
    Write-Host "  1. Open https://analytics.google.com/"
    Write-Host "  2. Admin -> Create property 'TSBR Enterprises' for tsbrenterprises.com"
    Write-Host "  3. Data stream -> Web -> copy Measurement ID (G-XXXXXXXXXX)"
    Write-Host "  4. Re-run: .\scripts\setup-production.ps1 -GaMeasurementId 'G-XXXXXXXXXX'"
} else {
    Write-EnvValue -Key "TSBR_GA_MEASUREMENT_ID" -Value $GaMeasurementId
    Write-Host "GA4 configured: $GaMeasurementId" -ForegroundColor Green
}

Write-EnvValue -Key "TSBR_FORMSPREE_ENDPOINT" -Value $FormEndpoint
Write-Host "Contact forms -> $FormEndpoint" -ForegroundColor Green

Write-Host "`nBuilding site..."
python _build.py
if ($LASTEXITCODE -ne 0) { throw "Build failed" }

if ($SkipDeploy) {
    Write-Host "Skipping deploy (-SkipDeploy)." -ForegroundColor Yellow
    exit 0
}

if (-not $env:CLOUDFLARE_API_TOKEN) {
    if (Test-Path $envFile) {
        Get-Content $envFile | ForEach-Object {
            if ($_ -match '^\s*CLOUDFLARE_API_TOKEN\s*=\s*(.+)$') {
                $env:CLOUDFLARE_API_TOKEN = $Matches[1].Trim().Trim('"').Trim("'")
            }
            if ($_ -match '^\s*CLOUDFLARE_ACCOUNT_ID\s*=\s*(.+)$') {
                $env:CLOUDFLARE_ACCOUNT_ID = $Matches[1].Trim().Trim('"').Trim("'")
            }
        }
    }
}

if (-not $env:CLOUDFLARE_API_TOKEN) {
    Write-Host "Cloudflare credentials not in .env — run deploy manually:" -ForegroundColor Yellow
    Write-Host "  npx wrangler pages deploy . --project-name $PagesProject --branch main"
    exit 0
}

Write-Host "`nDeploying to Cloudflare Pages ($PagesProject)..."
npx --yes wrangler@latest pages deploy . --project-name $PagesProject --branch main --commit-dirty=true
if ($LASTEXITCODE -ne 0) { throw "Cloudflare deploy failed" }

Write-Host "`nProduction setup complete." -ForegroundColor Green
Write-Host "  Preview:  http://localhost:8080"
Write-Host "  Live:     https://$PagesProject.pages.dev"
Write-Host "  Domain:   Add CNAME tsbrenterprises.com to $PagesProject.pages.dev in Cloudflare DNS"
Write-Host ""