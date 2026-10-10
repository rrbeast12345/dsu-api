#!/usr/bin/env python3
"""
Documentation build script for Render deployment
"""
import os
import subprocess
import sys

def build_documentation():
    """Build Docusaurus documentation"""
    docusaurus_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'my-website'))
    docusaurus_build_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'my-website', 'build'))
    
    print(f"Building documentation from: {docusaurus_path}")
    
    if not os.path.exists(docusaurus_path):
        print("Docusaurus project not found")
        return False
    
    try:
        # Check if Node.js is available
        try:
            subprocess.run(['node', '--version'], check=True, capture_output=True)
            print("Node.js is available")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Node.js is not available. Cannot build documentation.")
            return False
        
        # Check if npm is available
        try:
            subprocess.run(['npm', '--version'], check=True, capture_output=True)
            print("npm is available")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("npm is not available. Cannot build documentation.")
            return False
        
        # Install dependencies if needed
        node_modules_path = os.path.join(docusaurus_path, 'node_modules')
        if not os.path.exists(node_modules_path):
            print("Installing Docusaurus dependencies...")
            subprocess.run(['npm', 'install'], cwd=docusaurus_path, check=True)
            print("Dependencies installed successfully")
        
        # Build the documentation
        print("Building Docusaurus documentation...")
        subprocess.run(['npm', 'run', 'build'], cwd=docusaurus_path, check=True)
        print("Documentation built successfully")
        
        # Verify build exists
        if os.path.exists(docusaurus_build_path):
            print(f"Documentation build verified at: {docusaurus_build_path}")
            return True
        else:
            print("Build completed but build directory not found")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"Error building documentation: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = build_documentation()
    sys.exit(0 if success else 1) 