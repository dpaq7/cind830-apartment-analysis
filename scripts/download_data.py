#!/usr/bin/env python3
"""
Download script for apartment rental dataset from UCI ML Repository.
Run this script to download the required dataset before running the analysis.

Dataset: Apartment for Rent Classified
Source: UCI Machine Learning Repository
DOI: https://doi.org/10.24432/C5X623
"""

import os
import sys
import zipfile
import requests
from pathlib import Path
import pandas as pd

def download_dataset():
    """Download the apartment rental dataset from UCI ML Repository."""
    
    # UCI ML Repository dataset information
    dataset_info = {
        "name": "Apartment for Rent Classified",
        "doi": "https://doi.org/10.24432/C5X623",
        "uci_id": 555,
        # Using the ucimlrepo package approach
        "package": "ucimlrepo"
    }
    
    # Output file path
    output_file = Path(__file__).parent.parent / "apartments_for_rent_classified_100K.csv"
    
    # Check if file already exists
    if output_file.exists():
        print(f"✅ Dataset already exists at: {output_file}")
        file_size = output_file.stat().st_size / (1024*1024)
        print(f"📊 File size: {file_size:.1f} MB")
        return True
    
    print("📥 Downloading apartment rental dataset from UCI ML Repository...")
    print(f"🔗 DOI: {dataset_info['doi']}")
    print(f"📁 Destination: {output_file}")
    
    # Method 1: Try using ucimlrepo package
    try:
        print("\n🔄 Attempting to download using ucimlrepo package...")
        
        # Check if ucimlrepo is installed
        try:
            from ucimlrepo import fetch_ucirepo
            print("✅ ucimlrepo package found")
        except ImportError:
            print("❌ ucimlrepo package not found. Installing...")
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", "ucimlrepo"])
            from ucimlrepo import fetch_ucirepo
            print("✅ ucimlrepo package installed successfully")
        
        # Fetch dataset
        print(f"📡 Fetching dataset with ID {dataset_info['uci_id']}...")
        apartment_data = fetch_ucirepo(id=dataset_info['uci_id'])
        
        # Extract features and targets
        X = apartment_data.data.features
        y = apartment_data.data.targets if apartment_data.data.targets is not None else None
        
        # Combine if targets exist, otherwise use just features
        if y is not None:
            dataset = pd.concat([X, y], axis=1)
        else:
            dataset = X
        
        # Save to CSV
        dataset.to_csv(output_file, index=False, sep=';')
        print(f"✅ Dataset saved successfully!")
        print(f"📊 Shape: {dataset.shape}")
        print(f"📁 File size: {output_file.stat().st_size / (1024*1024):.1f} MB")
        
        return True
        
    except Exception as e:
        print(f"❌ Error using ucimlrepo: {e}")
        print("🔄 Falling back to manual download instructions...")
        
    # Method 2: Provide manual download instructions
    print("\n" + "="*60)
    print("📋 MANUAL DOWNLOAD INSTRUCTIONS")
    print("="*60)
    print(f"The dataset needs to be downloaded manually from:")
    print(f"🔗 {dataset_info['doi']}")
    print(f"")
    print(f"Steps:")
    print(f"1. 🌐 Visit the UCI ML Repository link above")
    print(f"2. 📥 Download the dataset (CSV or ZIP format)")
    print(f"3. 📁 Extract if needed and rename to: apartments_for_rent_classified_100K.csv")
    print(f"4. 📂 Place the file in the project root directory:")
    print(f"   {output_file.parent}")
    print(f"")
    print(f"Expected file structure:")
    print(f"📄 File: apartments_for_rent_classified_100K.csv")
    print(f"📊 Format: CSV with semicolon (;) separators")
    print(f"📈 Size: ~100,000 rental listings")
    print(f"🏷️  Features: 21 columns including price, location, size, amenities")
    print("="*60)
    
    return False

def verify_dataset():
    """Verify that the downloaded dataset has the expected structure."""
    
    output_file = Path(__file__).parent.parent / "apartments_for_rent_classified_100K.csv"
    
    if not output_file.exists():
        print("❌ Dataset file not found. Please run download first.")
        return False
    
    try:
        # Read first few rows to verify structure
        df = pd.read_csv(output_file, sep=';', nrows=5)
        
        print("✅ Dataset verification successful!")
        print(f"📊 Shape (first 5 rows): {df.shape}")
        print(f"🏷️  Columns: {list(df.columns)}")
        print(f"📝 Sample data:")
        print(df.head(2).to_string(max_cols=5))
        
        return True
        
    except Exception as e:
        print(f"❌ Error reading dataset: {e}")
        print("📝 Please ensure the file is a valid CSV with semicolon separators")
        return False

def main():
    """Main function to download and verify dataset."""
    
    print("🏠 CIND830 Assignment 2 - Apartment Dataset Downloader")
    print("="*50)
    
    # Download dataset
    success = download_dataset()
    
    if success:
        print(f"\n🔍 Verifying dataset structure...")
        verify_dataset()
    
    print(f"\n✨ Setup complete! You can now run the analysis notebook.")
    print(f"📓 Open: notebooks/apartment_analysis.ipynb")

if __name__ == "__main__":
    main()