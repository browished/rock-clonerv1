@echo off
setlocal enabledelayedexpansion

:: ---- Check for Python ----
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Python is not installed on this system.
    echo Please install Python 3.11.5 or later from:
    echo https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe
    pause
    exit /b 1
)

echo.
echo [✔] Python found. Installing requirements...

:: ---- Install requirements ----
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Failed to install some requirements.
    echo Make sure your internet is working and try again.
    pause
    exit /b 1
)

echo.
echo [✔] All dependencies installed successfully!
pause
