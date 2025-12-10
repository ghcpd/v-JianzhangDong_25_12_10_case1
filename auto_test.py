#!/usr/bin/env python3
"""
auto_test.py
- Uses the .venv environment if present; otherwise uses system python
- Runs all .py files in tests/ and saves combined output to logs/test_run.log
- Appends environment name, absolute path, Python and pip versions to README.md
"""
import os
import sys
import subprocess
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
# Ensure project root is on sys.path so tests can import local package 'app'
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "test_run.log"
VENV_DIR = ROOT / ".venv"

if VENV_DIR.exists():
    if os.name == 'nt':
        py = VENV_DIR / 'Scripts' / 'python.exe'
        pip = VENV_DIR / 'Scripts' / 'pip.exe'
    else:
        py = VENV_DIR / 'bin' / 'python'
        pip = VENV_DIR / 'bin' / 'pip'
else:
    py = Path(sys.executable)
    pip = shutil.which('pip') or 'pip'

py = str(py)

with open(LOG_FILE, 'a', encoding='utf-8') as log:
    log.write(f"=== Test run started: {__import__('datetime').datetime.utcnow().isoformat()} UTC ===\n")

    tests_dir = ROOT / 'tests'
    for test_file in sorted(tests_dir.glob('*.py')):
        log.write(f"--- Running {test_file.name} ---\n")
        try:
            # Ensure the child process can import local packages by setting PYTHONPATH
            env = os.environ.copy()
            env['PYTHONPATH'] = str(ROOT) + os.pathsep + env.get('PYTHONPATH', '')
            proc = subprocess.run([py, str(test_file)], capture_output=True, text=True, check=False, env=env)
            log.write(proc.stdout)
            if proc.stderr:
                log.write('\n--- STDERR ---\n')
                log.write(proc.stderr)
            log.write('\n')
        except Exception as e:
            log.write(f"Exception while running {test_file.name}: {e}\n")

    log.write(f"=== Test run finished: {__import__('datetime').datetime.utcnow().isoformat()} UTC ===\n")

# Append environment info to README.md
readme = ROOT / 'README.md'
info_lines = []
info_lines.append('\n\n---\nEnvironment information appended by auto_test.py:\n')
info_lines.append(f"Environment path: {ROOT}\n")
try:
    py_ver = subprocess.check_output([py, '--version'], text=True).strip()
except Exception:
    py_ver = 'unknown'
try:
    pip_ver = subprocess.check_output([py, '-m', 'pip', '--version'], text=True).strip()
except Exception:
    pip_ver = 'unknown'
info_lines.append(f"Python: {py_ver}\n")
info_lines.append(f"Pip: {pip_ver}\n")
readme.write_text(readme.read_text(encoding='utf-8') + ''.join(info_lines), encoding='utf-8')

print(f"Tests executed. Logs written to {LOG_FILE}")