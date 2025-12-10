@echo off
REM Create a fresh environment in .venv then run auto_test.py
IF EXIST .venv (
  echo Removing existing .venv
  rmdir /s /q .venv
)

python -m venv .venv
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

if not exist logs mkdir logs
echo Running tests and writing output to logs\test_run.log
python auto_test.py > logs\test_run.log 2>&1
type logs\test_run.log
