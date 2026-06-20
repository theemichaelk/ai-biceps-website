#Requires -Version 5.1
<#
.SYNOPSIS
  Build and deploy the TSBR static website.

.PARAMETER Method
  copy | ftp | sftp | preview

.EXAMPLE
  .\scripts\deploy.ps1 -Method preview
  .\scripts\deploy.ps1 -Method copy
  .\scripts\deploy.ps1 -Method ftp
#>
param(
    [ValidateSet("preview", "copy", "ftp", "sftp")]
    [string]$Method = "preview",
    [string]$ConfigPath = "",
    [int]$PreviewPort = 8080
)

$ErrorActionPreference = "Stop"
$Root = Split-Path $PSScriptRoot -Parent
Set-Location $Root

if (-not $ConfigPath) { $ConfigPath = Join-Path $Root "deploy.config.json" }

function Get-DeployConfig {
    if (-not (Test-Path $ConfigPath)) {
        if ($Method -ne "preview") {
            throw "Missing $ConfigPath — copy deploy.config.example.json and edit it."
        }
        return $null
    }
    return Get-Content $ConfigPath -Raw | ConvertFrom-Json
}

function Get-FilesToDeploy {
    param($Exclude)
    $all = Get-ChildItem -Path $Root -Recurse -File | Where-Object {
        $rel = $_.FullName.Substring($Root.Length + 1)
        $skip = $false
        foreach ($pat in $Exclude) {
            if ($rel -eq $pat -or $rel -like "$pat\*" -or $rel -like "*\$pat") { $skip = $true; break }
        }
        -not $skip
    }
    return $all
}

Write-Host "`n=== TSBR Deploy ($Method) ===" -ForegroundColor Cyan

# Load .env for credentials
$envFile = Join-Path $Root ".env"
if (Test-Path $envFile) {
    Get-Content $envFile | ForEach-Object {
        if ($_ -match '^\s*([^#=]+?)\s*=\s*(.+)$') {
            $k = $Matches[1].Trim(); $v = $Matches[2].Trim().Trim('"').Trim("'")
            if ($k -and $k -notin @('PATH','HOME')) { Set-Item -Path "env:$k" -Value $v }
        }
    }
}

Write-Host "Building site..."
python _build.py
if ($LASTEXITCODE -ne 0) { throw "Build failed" }

$config = Get-DeployConfig
$exclude = @("_build.py", "_content.py", "_content_extra.py", "_config.py", "formspree.json",
    ".env", ".env.example", ".gitignore", "deploy.config.example.json", "deploy.config.json",
    "scripts", "__pycache__")
if ($config -and $config.exclude) { $exclude = $config.exclude }

switch ($Method) {
    "preview" {
        Write-Host "Starting preview server at http://localhost:$PreviewPort"
        Write-Host "Press Ctrl+C to stop."
        python -m http.server $PreviewPort
    }
    "copy" {
        $dest = $config.localCopyPath
        if (-not $dest) { $dest = $env:TSBR_DEPLOY_LOCAL_PATH }
        if (-not $dest) { throw "Set localCopyPath in deploy.config.json or TSBR_DEPLOY_LOCAL_PATH in .env" }
        if (-not (Test-Path $dest)) { New-Item -ItemType Directory -Path $dest -Force | Out-Null }
        $files = Get-FilesToDeploy -Exclude $exclude
        $count = 0
        foreach ($f in $files) {
            $rel = $f.FullName.Substring($Root.Length + 1)
            $target = Join-Path $dest $rel
            $dir = Split-Path $target -Parent
            if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
            Copy-Item $f.FullName $target -Force
            $count++
        }
        Write-Host "Copied $count files to $dest" -ForegroundColor Green
    }
    "ftp" {
        $ftp = $config.ftp
        if (-not $ftp) { throw "ftp section missing in deploy.config.json" }
        $passVar = $ftp.passwordEnv
        $passItem = Get-Item "env:$passVar" -ErrorAction SilentlyContinue
        $pass = if ($passItem) { $passItem.Value } else { $null }
        if (-not $pass) { $pass = $env:TSBR_FTP_PASSWORD }
        if (-not $pass) { throw "Set $($ftp.passwordEnv) or TSBR_FTP_PASSWORD in .env" }
        $files = Get-FilesToDeploy -Exclude $exclude
        $uploaded = 0
        foreach ($f in $files) {
            $rel = $f.FullName.Substring($Root.Length + 1).Replace("\", "/")
            $remote = "$($ftp.remotePath.TrimEnd('/'))/$rel"
            $uri = "ftp://$($ftp.host)$remote"
            $req = [System.Net.FtpWebRequest]::Create($uri)
            $req.Method = [System.Net.WebRequestMethods+Ftp]::UploadFile
            $req.Credentials = New-Object System.Net.NetworkCredential($ftp.user, $pass)
            $req.UseBinary = $true
            $bytes = [System.IO.File]::ReadAllBytes($f.FullName)
            $req.ContentLength = $bytes.Length
            $stream = $req.GetRequestStream()
            $stream.Write($bytes, 0, $bytes.Length)
            $stream.Close()
            $req.GetResponse().Close()
            $uploaded++
            Write-Host "  ↑ $rel"
        }
        Write-Host "FTP upload complete: $uploaded files" -ForegroundColor Green
    }
    "sftp" {
        throw "SFTP deploy requires WinSCP or OpenSSH sftp. Use -Method copy or ftp, or upload via your host panel."
    }
}

Write-Host "Done.`n" -ForegroundColor Green