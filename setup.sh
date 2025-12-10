#!/usr/bin/env bash
set -e

# Create and activate venv
if [ -d ".venv" ]; then
  echo "Removing existing .venv"
  rm -rf .venv
fi
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

echo "Environment set up in .venv/"