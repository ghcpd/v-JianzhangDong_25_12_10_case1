#!/usr/bin/env bash
set -euo pipefail

# Creates/.recreates .venv and installs packages
VENV_DIR=".venv"
if [ -d "$VENV_DIR" ]; then
  echo "Removing existing $VENV_DIR"
  rm -rf "$VENV_DIR"
fi

python -m venv "$VENV_DIR"
# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

echo "Virtual environment created at $VENV_DIR and requirements installed."