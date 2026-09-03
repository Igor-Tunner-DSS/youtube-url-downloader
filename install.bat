@echo off
setlocal EnableExtensions EnableDelayedExpansion

title YouTube Audio Downloader - Installer

echo ============================================================
echo        YouTube Audio Downloader - Dependency Installer
echo ============================================================
echo.

REM ------------------------------------------------------------
REM Check Python
REM ------------------------------------------------------------
echo [1/3] Checking Python...

where py >nul 2>&1
if %errorlevel%==0 (
    set "PYTHON=py"
    goto :python_found
)

where python >nul 2>&1
if %errorlevel%==0 (
    set "PYTHON=python"
    goto :python_found
)

echo.
echo ERROR: Python was not found.
echo.
echo Please install Python 3.9 or newer from:
echo https://www.python.org/downloads/
echo.
echo During installation, enable "Add Python to PATH".
echo.
pause
exit /b 1

:python_found
for /f "tokens=*" %%V in ('%PYTHON% --version 2^>^&1') do set "PYTHON_VERSION=%%V"
echo       Found: %PYTHON_VERSION%

REM Check Python major/minor version using Python itself
%PYTHON% -c "import sys; raise SystemExit(0 if sys.version_info >= (3,9) else 1)" >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python 3.9 or newer is required.
    echo.
    pause
    exit /b 1
)

REM ------------------------------------------------------------
REM Install/update yt-dlp
REM ------------------------------------------------------------
echo.
echo [2/3] Installing/updating yt-dlp...

%PYTHON% -m pip --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: pip is not available for this Python installation.
    echo Try running:
    echo     %PYTHON% -m ensurepip --upgrade
    echo.
    pause
    exit /b 1
)

%PYTHON% -m pip install --upgrade yt-dlp
if errorlevel 1 (
    echo.
    echo ERROR: Failed to install yt-dlp.
    echo.
    pause
    exit /b 1
)

echo       yt-dlp installed successfully.

REM ------------------------------------------------------------
REM Check/install FFmpeg
REM ------------------------------------------------------------
echo.
echo [3/3] Checking FFmpeg...

where ffmpeg >nul 2>&1
if %errorlevel%==0 (
    for /f "tokens=*" %%V in ('ffmpeg -version 2^>nul ^| findstr /B "ffmpeg version"') do set "FFMPEG_VERSION=%%V"
    echo       FFmpeg found: !FFMPEG_VERSION!
    goto :finished
)

echo       FFmpeg was not found in PATH.
echo.

REM Try installing FFmpeg through winget if available
where winget >nul 2>&1
if %errorlevel%==0 (
    echo       Windows Package Manager (winget) was found.
    echo       Attempting to install FFmpeg...
    echo.

    winget install --id Gyan.FFmpeg.Shared -e --accept-source-agreements --accept-package-agreements

    REM Refresh PATH for the current process if possible
    set "PATH=%PATH%;%LOCALAPPDATA%\Microsoft\WinGet\Links"

    where ffmpeg >nul 2>&1
    if %errorlevel%==0 goto :finished

    echo.
    echo FFmpeg may have been installed, but this terminal has not
    echo picked up the updated PATH yet.
    echo Please close this terminal, open a new one, and run:
    echo     ffmpeg -version
    echo.
    goto :finished_with_warning
)

echo ============================================================
echo WARNING: FFmpeg could not be installed automatically.
echo.
echo Install FFmpeg manually from:
echo https://ffmpeg.org/download.html
echo.
echo After installing it, make sure ffmpeg.exe is available in
echo your system PATH.
echo ============================================================
echo.
goto :finished_with_warning

:finished
echo.
echo ============================================================
echo Installation completed successfully!
echo.
echo Dependencies:
echo   - Python:  OK
echo   - yt-dlp:  OK
echo   - FFmpeg:  OK
echo.
echo You can now run:
echo     %PYTHON% youtube_audio_downloader.py
echo ============================================================
echo.
pause
exit /b 0

:finished_with_warning
echo.
echo ============================================================
echo Installation partially completed.
echo.
echo Python and yt-dlp are ready.
echo FFmpeg still needs to be verified.
echo.
echo Run:
echo     ffmpeg -version
echo.
echo before running the downloader.
echo ============================================================
echo.
pause
exit /b 0
