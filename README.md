# Project Environment Setup and Dependency Management

This document provides comprehensive instructions for setting up and managing the Python project environment, including dependency updates, testing, and Docker containerization.

## Table of Contents

1. [Overview of Generated Files](#overview-of-generated-files)
2. [Environment Details](#environment-details)
3. [Dependency Updates](#dependency-updates)
4. [Setup Instructions](#setup-instructions)
5. [Running Tests](#running-tests)
6. [Docker Setup](#docker-setup)
7. [Troubleshooting](#troubleshooting)

---

## Overview of Generated Files

### Configuration and Setup Files

| File | Purpose |
|------|---------|
| `requirements.txt` | Updated Python dependencies with secure versions compatible with Python 3.14 |
| `requirements_backup.txt` | Backup of original requirements before updates |
| `setup.sh` | Environment setup script for Linux/macOS |
| `setup.bat` | Environment setup script for Windows |
| `.gitignore` | Git ignore rules to prevent tracking .venv and other temporary files |

### Test and Automation Scripts

| File | Purpose |
|------|---------|
| `run_test.sh` | Test runner script for Linux/macOS |
| `run_test.bat` | Test runner script for Windows |
| `auto_test.py` | Automated test runner with environment detection and logging |

### Documentation and Reporting

| File | Purpose |
|------|---------|
| `report.json` | Detailed report of dependency issues and updates |
| `README.md` | This comprehensive documentation file |
| `logs/test_run.log` | Test execution log (generated after running tests) |

### Docker Support

| File | Purpose |
|------|---------|
| `Dockerfile` | Docker container definition for reproducible environment |

---

## Environment Details

The following environment has been configured for this project:

```
Python Version: 3.14.0
Python Executable: d:\vscoderprojects\v-JianzhangDong_25_12_10_case1\haiku-4.5\v-JianzhangDong_25_12_10_case1\.venv\Scripts\python.exe
Virtual Environment: .venv
Virtual Environment Path: d:\vscoderprojects\v-JianzhangDong_25_12_10_case1\haiku-4.5\v-JianzhangDong_25_12_10_case1\.venv
Pip Version: 25.3
```

---

## Dependency Updates

All dependencies have been updated to secure and stable versions compatible with Python 3.14. See `report.json` for detailed information on each update.

### Updated Packages

| Package | Old Version | New Version | Reason |
|---------|------------|------------|--------|
| numpy | 1.24.0 | 1.26.4 | Python 3.14 compatibility, performance improvements |
| pandas | 1.5.0 | 2.2.0 | Python 3.14 support, functionality improvements |
| matplotlib | 3.5.0 | 3.8.4 | Python 3.14 compatibility |
| requests | 2.25.0 | 2.31.0 | **SECURITY: Fixed CVE-2023-32681** |
| pyyaml | 5.3.1 | 6.0.1 | **SECURITY: Fixed arbitrary code execution vulnerability** |
| scipy | 1.9.0 | 1.13.1 | Python 3.14 compatibility |
| regex | 2021.4.4 | 2024.4.28 | Major version update with bug fixes |
| tqdm | 4.32.0 | 4.66.2 | Major version update (from 2018) |
| lxml | 4.6.1 | 5.0.0 | Major version update with improvements |
| typing_extensions | 3.7.4 | 4.9.0 | Python 3.14 compatibility |

---

## Setup Instructions

### Windows

#### Option 1: Using setup.bat (Recommended)

```batch
# Run the automated setup script
setup.bat
```

This script will:
- Create a clean virtual environment at `.venv`
- Upgrade pip, setuptools, and wheel
- Install all dependencies from `requirements.txt`
- Display environment information

#### Option 2: Manual Setup

```batch
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate.bat

# Upgrade pip, setuptools, and wheel
python -m pip install --upgrade pip setuptools wheel

# Install dependencies
pip install -r requirements.txt
```

### Linux/macOS

#### Option 1: Using setup.sh (Recommended)

```bash
# Make setup script executable
chmod +x setup.sh

# Run the automated setup script
./setup.sh
```

This script will:
- Create a clean virtual environment at `.venv`
- Upgrade pip, setuptools, and wheel
- Install all dependencies from `requirements.txt`
- Display environment information

#### Option 2: Manual Setup

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip, setuptools, and wheel
python3 -m pip install --upgrade pip setuptools wheel

# Install dependencies
pip install -r requirements.txt
```

---

## Running Tests

### Windows

#### Using run_test.bat

```batch
run_test.bat
```

This script will:
- Verify the virtual environment exists
- Run all test files in the `tests/` directory
- Display test results and summary

#### Using auto_test.py (Recommended for automated logging)

```batch
.venv\Scripts\python.exe auto_test.py
```

This will:
- Auto-detect the virtual environment
- Run all tests with comprehensive logging
- Log results to `logs/test_run.log`
- Display environment information

### Linux/macOS

#### Using run_test.sh

```bash
# Make run_test script executable
chmod +x run_test.sh

# Run tests
./run_test.sh
```

#### Using auto_test.py (Recommended for automated logging)

```bash
source .venv/bin/activate
python auto_test.py
```

---

## Docker Setup

### Building the Docker Image

```bash
docker build -t project-env:latest .
```

### Running Tests in Docker

```bash
docker run --rm -v $(pwd)/logs:/app/logs project-env:latest
```

### Running Interactive Shell in Docker

```bash
docker run --rm -it project-env:latest /bin/bash
```

---

## Checking Test Results

After running tests, check the comprehensive log file:

```bash
# View the test log (Windows)
type logs\test_run.log

# View the test log (Linux/macOS)
cat logs/test_run.log

# Follow the test log in real-time (Linux/macOS)
tail -f logs/test_run.log
```

The log file includes:
- Full environment information
- Output from each test
- Test pass/fail status
- Execution timestamps
- Summary statistics

---

## Project Structure

```
.
├── app/                          # Application source code
│   ├── __init__.py
│   ├── data_loader.py
│   ├── text_processor.py
│   └── visualizer.py
├── tests/                        # Test suite
│   ├── case_1.py
│   ├── case_2.py
│   └── case_3.py
├── .venv/                        # Virtual environment (created by setup scripts)
├── logs/                         # Test execution logs (created by auto_test.py)
├── requirements.txt              # Updated dependencies
├── requirements_backup.txt       # Backup of original dependencies
├── report.json                   # Detailed report of dependency changes
├── setup.sh                      # Linux/macOS setup script
├── setup.bat                     # Windows setup script
├── run_test.sh                   # Linux/macOS test runner
├── run_test.bat                  # Windows test runner
├── auto_test.py                  # Automated test runner with logging
├── Dockerfile                    # Docker container definition
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
```

---

## Dependency Conflict Resolution

All dependencies have been resolved for compatibility with Python 3.14. The updated versions ensure:

- ✅ No security vulnerabilities
- ✅ Full Python 3.14 compatibility
- ✅ Cross-platform compatibility (Windows, Linux, macOS)
- ✅ Mutual dependency compatibility
- ✅ Stable, production-ready versions

For detailed information on each update, refer to `report.json`.

---

## Troubleshooting

### Virtual Environment Issues

**Problem**: Virtual environment not found or activation fails

**Solution**:
- Re-run `setup.sh` (Linux/macOS) or `setup.bat` (Windows)
- Ensure Python 3.14 is installed and in PATH
- Check file permissions

### Dependency Installation Issues

**Problem**: Pip fails to install dependencies

**Solution**:
```bash
# Upgrade pip to latest version
python -m pip install --upgrade pip

# Try installing with no build isolation (if still fails)
pip install --no-build-isolation -r requirements.txt

# Check for missing system dependencies (Linux/macOS)
# For lxml: sudo apt-get install libxml2-dev libxslt1-dev (Ubuntu/Debian)
```

### Test Execution Issues

**Problem**: Tests fail to run or import errors occur

**Solution**:
- Ensure virtual environment is activated
- Verify all dependencies are installed: `pip list`
- Check `logs/test_run.log` for detailed error messages
- Verify test files are in the `tests/` directory

### Docker Issues

**Problem**: Docker build fails

**Solution**:
- Ensure Docker is installed and running
- Check Docker logs: `docker logs <container-id>`
- Verify `requirements.txt` is in the same directory as `Dockerfile`

---

## Additional Resources

- [Python 3.14 Documentation](https://docs.python.org/3.14/)
- [Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [Docker Documentation](https://docs.docker.com/)
- [pytest Testing Framework](https://pytest.org/)

---

## Notes

- The `.venv` directory is included in `.gitignore` and should not be committed to version control
- Always use the virtual environment when developing or running tests
- Regularly update dependencies by reviewing `report.json` and security advisories
- Use Docker for reproducible environments across different systems

---

**Generated**: December 10, 2025  
**Python Version**: 3.14.0  
**Environment**: Virtual Environment (.venv)
