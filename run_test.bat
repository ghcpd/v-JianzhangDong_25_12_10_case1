@echo off
REM run_test.bat - Test runner script for Windows
REM This script runs all test files in the tests\ directory

setlocal enabledelayedexpansion

echo ======================================
echo Running Tests (Windows)
echo ======================================
echo.

REM Check if virtual environment exists
if not exist ".venv\" (
    echo Error: Virtual environment not found at .venv
    echo Please run setup.bat first to create the environment.
    exit /b 1
)

REM Activate virtual environment
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo Error: Failed to activate virtual environment
    exit /b 1
)

echo Environment Information:
for /f "tokens=*" %%i in ('python --version') do echo   Python: %%i
for /f "tokens=*" %%i in ('pip --version') do echo   Pip: %%i
echo   Virtual Environment: %CD%\.venv
echo.

REM Create logs directory if it doesn't exist
if not exist "logs" mkdir logs

REM Run tests
echo Running test suite...
echo.

set TEST_DIR=tests
set FAILED=0
set PASSED=0

if not exist "%TEST_DIR%" (
    echo Error: Tests directory not found at %TEST_DIR%
    exit /b 1
)

REM Run each test file
for %%F in (%TEST_DIR%\*.py) do (
    set test_name=%%~nF
    echo Running !test_name!...
    REM Run with PYTHONPATH set to current directory
    set PYTHONPATH=%CD%
    python "%%F"
    if errorlevel 1 (
        echo X !test_name! failed
        set /a FAILED+=1
    ) else (
        echo + !test_name! passed
        set /a PASSED+=1
    )
    echo.
)

echo ======================================
echo Test Summary
echo ======================================
echo Passed: %PASSED%
echo Failed: %FAILED%
echo.

if %FAILED% equ 0 (
    echo All tests passed!
    exit /b 0
) else (
    echo Some tests failed. Check output above for details.
    exit /b 1
)
