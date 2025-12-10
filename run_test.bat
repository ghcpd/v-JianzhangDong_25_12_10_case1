@echo off
REM Activate .venv and run tests, write output to logs\test_run.log
set VENV_DIR=.venv
if not exist logs mkdir logs
set LOG_FILE=logs\test_run.log

echo === Test run started: %DATE% %TIME% > %LOG_FILE%
if exist %VENV_DIR%\Scripts\activate (
  call %VENV_DIR%\Scripts\activate
  set PY=%VENV_DIR%\Scripts\python.exe
) else (
  set PY=python
)

REM Ensure tests can import local package 'app' by adding current directory to PYTHONPATH
set PYTHONPATH=%CD% %PYTHONPATH%

for %%F in (tests\*.py) do (
  echo --- Running %%~nxF --- >> %LOG_FILE%
  "%PY%" "%%F" >> %LOG_FILE% 2>&1
)

echo === Test run finished: %DATE% %TIME% >> %LOG_FILE%