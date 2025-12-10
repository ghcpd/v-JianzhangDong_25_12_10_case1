@echo off
REM setup.bat - Environment setup script for Windows
REM This script creates a virtual environment and installs dependencies

setlocal enabledelayedexpansion

echo ======================================
echo Project Environment Setup (Windows)
echo ======================================
echo.

REM Check if Python 3.14+ is available
echo Checking Python version...
for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo Found: %PYTHON_VERSION%
echo.

REM Create virtual environment
echo Creating virtual environment at .venv...
if exist ".venv" (
    echo Removing existing .venv directory...
    rmdir /s /q .venv
)

python -m venv .venv
if errorlevel 1 (
    echo Error: Failed to create virtual environment
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo Note: Could not activate virtual environment using batch file.
    echo Using python.exe directly to install packages.
)

REM Upgrade pip, setuptools, and wheel
echo.
echo Upgrading pip, setuptools, and wheel...
.\.venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel

REM Install dependencies
echo.
echo Installing dependencies from requirements.txt...
echo This may take several minutes...
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 (
    echo Warning: Some packages may have failed to install. Please check the output above.
)

REM Display environment info
echo.
echo ======================================
echo Environment Setup Complete!
echo ======================================
echo.
echo Environment Details:
for /f "tokens=*" %%i in ('.\.venv\Scripts\python.exe --version') do echo   Python Version: %%i
for /f "tokens=*" %%i in ('.\.venv\Scripts\python.exe -m pip --version') do echo   Pip Version: %%i
echo   Virtual Environment: %CD%\.venv
echo.
echo To activate the environment, run:
echo   .venv\Scripts\activate.bat
echo.
echo To run tests, execute:
echo   run_test.bat
echo.
echo To run automated tests with logging, execute:
echo   .venv\Scripts\python.exe auto_test.py
echo.
