#!/usr/bin/env bash
set -euo pipefail

# Activate venv and run test scripts in tests/ folder, writing output to logs/test_run.log
VENV_DIR=".venv"
LOG_DIR="logs"
LOG_FILE="$LOG_DIR/test_run.log"

if [ ! -d "$LOG_DIR" ]; then
  mkdir -p "$LOG_DIR"
fi

if [ -d "$VENV_DIR" ]; then
  # shellcheck disable=SC1091
  source "$VENV_DIR/bin/activate"
  PY="$VENV_DIR/bin/python"
else
  PY="python"
fi

# Ensure tests can import the local package: add project root to PYTHONPATH
export PYTHONPATH="$(pwd)${PYTHONPATH:+:$PYTHONPATH}"

echo "=== Test run started: $(date -u) ===" | tee -a "$LOG_FILE"
for f in tests/*.py; do
  echo "--- Running $f ---" | tee -a "$LOG_FILE"
  "$PY" "$f" 2>&1 | tee -a "$LOG_FILE"
done

echo "=== Test run finished: $(date -u) ===" | tee -a "$LOG_FILE"