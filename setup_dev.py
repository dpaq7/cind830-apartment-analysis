#!/usr/bin/env python3
"""
Development setup script for CIND830 Assignment 2.
This script installs the package in development mode for easier imports.
"""

import subprocess
import sys
from pathlib import Path

def setup_development():
    """Install the package in development mode."""
    
    print("🔧 Setting up CIND830 Apartment Analysis for development...")
    
    # Get the current directory (should be project root)
    project_root = Path(__file__).parent
    print(f"📂 Project root: {project_root}")
    
    try:
        # Install in development mode
        print("📦 Installing package in development mode...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-e", "."
        ], cwd=project_root)
        
        print("✅ Package installed successfully!")
        print("📝 You can now import modules directly:")
        print("   from src.models.apartment import Apartment")
        print("   from src.data.dataset_manager import DatasetManager")
        print("")
        print("🚀 Or run the package installation check:")
        
        # Test imports
        print("🧪 Testing imports...")
        
        # Add src to path temporarily for testing
        sys.path.insert(0, str(project_root / 'src'))
        
        try:
            from models.apartment import Apartment
            from data.dataset_manager import DatasetManager
            print("✅ Basic imports working!")
            
            # Test creating objects
            apt = Apartment(id=1, price=1500, cityname="Test City")
            print(f"✅ Apartment object created: {apt}")
            
            print("🎉 Setup complete! You can now run the notebooks.")
            
        except ImportError as e:
            print(f"❌ Import test failed: {e}")
            print("💡 Try running the notebook with the corrected imports.")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing package: {e}")
        print("💡 Try running manually: pip install -e .")

if __name__ == "__main__":
    setup_development()