@echo off
setlocal enabledelayedexpansion

if "%~1"=="" (
    echo Usage: download.bat "URL1" "URL2" ...
    echo.
    echo Examples:
    echo   download.bat "https://youtube.com/watch?v=..."
    echo   download.bat "https://youtube.com/watch?v=..." "https://vimeo.com/..."
    echo   download.bat "https://youtube.com/playlist?list=..."
    exit /b 1
)

echo ========================================
echo yt-dlp Video Downloader (Optimized)
echo ========================================
echo.

:loop
if "%~1"=="" goto end

echo Downloading: %~1
echo.

yt-dlp --js-runtimes deno -f "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]" -o "%%(title)s_%%(id)s.%%(ext)s" "%~1"

echo.
if errorlevel 1 (
    echo [FAILED] %~1
) else (
    echo [SUCCESS] %~1
)
echo ---------------------------------------
echo.

shift
goto loop

:end
echo ========================================
echo All downloads complete!
echo ========================================
endlocal
pause
