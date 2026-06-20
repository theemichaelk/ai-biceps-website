#Requires -Version 5.1
<#
.SYNOPSIS
  Authenticate with GitHub (if needed), create remote repo, and push.

.EXAMPLE
  .\scripts\push-to-github.ps1
  .\scripts\push-to-github.ps1 -RepoName "ai-biceps-website" -Private
#>
param(
    [string]$RepoName = "ai-biceps-website",
    [switch]$Private
)

$ErrorActionPreference = "Stop"
$Root = Split-Path $PSScriptRoot -Parent
Set-Location $Root

$gh = "C:\Program Files\GitHub CLI\gh.exe"
if (-not (Test-Path $gh)) {
    $ghCmd = Get-Command gh -ErrorAction SilentlyContinue
    if ($ghCmd) { $gh = $ghCmd.Source } else { throw "GitHub CLI (gh) not found. Install from https://cli.github.com/" }
}

Write-Host "`n=== Push TSBR site to GitHub ===" -ForegroundColor Cyan

& $gh auth status 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "GitHub login required. Complete the browser flow when prompted." -ForegroundColor Yellow
    & $gh auth login -h github.com -p https -w
}

$visibility = if ($Private) { "--private" } else { "--public" }
$desc = "The Stone Builders Rejected (TSBR) — Texas B2B local SEO static website"

if (git remote get-url origin 2>$null) {
    Write-Host "Remote 'origin' already exists. Pushing to main..."
    git push -u origin main
} else {
    Write-Host "Creating GitHub repo: $RepoName ($($visibility.TrimStart('-')))"
    & $gh repo create $RepoName $visibility --description $desc --source=. --remote=origin --push
}

if ($LASTEXITCODE -ne 0) { throw "GitHub push failed" }

$repoUrl = (& $gh repo view --json url -q .url 2>$null)
Write-Host "`nRepository ready:" -ForegroundColor Green
Write-Host "  $repoUrl"