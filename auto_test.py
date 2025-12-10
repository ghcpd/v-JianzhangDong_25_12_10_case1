#!/usr/bin/env python3

import os
import sys
import subprocess
import logging
from pathlib import Path

def setup_logging():
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    logging.basicConfig(
        filename=log_dir / "test_run.log",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def get_env_info():
    venv_path = Path(".venv").resolve()
    python_exe = venv_path / "Scripts" / "python.exe" if os.name == 'nt' else venv_path / "bin" / "python"
    pip_version = subprocess.check_output([str(python_exe), "-m", "pip", "--version"]).decode().strip()
    python_version = subprocess.check_output([str(python_exe), "--version"]).decode().strip()
    return str(venv_path), str(python_exe), python_version, pip_version

def run_test_script(script_path):
    venv_path, python_exe, python_version, pip_version = get_env_info()
    
    logging.info(f"Running test script: {script_path}")
    try:
        result = subprocess.run([python_exe, "-c", f"import sys; sys.path.insert(0, '.'); exec(open('{script_path}').read())"], 
                                capture_output=True, text=True, timeout=30)
        logging.info("Test output:")
        logging.info(result.stdout)
        if result.stderr:
            logging.error("Test errors:")
            logging.error(result.stderr)
        logging.info(f"Return code: {result.returncode}")
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        logging.error(f"Test {script_path} timed out")
        return False
    except Exception as e:
        logging.error(f"Error running {script_path}: {e}")
        return False

def run_tests():
    venv_path, python_exe, python_version, pip_version = get_env_info()
    
    logging.info(f"Environment: {venv_path}")
    logging.info(f"Python executable: {python_exe}")
    logging.info(f"Python version: {python_version}")
    logging.info(f"Pip version: {pip_version}")
    
    test_scripts = ["tests/case_1.py", "tests/case_2.py", "tests/case_3.py"]
    all_passed = True
    for script in test_scripts:
        if not run_test_script(script):
            all_passed = False
    
    return all_passed

if __name__ == "__main__":
    setup_logging()
    success = run_tests()
    sys.exit(0 if success else 1)