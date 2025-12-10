@echo off
if not exist .venv (
  echo .venv not found — run setup.bat or setup.sh first
  exit /b 1
)
.venv\Scripts\python.exe auto_test.py
pause