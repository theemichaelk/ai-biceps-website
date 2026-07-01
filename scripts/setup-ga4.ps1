#Requires -Version 5.1
<#
.SYNOPSIS
  Configure GA4 measurement ID and rebuild the site.

.EXAMPLE
  .\scripts\setup-ga4.ps1 -MeasurementId "G-XXXXXXXXXX"
#>
param(
    [Parameter(Mandatory = $true)]
    [string]$MeasurementId
)

if ($MeasurementId -notmatch '^G-[A-Z0-9]+$') {
    throw "Invalid GA4 measurement ID. Expected format G-XXXXXXXXXX"
}

$Root = Split-Path $PSScriptRoot -Parent
Set-Location $Root

& "$PSScriptRoot\setup-production.ps1" -GaMeasurementId $MeasurementId -SkipDeploy

Write-Host "`nGA4 active in all pages. Redeploy with:" -ForegroundColor Green
Write-Host "  .\scripts\setup-production.ps1"