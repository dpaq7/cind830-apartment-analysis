import pandas as pd
import numpy as np
from typing import List, Optional

# Handle both notebook and package imports
try:
    from ..models.apartment import Apartment
except ImportError:
    from models.apartment import Apartment


class DatasetManager:
    def __init__(self, data_path: Optional[str] = None):
        self.data_path = data_path
        self.raw_data = None
        self.cleaned_data = None
        self.apartments = []
    
    def load_data(self, data_path: Optional[str] = None) -> pd.DataFrame:
        if data_path:
            self.data_path = data_path
        
        if not self.data_path:
            raise ValueError("Data path must be provided")
        
        # Try different encodings to handle various character sets
        encodings_to_try = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252', 'utf-16']
        
        for encoding in encodings_to_try:
            try:
                print(f"Trying to load with {encoding} encoding...")
                self.raw_data = pd.read_csv(self.data_path, sep=';', encoding=encoding)
                print(f"✅ Successfully loaded {len(self.raw_data)} records with {encoding} encoding")
                return self.raw_data
            except UnicodeDecodeError:
                print(f"❌ Failed with {encoding} encoding")
                continue
            except Exception as e:
                print(f"❌ Error with {encoding} encoding: {str(e)}")
                continue
        
        # If all encodings fail, try with error handling
        try:
            print("Trying with error handling (replacing invalid characters)...")
            self.raw_data = pd.read_csv(self.data_path, sep=';', encoding='utf-8', encoding_errors='replace')
            print(f"✅ Successfully loaded {len(self.raw_data)} records with error replacement")
            print("⚠️  Note: Some characters may have been replaced due to encoding issues")
            return self.raw_data
        except Exception as e:
            raise Exception(f"Error loading data with all attempted encodings: {str(e)}")
    
    def clean_data(self) -> pd.DataFrame:
        if self.raw_data is None:
            raise ValueError("No data loaded. Call load_data() first.")
        
        self.cleaned_data = self.raw_data.copy()
        
        # Handle missing values and data type conversions
        numeric_columns = ['price', 'square_feet', 'bathrooms', 'bedrooms', 'latitude', 'longitude']
        
        for col in numeric_columns:
            if col in self.cleaned_data.columns:
                self.cleaned_data[col] = pd.to_numeric(self.cleaned_data[col], errors='coerce')
        
        # Convert categorical variables to consistent string formats
        categorical_columns = ['cityname', 'state', 'category', 'currency', 'pets_allowed']
        for col in categorical_columns:
            if col in self.cleaned_data.columns:
                self.cleaned_data[col] = self.cleaned_data[col].astype(str).str.strip()
        
        # Remove rows with missing critical information
        critical_columns = ['price', 'cityname', 'state']
        self.cleaned_data = self.cleaned_data.dropna(subset=critical_columns)
        
        print(f"Data cleaned. {len(self.cleaned_data)} records remaining after cleaning")
        return self.cleaned_data
    
    def create_apartments(self) -> List[Apartment]:
        if self.cleaned_data is None:
            raise ValueError("No cleaned data available. Call clean_data() first.")
        
        self.apartments = []
        
        for _, row in self.cleaned_data.iterrows():
            apartment = Apartment(
                id=row.get('id'),
                category=row.get('category'),
                title=row.get('title'),
                body=row.get('body'),
                amenities=row.get('amenities'),
                bathrooms=row.get('bathrooms'),
                bedrooms=row.get('bedrooms'),
                currency=row.get('currency'),
                fee=row.get('fee'),
                has_photo=row.get('has_photo'),
                pets_allowed=row.get('pets_allowed'),
                price=row.get('price'),
                price_display=row.get('price_display'),
                price_type=row.get('price_type'),
                square_feet=row.get('square_feet'),
                address=row.get('address'),
                cityname=row.get('cityname'),
                state=row.get('state'),
                latitude=row.get('latitude'),
                longitude=row.get('longitude'),
                source=row.get('source'),
                time=row.get('time')
            )
            self.apartments.append(apartment)
        
        print(f"Created {len(self.apartments)} apartment objects")
        return self.apartments
    
    def get_data_info(self):
        if self.cleaned_data is None:
            print("No data loaded")
            return
        
        print("\nDataset Information:")
        print(f"Shape: {self.cleaned_data.shape}")
        print(f"Columns: {list(self.cleaned_data.columns)}")
        print("\nData Types:")
        print(self.cleaned_data.dtypes)
        print("\nMissing Values:")
        print(self.cleaned_data.isnull().sum())
    
    def get_descriptive_statistics(self):
        if self.cleaned_data is None:
            raise ValueError("No cleaned data available.")
        
        numeric_columns = self.cleaned_data.select_dtypes(include=[np.number]).columns
        stats = {}
        
        for col in numeric_columns:
            if not self.cleaned_data[col].empty:
                stats[col] = {
                    'mean': self.cleaned_data[col].mean(),
                    'median': self.cleaned_data[col].median(),
                    'mode': self.cleaned_data[col].mode().iloc[0] if not self.cleaned_data[col].mode().empty else None,
                    'std': self.cleaned_data[col].std(),
                    'min': self.cleaned_data[col].min(),
                    'max': self.cleaned_data[col].max()
                }
        
        return stats