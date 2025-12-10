#!/usr/bin/env bash
set -euo pipefail

# Ensure .venv exists and is fresh
if [ -d ".venv" ]; then
  echo "Removing existing .venv to ensure a clean environment"
  rm -rf .venv
fi

python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

mkdir -p logs
echo "Running all test scripts under tests/ and logging to logs/test_run.log"
python auto_test.py 2>&1 | tee logs/test_run.log
