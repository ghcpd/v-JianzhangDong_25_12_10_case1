# Environment & Test Runner (auto-generated)

This repository contains generated helper files to make the environment reproducible and test runs easy.

Files created/updated by the dependency maintenance run:

- `requirements_backup.txt`  — original copy of the project's requirements before updates
- `requirements.txt`       — updated to safe, compatible pinned versions for Python 3.14
- `report.json`            — list of packages that were changed and why
- `.venv/`                 — virtual environment created for testing (ignored by git)
- `Dockerfile`             — container recipe to reproduce the environment
- `setup.sh`               — creates `.venv` and installs pinned requirements (Linux/macOS)
- `run_test.sh`            — sets up `.venv`, runs tests and writes logs/test_run.log (Linux/macOS)
- `run_test.bat`           — sets up `.venv`, runs tests and writes logs\test_run.log (Windows)
- `auto_test.py`           — test runner which executes all scripts in `tests/` using `.venv` interpreter and writes logs/test_run.log
- `logs/`                  — test-run artifacts (ignored by git)

See the "Setup" and "Running tests" sections below for exact commands.

## Setup instructions (Linux / macOS)

1. Create a fresh virtual environment and install pinned dependencies:

```bash
./setup.sh
```

2. Alternatively run the whole test setup + test runner:

```bash
./run_test.sh
```

## Setup instructions (Windows)

1. Create a fresh virtual environment and install pinned dependencies:

```powershell
python -m venv .venv ; .\.venv\Scripts\activate ; python -m pip install --upgrade pip setuptools wheel ; pip install -r requirements.txt
```

2. Or use the helper batch script which will create the venv and run tests:

```cmd
run_test.bat
```

## Running tests

- Use `./run_test.sh` on Linux/macOS, or `run_test.bat` on Windows. These scripts create a fresh `.venv`, install dependencies and run `auto_test.py`. All test output is written to `logs/test_run.log`.

- You can also run `auto_test.py` directly with your interpreter (it will prefer `.venv` if present):

```bash
.venv/bin/python auto_test.py   # linux/macOS
.venv\Scripts\python.exe auto_test.py   # windows
```

## What `auto_test.py` does

- Executes each Python file under `tests/` with the Python interpreter inside `.venv` if present.
- Writes complete stdout/stderr and exit codes to `logs/test_run.log`.
- Appends environment metadata (environment name, absolute path, Python/pip versions) to this README each time the tests are run.

## Logs

- test results get appended to `logs/test_run.log`. See that file to inspect failures or stdout/stderr from individual test scripts.

---



Environment: .venv
Absolute path: D:\vscoderprojects\v-JianzhangDong_25_12_10_case1\oswe-mini-secondary\v-JianzhangDong_25_12_10_case1\.venv
Python: Python 3.14.0
pip: pip 25.3 from D:\vscoderprojects\v-JianzhangDong_25_12_10_case1\oswe-mini-secondary\v-JianzhangDong_25_12_10_case1\.venv\Lib\site-packages\pip (python 3.14)


Environment: .venv
Absolute path: D:\vscoderprojects\v-JianzhangDong_25_12_10_case1\oswe-mini-secondary\v-JianzhangDong_25_12_10_case1\.venv
Python: Python 3.14.0
pip: pip 25.3 from D:\vscoderprojects\v-JianzhangDong_25_12_10_case1\oswe-mini-secondary\v-JianzhangDong_25_12_10_case1\.venv\Lib\site-packages\pip (python 3.14)
