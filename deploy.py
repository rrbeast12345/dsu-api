#!/usr/bin/env python3
"""
Deployment script for DSU API
This script builds the documentation and starts the FastAPI server
"""

import os
import subprocess
import sys
import time

def run_command(command, cwd=None):
    """Run a command and return the result"""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error running command: {command}")
            print(f"Error: {result.stderr}")
            return False
        print(f"Success: {result.stdout}")
        return True
    except Exception as e:
        print(f"Exception running command {command}: {e}")
        return False

def check_dependencies():
    """Check if required dependencies are installed"""
    print("Checking dependencies...")
    
    # Check if Node.js is installed
    if not run_command("node --version"):
        print("Error: Node.js is not installed")
        return False
    
    # Check if npm is installed
    if not run_command("npm --version"):
        print("Error: npm is not installed")
        return False
    
    # Check if Python dependencies are installed
    if not os.path.exists("backend/requirements.txt"):
        print("Error: requirements.txt not found")
        return False
    
    return True

def install_dependencies():
    """Install Python dependencies"""
    print("Installing Python dependencies...")
    return run_command("pip install -r requirements.txt", cwd="backend")

def build_documentation():
    """Build the documentation"""
    print("Building documentation...")
    
    # Check if my-website directory exists
    if not os.path.exists("my-website"):
        print("Error: my-website directory not found")
        return False
    
    # Change to my-website directory
    os.chdir("my-website")
    
    # Install dependencies if node_modules doesn't exist
    if not os.path.exists("node_modules"):
        print("Installing Node.js dependencies...")
        if not run_command("npm install"):
            return False
    
    # Build the documentation
    print("Building documentation...")
    if not run_command("npm run build"):
        return False
    
    # Go back to root directory
    os.chdir("..")
    
    # Copy to backend
    source = "my-website/build"
    destination = "backend/docs"
    
    if os.path.exists(destination):
        import shutil
        shutil.rmtree(destination)
    
    try:
        import shutil
        shutil.copytree(source, destination)
        print(f"Documentation copied to {destination}")
        return True
    except Exception as e:
        print(f"Error copying documentation: {e}")
        return False

def start_server():
    """Start the FastAPI server"""
    print("Starting FastAPI server...")
    print("Documentation will be available at: http://localhost:8000/docs")
    print("API will be available at: http://localhost:8000")
    print("Press Ctrl+C to stop the server")
    
    # Start the server
    os.chdir("backend")
    subprocess.run(["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"])

def main():
    """Main deployment function"""
    print("DSU API Deployment Script")
    print("=" * 40)
    
    # Check dependencies
    if not check_dependencies():
        print("Dependency check failed")
        sys.exit(1)
    
    # Install Python dependencies
    if not install_dependencies():
        print("Failed to install Python dependencies")
        sys.exit(1)
    
    # Build documentation
    if not build_documentation():
        print("Failed to build documentation")
        sys.exit(1)
    
    # Start server
    start_server()

if __name__ == "__main__":
    main() 