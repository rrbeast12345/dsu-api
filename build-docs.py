#!/usr/bin/env python3
"""
Build script for Docusaurus documentation
This script builds the documentation and copies it to the backend directory
"""

import os
import subprocess
import shutil
import sys

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

def build_documentation():
    """Build the Docusaurus documentation"""
    print("Building Docusaurus documentation...")
    
    # Check if my-website directory exists
    if not os.path.exists("my-website"):
        print("Error: my-website directory not found")
        return False
    
    # Change to my-website directory
    os.chdir("my-website")
    
    # Install dependencies if node_modules doesn't exist
    if not os.path.exists("node_modules"):
        print("Installing dependencies...")
        if not run_command("npm install"):
            return False
    
    # Build the documentation
    print("Building documentation...")
    if not run_command("npm run build"):
        return False
    
    # Go back to root directory
    os.chdir("..")
    
    # Check if build was successful
    build_path = "my-website/build"
    if not os.path.exists(build_path):
        print("Error: Build failed - build directory not found")
        return False
    
    print(f"Documentation built successfully at {build_path}")
    return True

def copy_docs_to_backend():
    """Copy built documentation to backend directory for deployment"""
    print("Copying documentation to backend...")
    
    source = "my-website/build"
    destination = "backend/docs"
    
    # Remove existing docs directory if it exists
    if os.path.exists(destination):
        shutil.rmtree(destination)
    
    # Copy the build directory
    try:
        shutil.copytree(source, destination)
        print(f"Documentation copied to {destination}")
        return True
    except Exception as e:
        print(f"Error copying documentation: {e}")
        return False

def main():
    """Main function"""
    print("DSU API Documentation Builder")
    print("=" * 40)
    
    # Build documentation
    if not build_documentation():
        print("Failed to build documentation")
        sys.exit(1)
    
    # Copy to backend
    if not copy_docs_to_backend():
        print("Failed to copy documentation to backend")
        sys.exit(1)
    
    print("Documentation build and copy completed successfully!")
    print("The documentation will be available at /docs when the FastAPI server starts")

if __name__ == "__main__":
    main() 