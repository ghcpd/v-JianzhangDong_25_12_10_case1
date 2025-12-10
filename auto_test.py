#!/usr/bin/env python3
"""
auto_test.py - Automated test runner with environment detection

This script:
1. Detects the virtual environment automatically
2. Runs all test scripts in the tests/ directory
3. Logs all results to logs/test_run.log
4. Provides a summary of test results
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime

# Add project root to Python path to enable imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def create_logs_directory():
    """Create logs directory if it doesn't exist."""
    logs_dir = Path("logs")
    if not logs_dir.exists():
        logs_dir.mkdir(exist_ok=True)
        print(f"Created logs directory: {logs_dir}")
    return logs_dir


def get_environment_info():
    """Get Python environment information."""
    env_info = {
        "python_version": sys.version,
        "python_executable": sys.executable,
        "virtual_env": os.environ.get("VIRTUAL_ENV", "Not detected"),
        "pip_version": subprocess.check_output([sys.executable, "-m", "pip", "--version"]).decode().strip(),
        "timestamp": datetime.now().isoformat(),
        "working_directory": os.getcwd(),
    }
    return env_info


def run_tests(test_dir="tests", log_file="logs/test_run.log"):
    """
    Run all test files in the specified directory.
    
    Args:
        test_dir: Directory containing test files
        log_file: Path to log file
        
    Returns:
        Dictionary with test results
    """
    # Ensure logs directory exists
    create_logs_directory()
    
    # Get environment info
    env_info = get_environment_info()
    
    # Initialize results
    results = {
        "environment": env_info,
        "test_results": [],
        "summary": {
            "total": 0,
            "passed": 0,
            "failed": 0,
            "errors": 0
        }
    }
    
    # Log file setup
    with open(log_file, "w") as log:
        # Write header
        log.write("=" * 70 + "\n")
        log.write("Test Execution Report\n")
        log.write("=" * 70 + "\n\n")
        
        # Write environment info
        log.write("ENVIRONMENT INFORMATION\n")
        log.write("-" * 70 + "\n")
        log.write(f"Python Version: {env_info['python_version']}\n")
        log.write(f"Python Executable: {env_info['python_executable']}\n")
        log.write(f"Virtual Environment: {env_info['virtual_env']}\n")
        log.write(f"Pip Version: {env_info['pip_version']}\n")
        log.write(f"Working Directory: {env_info['working_directory']}\n")
        log.write(f"Timestamp: {env_info['timestamp']}\n\n")
        
        # Verify test directory exists
        test_path = Path(test_dir)
        if not test_path.exists():
            error_msg = f"Error: Test directory '{test_dir}' not found"
            log.write(f"{error_msg}\n")
            print(f"❌ {error_msg}")
            return results
        
        # Write test results header
        log.write("TEST RESULTS\n")
        log.write("-" * 70 + "\n\n")
        
        # Get all test files
        test_files = sorted(test_path.glob("*.py"))
        
        if not test_files:
            warning_msg = f"No Python test files found in '{test_dir}'"
            log.write(f"{warning_msg}\n")
            print(f"⚠️  {warning_msg}")
            return results
        
        # Run each test file
        for test_file in test_files:
            test_name = test_file.name
            results["summary"]["total"] += 1
            
            print(f"Running {test_name}...", end=" ")
            log.write(f"\nTest: {test_name}\n")
            log.write("-" * 70 + "\n")
            
            try:
                # Run the test file with project root in PYTHONPATH
                env = os.environ.copy()
                env['PYTHONPATH'] = os.path.dirname(os.path.abspath(__file__))
                
                result = subprocess.run(
                    [sys.executable, str(test_file)],
                    capture_output=True,
                    text=True,
                    timeout=30,
                    env=env,
                    cwd=os.path.dirname(os.path.abspath(__file__))
                )
                
                # Log output
                if result.stdout:
                    log.write("STDOUT:\n")
                    log.write(result.stdout + "\n")
                
                if result.stderr:
                    log.write("STDERR:\n")
                    log.write(result.stderr + "\n")
                
                # Check result
                if result.returncode == 0:
                    status = "PASSED"
                    print("✓")
                    results["summary"]["passed"] += 1
                    results["test_results"].append({
                        "test": test_name,
                        "status": "passed",
                        "return_code": result.returncode
                    })
                    log.write("Status: PASSED\n")
                else:
                    status = "FAILED"
                    print("✗")
                    results["summary"]["failed"] += 1
                    results["test_results"].append({
                        "test": test_name,
                        "status": "failed",
                        "return_code": result.returncode
                    })
                    log.write(f"Status: FAILED (return code: {result.returncode})\n")
                
                log.write("\n")
                
            except subprocess.TimeoutExpired:
                status = "TIMEOUT"
                print("⏱")
                results["summary"]["errors"] += 1
                results["test_results"].append({
                    "test": test_name,
                    "status": "timeout",
                    "error": "Test execution timed out"
                })
                log.write("Status: TIMEOUT\n")
                log.write("Error: Test execution timed out (30 seconds)\n\n")
                
            except Exception as e:
                status = "ERROR"
                print("❌")
                results["summary"]["errors"] += 1
                results["test_results"].append({
                    "test": test_name,
                    "status": "error",
                    "error": str(e)
                })
                log.write("Status: ERROR\n")
                log.write(f"Error: {str(e)}\n\n")
        
        # Write summary
        log.write("\n" + "=" * 70 + "\n")
        log.write("TEST SUMMARY\n")
        log.write("=" * 70 + "\n")
        log.write(f"Total Tests: {results['summary']['total']}\n")
        log.write(f"Passed: {results['summary']['passed']}\n")
        log.write(f"Failed: {results['summary']['failed']}\n")
        log.write(f"Errors: {results['summary']['errors']}\n")
        log.write(f"\nTimestamp: {datetime.now().isoformat()}\n")
        log.write("=" * 70 + "\n")
    
    return results


def print_summary(results):
    """Print a nice summary of test results."""
    print("\n" + "=" * 70)
    print("TEST EXECUTION SUMMARY")
    print("=" * 70)
    print(f"Total Tests: {results['summary']['total']}")
    print(f"Passed: {results['summary']['passed']}")
    print(f"Failed: {results['summary']['failed']}")
    print(f"Errors: {results['summary']['errors']}")
    print("\nEnvironment:")
    print(f"  Python: {results['environment']['python_version'].split()[0]}")
    print(f"  Executable: {results['environment']['python_executable']}")
    print(f"  Virtual Env: {results['environment']['virtual_env']}")
    print("\nLog file: logs/test_run.log")
    print("=" * 70 + "\n")


def main():
    """Main entry point."""
    print("=" * 70)
    print("Automated Test Runner")
    print("=" * 70)
    print()
    
    # Run tests
    results = run_tests(test_dir="tests", log_file="logs/test_run.log")
    
    # Print summary
    print_summary(results)
    
    # Return appropriate exit code
    if results["summary"]["failed"] > 0 or results["summary"]["errors"] > 0:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
