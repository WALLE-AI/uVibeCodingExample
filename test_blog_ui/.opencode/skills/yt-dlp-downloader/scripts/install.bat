@echo off
setlocal

echo ========================================
echo yt-dlp Downloader - Installation
echo ========================================

REM Install yt-dlp
echo [1/3] Installing yt-dlp...
pip install -U yt-dlp
if errorlevel 1 (
    echo [ERROR] Failed to install yt-dlp
    exit /b 1
)
echo [OK] yt-dlp installed

REM Install Deno (JS runtime for faster YouTube extraction)
echo [2/3] Installing Deno (JavaScript runtime)...
if not exist "%USERPROFILE%\.deno\deno.exe" (
    powershell -Command "& {Invoke-WebRequest -Uri https://deno.land/install.ps1 -OutFile deno-install.ps1; ./deno-install.ps1; Remove-Item deno-install.ps1}"
) else (
    echo [OK] Deno already installed
)

REM Add Deno to PATH for current session
set PATH=%USERPROFILE%\.deno;%PATH%

echo [OK] Deno installed

REM Check for FFmpeg
echo [3/3] Checking FFmpeg...
where ffmpeg >nul 2>nul
if errorlevel 1 (
    echo [WARNING] FFmpeg not found. Video/audio merging may not work.
    echo [INFO] Install FFmpeg from https://ffmpeg.org/download.html
    echo [INFO] Or run: winget install FFmpeg
) else (
    echo [OK] FFmpeg found
)

echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo Tips:
echo - Deno enables faster YouTube extraction
echo - FFmpeg merges video and audio tracks
echo - Run scripts\download.bat to download videos
echo.
pause
endlocal
