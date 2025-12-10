@echo off
IF NOT EXIST .venv (echo .venv not found. Run setup.sh or create .venv first.& exit /b 1)
.venv\Scripts\activate
python -m auto_test
