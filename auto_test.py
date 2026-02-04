#!/usr/bin/env python3
"""
Simple test runner that executes every python file in the tests/ directory
using the Python interpreter inside .venv (if present), writes results to
logs/test_run.log and appends environment info to README.md.

Designed to be runnable on Windows and POSIX in-place.
"""
import os
import sys
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOGS = HERE / 'logs'
TESTS = HERE / 'tests'
VENV = (HERE / '.venv')

def get_interpreter():
    # prefer interpreter within .venv if available
    if VENV.exists():
        candidate = VENV / ('Scripts' if os.name == 'nt' else 'bin') / ('python.exe' if os.name == 'nt' else 'python')
        if candidate.exists():
            return str(candidate)
    # fallback
    return sys.executable

def get_pip(interpreter):
    # get pip path for the interpreter used
    pipexe = Path(interpreter).parent / ('pip.exe' if os.name == 'nt' else 'pip')
    if pipexe.exists():
        return str(pipexe)
    return f"{interpreter} -m pip"

def write_readme_append(interpreter, pip_path):
    readme = HERE / 'README.md'
    info = (
        f"\n\nEnvironment: .venv\n"
        f"Absolute path: {VENV.resolve()}\n"
        f"Python: {subprocess.check_output([interpreter, '--version'], stderr=subprocess.STDOUT).decode().strip()}\n"
        f"pip: {subprocess.check_output([interpreter, '-m', 'pip', '--version'], stderr=subprocess.STDOUT).decode().strip()}\n"
    )
    # Append information to README.md
    with open(readme, 'a', encoding='utf-8') as f:
        f.write(info)

def run_tests(interpreter, logfile):
    if not TESTS.exists():
        logfile.write('No tests/ directory found.\n')
        return 1

    test_files = sorted([p for p in TESTS.iterdir() if p.suffix == '.py'])
    if not test_files:
        logfile.write('No test scripts found under tests/.\n')
        return 1

    exit_code = 0
    for t in test_files:
        logfile.write(f"\n=== Running {t.name} ===\n")
        cmd = [interpreter, str(t)]
        # ensure tests can import local package(s) by setting PYTHONPATH to project root
        env = os.environ.copy()
        env['PYTHONPATH'] = str(HERE)
        proc = subprocess.run(cmd, capture_output=True, text=True, env=env)
        logfile.write(proc.stdout)
        if proc.stderr:
            logfile.write('\n--- STDERR ---\n')
            logfile.write(proc.stderr)
        logfile.write(f"\nExit status: {proc.returncode}\n")
        if proc.returncode != 0:
            exit_code = proc.returncode
    return exit_code

def main():
    LOGS.mkdir(exist_ok=True)
    log_path = LOGS / 'test_run.log'
    interpreter = get_interpreter()
    pip_path = get_pip(interpreter)

    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(f"Auto test run using interpreter: {interpreter}\n")
        f.write(f"pip command: {pip_path}\n")
        f.write('\n')
        code = run_tests(interpreter, f)

    # Append environment info to README.md (always update)
    try:
        write_readme_append(interpreter, pip_path)
    except Exception as e:
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(f"Failed to update README.md: {e}\n")

    return code

if __name__ == '__main__':
    raise SystemExit(main())
