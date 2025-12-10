#!/usr/bin/env bash
set -euo pipefail

if [ ! -d ".venv" ]; then
  echo ".venv not found. Run setup.sh first." >&2
  exit 1
fi

source .venv/bin/activate
python -m auto_test
