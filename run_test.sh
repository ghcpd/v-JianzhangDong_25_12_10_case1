#!/bin/bash

# run_test.sh - Test runner script for Linux/macOS
# This script runs all test files in the tests/ directory

set -e

echo "======================================"
echo "Running Tests (Linux/macOS)"
echo "======================================"
echo ""

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Error: Virtual environment not found at .venv"
    echo "Please run setup.sh first to create the environment."
    exit 1
fi

# Activate virtual environment
source .venv/bin/activate

echo "Environment Information:"
echo "  Python: $(python --version)"
echo "  Pip: $(pip --version)"
echo "  Virtual Environment: $(pwd)/.venv"
echo ""

# Create logs directory if it doesn't exist
mkdir -p logs

# Run tests
echo "Running test suite..."
echo ""

TEST_DIR="tests"
FAILED=0
PASSED=0

if [ ! -d "$TEST_DIR" ]; then
    echo "Error: Tests directory not found at $TEST_DIR"
    exit 1
fi

# Run each test file
for test_file in "$TEST_DIR"/*.py; do
    if [ -f "$test_file" ]; then
        test_name=$(basename "$test_file")
        echo "Running $test_name..."
        # Set PYTHONPATH to current directory
        PYTHONPATH="$(pwd)" python "$test_file"
        if [ $? -eq 0 ]; then
            echo "✓ $test_name passed"
            ((PASSED++))
        else
            echo "✗ $test_name failed"
            ((FAILED++))
        fi
        echo ""
    fi
done

echo "======================================"
echo "Test Summary"
echo "======================================"
echo "Passed: $PASSED"
echo "Failed: $FAILED"
echo ""

if [ $FAILED -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed. Check output above for details."
    exit 1
fi
