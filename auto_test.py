import os
import sys
import subprocess
import pathlib
from datetime import datetime

ROOT = pathlib.Path(__file__).parent.resolve()
VENV_DIR = ROOT / '.venv'
LOG_DIR = ROOT / 'logs'
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / 'test_run.log'

# Detect venv python
if os.name == 'nt':
    venv_python = VENV_DIR / 'Scripts' / 'python.exe'
else:
    venv_python = VENV_DIR / 'bin' / 'python'

if not venv_python.exists():
    print('.venv python not found. Create environment first (setup.sh/setup.bat).')
    sys.exit(2)

# Find tests
tests_dir = ROOT / 'tests'
if not tests_dir.exists():
    print('tests/ directory not found')
    sys.exit(3)

test_files = sorted([p for p in tests_dir.glob('*.py')])

with LOG_FILE.open('a', encoding='utf-8') as f:
    f.write('\n=== Test run: {} ===\n'.format(datetime.utcnow().isoformat()))
    for t in test_files:
        f.write('\n--- Running {} ---\n'.format(t.name))
        env = os.environ.copy()
        stub_path = str(ROOT / 'third_party_stubs')
        env['PYTHONPATH'] = stub_path + os.pathsep + str(ROOT)
        proc = subprocess.run([str(venv_python), str(t)], capture_output=True, text=True, env=env)
        f.write('returncode: {}\n'.format(proc.returncode))
        f.write('stdout:\n')
        f.write(proc.stdout + '\n')
        f.write('stderr:\n')
        f.write(proc.stderr + '\n')

# Append environment info to README.md
readme = ROOT / 'README.md'
py_ver = subprocess.run([str(venv_python), '--version'], capture_output=True, text=True).stdout.strip()
pip_ver = subprocess.run([str(venv_python), '-m', 'pip', '--version'], capture_output=True, text=True).stdout.strip()
with readme.open('a', encoding='utf-8') as f:
    f.write('\nEnvironment name: .venv\n')
    f.write('Absolute path: {}\n'.format(str(VENV_DIR.resolve())))
    f.write('Python: {}\n'.format(py_ver))
    f.write('pip: {}\n'.format(pip_ver))

print('Tests executed. Logs written to {}'.format(str(LOG_FILE)))