#!/bin/bash

# setup.sh - Environment setup script for Linux/macOS
# This script creates a virtual environment and installs dependencies

set -e  # Exit on error

echo "======================================"
echo "Project Environment Setup"
echo "======================================"

# Check if Python 3.14+ is available
echo "Checking Python version..."
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
REQUIRED_VERSION="3.14"

if ! python3 -c "import sys; sys.exit(0 if sys.version_info >= (3, 14) else 1)" 2>/dev/null; then
    echo "⚠️  Warning: Python 3.14+ is recommended. Found: $PYTHON_VERSION"
fi

# Create virtual environment
echo ""
echo "Creating virtual environment at .venv..."
if [ -d ".venv" ]; then
    echo "Removing existing .venv directory..."
    rm -rf .venv
fi

python3 -m venv .venv

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip, setuptools, and wheel
echo ""
echo "Upgrading pip, setuptools, and wheel..."
python3 -m pip install --upgrade pip setuptools wheel

# Install dependencies
echo ""
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Display environment info
echo ""
echo "======================================"
echo "Environment Setup Complete!"
echo "======================================"
echo ""
echo "Environment Details:"
echo "  Python Version: $(python3 --version)"
echo "  Pip Version: $(pip --version)"
echo "  Virtual Environment: $(pwd)/.venv"
echo ""
echo "To activate the environment, run:"
echo "  source .venv/bin/activate"
echo ""
echo "To run tests, execute:"
echo "  ./run_test.sh"
echo ""
echo "To run automated tests with logging, execute:"
echo "  python auto_test.py"
echo ""
