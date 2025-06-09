import numpy as np
from typing import List, Dict, Any
from .dataset_manager import DatasetManager
from ..models.apartment import Apartment


class PriceAnalysis(DatasetManager):
    def __init__(self, data_path: str = None):
        super().__init__(data_path)
        self.price_stats = {}
    
    def get_summary(self) -> str:
        if not self.apartments:
            return "No apartments loaded for price analysis"
        
        prices = [apt.price for apt in self.apartments if apt.price is not None]
        if not prices:
            return "No valid price data available"
        
        mean_price = np.mean(prices)
        median_price = np.median(prices)
        min_price = np.min(prices)
        max_price = np.max(prices)
        
        return f"""Price Analysis Summary:
        Total Apartments: {len(self.apartments)}
        Valid Price Records: {len(prices)}
        Mean Price: ${mean_price:,.2f}
        Median Price: ${median_price:,.2f}
        Min Price: ${min_price:,.2f}
        Max Price: ${max_price:,.2f}
        Price Range: ${max_price - min_price:,.2f}"""
    
    def compute_price_statistics(self) -> Dict[str, float]:
        if not self.apartments:
            raise ValueError("No apartments loaded")
        
        prices = [apt.price for apt in self.apartments if apt.price is not None]
        if not prices:
            raise ValueError("No valid price data")
        
        self.price_stats = {
            'mean': np.mean(prices),
            'median': np.median(prices),
            'std': np.std(prices),
            'min': np.min(prices),
            'max': np.max(prices),
            'q25': np.percentile(prices, 25),
            'q75': np.percentile(prices, 75),
            'count': len(prices)
        }
        
        return self.price_stats
    
    def get_price_percentiles(self, percentiles: List[float] = [10, 25, 50, 75, 90]) -> Dict[float, float]:
        if not self.apartments:
            raise ValueError("No apartments loaded")
        
        prices = [apt.price for apt in self.apartments if apt.price is not None]
        if not prices:
            raise ValueError("No valid price data")
        
        return {p: np.percentile(prices, p) for p in percentiles}
    
    def filter_by_price_range(self, min_price: float, max_price: float) -> List[Apartment]:
        if not self.apartments:
            return []
        
        return [apt for apt in self.apartments 
                if apt.price is not None and min_price <= apt.price <= max_price]
    
    def get_price_by_bedrooms(self) -> Dict[int, Dict[str, float]]:
        if not self.apartments:
            return {}
        
        bedroom_prices = {}
        
        for apt in self.apartments:
            if apt.price is not None and apt.bedrooms is not None:
                bedrooms = int(apt.bedrooms) if apt.bedrooms == apt.bedrooms else apt.bedrooms
                if bedrooms not in bedroom_prices:
                    bedroom_prices[bedrooms] = []
                bedroom_prices[bedrooms].append(apt.price)
        
        stats = {}
        for bedrooms, prices in bedroom_prices.items():
            if prices:
                stats[bedrooms] = {
                    'mean': np.mean(prices),
                    'median': np.median(prices),
                    'count': len(prices),
                    'min': np.min(prices),
                    'max': np.max(prices)
                }
        
        return stats