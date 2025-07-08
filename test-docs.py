#!/usr/bin/env python3
"""
Test script to verify documentation deployment
"""

import os
import subprocess
import sys
import time
import requests

def check_dependencies():
    """Check if required tools are available"""
    print("Checking dependencies...")
    
    # Check Node.js
    try:
        result = subprocess.run(["node", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ Node.js: {result.stdout.strip()}")
        else:
            print("✗ Node.js not found")
            return False
    except FileNotFoundError:
        print("✗ Node.js not found")
        return False
    
    # Check npm
    try:
        result = subprocess.run(["npm", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ npm: {result.stdout.strip()}")
        else:
            print("✗ npm not found")
            return False
    except FileNotFoundError:
        print("✗ npm not found")
        return False
    
    return True

def build_documentation():
    """Build the documentation"""
    print("\nBuilding documentation...")
    
    if not os.path.exists("my-website"):
        print("✗ my-website directory not found")
        return False
    
    # Change to my-website directory
    os.chdir("my-website")
    
    # Install dependencies if needed
    if not os.path.exists("node_modules"):
        print("Installing Node.js dependencies...")
        result = subprocess.run(["npm", "install"], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"✗ Failed to install dependencies: {result.stderr}")
            os.chdir("..")
            return False
    
    # Build documentation
    print("Building documentation...")
    result = subprocess.run(["npm", "run", "build"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"✗ Build failed: {result.stderr}")
        os.chdir("..")
        return False
    
    os.chdir("..")
    
    # Check if build was successful
    if not os.path.exists("my-website/build"):
        print("✗ Build directory not found")
        return False
    
    print("✓ Documentation built successfully")
    return True

def copy_documentation():
    """Copy documentation to backend"""
    print("\nCopying documentation to backend...")
    
    source = "my-website/build"
    destination = "backend/docs"
    
    if not os.path.exists(source):
        print("✗ Build directory not found")
        return False
    
    # Remove existing docs directory
    if os.path.exists(destination):
        import shutil
        shutil.rmtree(destination)
    
    # Copy documentation
    try:
        import shutil
        shutil.copytree(source, destination)
        print("✓ Documentation copied to backend")
        return True
    except Exception as e:
        print(f"✗ Failed to copy documentation: {e}")
        return False

def test_server():
    """Test the FastAPI server with documentation"""
    print("\nTesting server...")
    
    # Check if docs directory exists
    if not os.path.exists("backend/docs"):
        print("✗ Documentation not found in backend")
        return False
    
    # Start server in background
    print("Starting server...")
    server_process = subprocess.Popen(
        ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"],
        cwd="backend",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Wait for server to start
    time.sleep(3)
    
    try:
        # Test root endpoint
        print("Testing root endpoint...")
        response = requests.get("http://localhost:8000/", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Root endpoint: {data.get('message', 'Unknown')}")
            print(f"  Documentation: {data.get('endpoints', {}).get('documentation', 'Unknown')}")
        else:
            print(f"✗ Root endpoint failed: {response.status_code}")
        
        # Test health endpoint
        print("Testing health endpoint...")
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Health endpoint: {data.get('status', 'Unknown')}")
            print(f"  Documentation: {data.get('documentation', 'Unknown')}")
        else:
            print(f"✗ Health endpoint failed: {response.status_code}")
        
        # Test documentation endpoint
        print("Testing documentation endpoint...")
        response = requests.get("http://localhost:8000/docs/", timeout=5)
        if response.status_code == 200:
            print("✓ Documentation endpoint accessible")
        else:
            print(f"✗ Documentation endpoint failed: {response.status_code}")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Server test failed: {e}")
        return False
    
    finally:
        # Stop server
        server_process.terminate()
        server_process.wait()

def main():
    """Main test function"""
    print("DSU API Documentation Test")
    print("=" * 40)
    
    # Check dependencies
    if not check_dependencies():
        print("\n❌ Dependency check failed")
        sys.exit(1)
    
    # Build documentation
    if not build_documentation():
        print("\n❌ Documentation build failed")
        sys.exit(1)
    
    # Copy documentation
    if not copy_documentation():
        print("\n❌ Documentation copy failed")
        sys.exit(1)
    
    # Test server
    if not test_server():
        print("\n❌ Server test failed")
        sys.exit(1)
    
    print("\n✅ All tests passed!")
    print("\nDocumentation is ready for deployment.")
    print("You can now run: python deploy.py")

if __name__ == "__main__":
    main() 