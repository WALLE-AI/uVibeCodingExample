#!/usr/bin/env pwsh

# Pake Web-to-Desktop Packaging Script (PowerShell)
# Usage: .\scripts\package.ps1 [-BuildDir <string>] [-Port <int>] [-AppName <string>] [-Icon <string>]

param(
    [string]$BuildDir = "dist",
    [int]$Port = 3000,
    [string]$AppName = "MyApp",
    [string]$Icon = ""
)

$ErrorActionPreference = "Stop"

function Write-Step {
    param([string]$Message)
    Write-Host "==>" -ForegroundColor Green -NoNewline
    Write-Host " $Message"
}

function Write-Warn {
    param([string]$Message)
    Write-Host "WARNING:" -ForegroundColor Yellow -NoNewline
    Write-Host " $Message"
}

function Write-Error {
    param([string]$Message)
    Write-Host "ERROR:" -ForegroundColor Red -NoNewline
    Write-Host " $Message"
}

function Test-Prerequisites {
    Write-Step "Checking prerequisites..."

    # Check Node.js
    try {
        $nodeVersion = node --version
        Write-Step "Node.js version: $nodeVersion"
    }
    catch {
        Write-Error "Node.js is not installed. Please install Node.js >= 22"
        exit 1
    }

    # Check Pake CLI
    try {
        $pakeVersion = pake --version
        Write-Step "Pake CLI version: $pakeVersion"
    }
    catch {
        Write-Warn "Pake CLI not found. Installing..."
        npm install -g pake-cli
    }

    Write-Step "Prerequisites check passed"
}

function Test-BuildDirectory {
    param([string]$BuildDir)

    Write-Step "Checking build directory: $BuildDir"

    if (-not (Test-Path $BuildDir)) {
        Write-Error "Build directory '$BuildDir' not found. Run your build command first:"
        Write-Host "  npm run build   # for React/Vue/Vite" -ForegroundColor Cyan
        Write-Host "  pnpm build" -ForegroundColor Cyan
        exit 1
    }

    if (-not (Test-Path "$BuildDir\index.html")) {
        Write-Error "index.html not found in $BuildDir"
        exit 1
    }

    Write-Step "Build directory is valid"
}

function Start-Server {
    param(
        [string]$BuildDir,
        [int]$Port
    )

    Write-Step "Starting local server on port $Port..."

    # Kill any existing server on this port
    $existingProcess = Get-Process -ErrorAction SilentlyContinue | Where-Object {
        $_.Ports -like "*$Port*" -or ($_.CommandLine -and $_.CommandLine.Contains($Port.ToString()))
    }

    if ($existingProcess) {
        Write-Warn "Stopping existing process on port $Port"
        $existingProcess | Stop-Process -Force
    }

    # Start server in background
    if (Get-Command npx -ErrorAction SilentlyContinue) {
        $script = {
            param($Dir, $P)
            npx serve $Dir -l $P
        }
        $job = Start-Job -ScriptBlock $script -ArgumentList $BuildDir, $Port
    }
    else {
        Write-Warn "npx not found, trying Python..."
        $script = {
            param($Dir, $P)
            python -m http.server $P --directory $Dir
        }
        $job = Start-Job -ScriptBlock $script -ArgumentList $BuildDir, $Port
    }

    # Wait for server to start
    Start-Sleep -Seconds 2

    Write-Step "Server started"
    return $job
}

function Invoke-Package {
    param(
        [int]$Port,
        [string]$AppName,
        [string]$Icon
    )

    $url = "http://localhost:$Port"

    Write-Step "Packaging $AppName..."

    $pakeArgs = @(
        "--name", $AppName
    )

    if ($Icon) {
        $pakeArgs += "--icon", $Icon
    }

    pake $url @pakeArgs

    Write-Step "Packaging complete!"
}

function Stop-Server {
    param($Job)

    if ($Job) {
        Write-Step "Stopping server..."
        Stop-Job $Job
        Remove-Job $Job -ErrorAction SilentlyContinue
    }
}

# Main execution
function Main {
    Write-Host ""
    Write-Host "=========================================" -ForegroundColor Cyan
    Write-Host "  Pake Web-to-Desktop Packaging Script" -ForegroundColor Cyan
    Write-Host "=========================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "  Build Dir: $BuildDir" -ForegroundColor White
    Write-Host "  Port:      $Port" -ForegroundColor White
    Write-Host "  App Name:  $AppName" -ForegroundColor White
    Write-Host "  Icon:      $(if ($Icon) { $Icon } else { 'auto' })" -ForegroundColor White
    Write-Host ""
    Write-Host "=========================================" -ForegroundColor Cyan
    Write-Host ""

    $serverJob = $null

    try {
        Test-Prerequisites
        Test-BuildDirectory -BuildDir $BuildDir
        $serverJob = Start-Server -BuildDir $BuildDir -Port $Port
        Invoke-Package -Port $Port -AppName $AppName -Icon $Icon
    }
    finally {
        Stop-Server -Job $serverJob
    }
}

Main
