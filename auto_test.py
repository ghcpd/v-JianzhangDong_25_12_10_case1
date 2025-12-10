#!/usr/bin/env python3
import sys
import subprocess
import glob
import os
from pathlib import Path
from datetime import datetime

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "test_run.log"
TEST_DIR = Path("tests")


def run_test_file(python_exe: str, test_path: Path):
    start = datetime.utcnow()
    env = os.environ.copy()
    # Ensure the repository root is on PYTHONPATH so tests can import the local app package
    env["PYTHONPATH"] = str(Path.cwd())
    proc = subprocess.run([python_exe, str(test_path)], capture_output=True, text=True, env=env)
    end = datetime.utcnow()
    return {
        "test": str(test_path),
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "start": start.isoformat() + "Z",
        "end": end.isoformat() + "Z",
    }


def append_env_info(readme_path: Path):
    try:
        py = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
        pip = subprocess.run([sys.executable, "-m", "pip", "--version"], capture_output=True, text=True)
        abs_path = str(Path(sys.executable).parent)
        env_name = ".venv" if ".venv" in str(sys.prefix) or (Path(".venv").exists() and Path(".venv").samefile(Path(sys.prefix))) else Path(sys.prefix).name
    except Exception:
        py = pip = None
        abs_path = str(Path(sys.executable).parent)
        env_name = Path(sys.prefix).name

    with open(readme_path, "a", encoding="utf-8") as f:
        f.write("\n\n## Environment info appended by auto_test.py\n")
        f.write(f"Environment name: {env_name}\n")
        f.write(f"Environment path: {abs_path}\n")
        if py:
            f.write(f"Python: {py.stdout.strip()}\n")
        if pip:
            f.write(f"pip: {pip.stdout.strip()}\n")


def main():
    python_exe = sys.executable
    test_files = sorted(TEST_DIR.glob("*.py"))
    results = []

    with open(LOG_FILE, "a", encoding="utf-8") as logf:
        logf.write(f"\n=== Test run: {datetime.utcnow().isoformat()}Z ===\n")
        if not test_files:
            logf.write("No test files found in tests/\n")
            print("No test files found in tests/")
            return 0

        for t in test_files:
            logf.write(f"Running {t}\n")
            res = run_test_file(python_exe, t)
            results.append(res)
            logf.write(f"Start: {res['start']}\n")
            logf.write(f"End:   {res['end']}\n")
            logf.write(f"Return code: {res['returncode']}\n")
            if res["stdout"]:
                logf.write("--- STDOUT ---\n")
                logf.write(res["stdout"] + "\n")
            if res["stderr"]:
                logf.write("--- STDERR ---\n")
                logf.write(res["stderr"] + "\n")
            logf.write("\n")

    # Append environment info to README.md
    readme_path = Path("README.md")
    if not readme_path.exists():
        readme_path.write_text("# Project tests and environment\n")
    append_env_info(readme_path)

    # Print summary
    failed = [r for r in results if r["returncode"] != 0]
    print(f"Ran {len(results)} tests, {len(failed)} failed. Log written to {LOG_FILE}")
    return 0 if len(failed) == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
