#!/usr/bin/env bash
set -euo pipefail

# Create a fresh venv in .venv and install pinned requirements
if [ -d ".venv" ]; then
  echo "Removing existing .venv to create a fresh environment"
  rm -rf .venv
fi

python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

echo "Virtual environment created at $(pwd)/.venv"
