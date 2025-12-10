#!/usr/bin/env bash
set -e

# Ensure .venv exists
if [ ! -d ".venv" ]; then
  echo ".venv not found — run setup.sh first"
  exit 1
fi

. .venv/bin/activate
python auto_test.py