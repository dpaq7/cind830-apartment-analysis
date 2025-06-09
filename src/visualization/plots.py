import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from typing import List, Dict, Any, Optional, Tuple
from ..models.apartment import Apartment


class ApartmentVisualizer:
    
    def __init__(self, style: str = 'whitegrid'):
        """Initialize the visualizer with a plotting style."""
        sns.set_style(style)
        plt.rcParams['figure.figsize'] = (10, 6)
        plt.rcParams['font.size'] = 10
    
    def plot_price_histogram(self, apartments: List[Apartment], 
                           bins: int = 50, 
                           title: str = "Distribution of Apartment Prices",
                           save_path: Optional[str] = None) -> plt.Figure:
        """
        Create a histogram of apartment prices.
        
        Args:
            apartments: List of apartment objects
            bins: Number of histogram bins
            title: Plot title
            save_path: Optional path to save the plot
            
        Returns:
            Matplotlib figure object
        """
        prices = [apt.price for apt in apartments if apt.price is not None]
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        ax.hist(prices, bins=bins, alpha=0.7, color='skyblue', edgecolor='black')
        ax.set_xlabel('Price ($)')
        ax.set_ylabel('Frequency')
        ax.set_title(title)
        ax.grid(True, alpha=0.3)
        
        # Add statistics text
        mean_price = np.mean(prices)
        median_price = np.median(prices)
        ax.axvline(mean_price, color='red', linestyle='--', label=f'Mean: ${mean_price:,.0f}')
        ax.axvline(median_price, color='green', linestyle='--', label=f'Median: ${median_price:,.0f}')
        ax.legend()
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        return fig
    
    def plot_price_vs_sqft_scatter(self, apartments: List[Apartment],
                                  title: str = "Square Feet vs. Price Scatter Plot",
                                  save_path: Optional[str] = None) -> plt.Figure:
        """
        Create a scatter plot of square feet vs price.
        
        Args:
            apartments: List of apartment objects
            title: Plot title
            save_path: Optional path to save the plot
            
        Returns:
            Matplotlib figure object
        """
        # Filter apartments with both price and square feet data
        valid_data = [(apt.square_feet, apt.price) for apt in apartments 
                     if apt.square_feet is not None and apt.price is not None]
        
        if not valid_data:
            raise ValueError("No apartments with both square feet and price data")
        
        sqft, prices = zip(*valid_data)
        
        fig, ax = plt.subplots(figsize=(12, 8))
        
        scatter = ax.scatter(sqft, prices, alpha=0.6, c='blue', s=20)
        ax.set_xlabel('Square Feet')
        ax.set_ylabel('Price ($)')
        ax.set_title(title)
        ax.grid(True, alpha=0.3)
        
        # Add correlation coefficient
        correlation = np.corrcoef(sqft, prices)[0, 1]
        ax.text(0.05, 0.95, f'Correlation: {correlation:.3f}', 
                transform=ax.transAxes, bbox=dict(boxstyle="round", facecolor='wheat'))
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        return fig
    
    def plot_price_by_bedrooms_bar(self, apartments: List[Apartment],
                                  title: str = "Average Price by Number of Bedrooms",
                                  save_path: Optional[str] = None) -> plt.Figure:
        """
        Create a bar chart of average price grouped by number of bedrooms.
        
        Args:
            apartments: List of apartment objects
            title: Plot title
            save_path: Optional path to save the plot
            
        Returns:
            Matplotlib figure object
        """
        # Group by bedrooms and calculate average price
        bedroom_prices = {}
        for apt in apartments:
            if apt.bedrooms is not None and apt.price is not None:
                bedrooms = int(apt.bedrooms) if apt.bedrooms == apt.bedrooms else apt.bedrooms
                if bedrooms not in bedroom_prices:
                    bedroom_prices[bedrooms] = []
                bedroom_prices[bedrooms].append(apt.price)
        
        # Calculate averages
        bedroom_avg = {bedrooms: np.mean(prices) 
                      for bedrooms, prices in bedroom_prices.items()}
        
        # Sort by number of bedrooms
        sorted_bedrooms = sorted(bedroom_avg.keys())
        avg_prices = [bedroom_avg[br] for br in sorted_bedrooms]
        counts = [len(bedroom_prices[br]) for br in sorted_bedrooms]
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        bars = ax.bar(range(len(sorted_bedrooms)), avg_prices, 
                     color='lightcoral', alpha=0.7, edgecolor='black')
        
        ax.set_xlabel('Number of Bedrooms')
        ax.set_ylabel('Average Price ($)')
        ax.set_title(title)
        ax.set_xticks(range(len(sorted_bedrooms)))
        ax.set_xticklabels([str(br) for br in sorted_bedrooms])
        ax.grid(True, alpha=0.3, axis='y')
        
        # Add value labels on bars
        for i, (bar, count) in enumerate(zip(bars, counts)):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                   f'${height:,.0f}\n(n={count})',
                   ha='center', va='bottom', fontsize=9)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        return fig
    
    def plot_correlation_heatmap(self, apartments: List[Apartment],
                               title: str = "Correlation Matrix of Numerical Features",
                               save_path: Optional[str] = None) -> plt.Figure:
        """
        Create a heatmap of correlations among numerical features.
        
        Args:
            apartments: List of apartment objects
            title: Plot title
            save_path: Optional path to save the plot
            
        Returns:
            Matplotlib figure object
        """
        # Extract numerical data
        data = []
        for apt in apartments:
            row = {
                'price': apt.price,
                'square_feet': apt.square_feet,
                'bathrooms': apt.bathrooms,
                'bedrooms': apt.bedrooms,
                'latitude': apt.latitude,
                'longitude': apt.longitude
            }
            data.append(row)
        
        # Create DataFrame and calculate correlation
        df = pd.DataFrame(data)
        correlation_matrix = df.corr()
        
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Create heatmap
        sns.heatmap(correlation_matrix, 
                   annot=True, 
                   cmap='coolwarm', 
                   center=0,
                   square=True,
                   linewidths=0.5,
                   fmt='.3f',
                   ax=ax)
        
        ax.set_title(title)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        return fig
    
    def create_comprehensive_dashboard(self, apartments: List[Apartment],
                                     save_path: Optional[str] = None) -> plt.Figure:
        """
        Create a comprehensive dashboard with multiple visualizations.
        
        Args:
            apartments: List of apartment objects
            save_path: Optional path to save the plot
            
        Returns:
            Matplotlib figure object
        """
        fig = plt.figure(figsize=(20, 15))
        
        # Price histogram
        ax1 = plt.subplot(2, 3, 1)
        prices = [apt.price for apt in apartments if apt.price is not None]
        plt.hist(prices, bins=50, alpha=0.7, color='skyblue', edgecolor='black')
        plt.xlabel('Price ($)')
        plt.ylabel('Frequency')
        plt.title('Distribution of Apartment Prices')
        plt.grid(True, alpha=0.3)
        
        # Scatter plot
        ax2 = plt.subplot(2, 3, 2)
        valid_data = [(apt.square_feet, apt.price) for apt in apartments 
                     if apt.square_feet is not None and apt.price is not None]
        if valid_data:
            sqft, prices = zip(*valid_data)
            plt.scatter(sqft, prices, alpha=0.6, c='blue', s=10)
            plt.xlabel('Square Feet')
            plt.ylabel('Price ($)')
            plt.title('Square Feet vs. Price')
            plt.grid(True, alpha=0.3)
        
        # Bar chart
        ax3 = plt.subplot(2, 3, 3)
        bedroom_prices = {}
        for apt in apartments:
            if apt.bedrooms is not None and apt.price is not None:
                bedrooms = int(apt.bedrooms) if apt.bedrooms == apt.bedrooms else apt.bedrooms
                if bedrooms not in bedroom_prices:
                    bedroom_prices[bedrooms] = []
                bedroom_prices[bedrooms].append(apt.price)
        
        if bedroom_prices:
            bedroom_avg = {bedrooms: np.mean(prices) 
                          for bedrooms, prices in bedroom_prices.items()}
            sorted_bedrooms = sorted(bedroom_avg.keys())
            avg_prices = [bedroom_avg[br] for br in sorted_bedrooms]
            
            plt.bar(range(len(sorted_bedrooms)), avg_prices, 
                   color='lightcoral', alpha=0.7)
            plt.xlabel('Number of Bedrooms')
            plt.ylabel('Average Price ($)')
            plt.title('Average Price by Bedrooms')
            plt.xticks(range(len(sorted_bedrooms)), [str(br) for br in sorted_bedrooms])
            plt.grid(True, alpha=0.3, axis='y')
        
        # Correlation heatmap
        ax4 = plt.subplot(2, 3, (4, 6))
        data = []
        for apt in apartments:
            row = {
                'price': apt.price,
                'square_feet': apt.square_feet,
                'bathrooms': apt.bathrooms,
                'bedrooms': apt.bedrooms,
                'latitude': apt.latitude,
                'longitude': apt.longitude
            }
            data.append(row)
        
        df = pd.DataFrame(data)
        correlation_matrix = df.corr()
        
        sns.heatmap(correlation_matrix, 
                   annot=True, 
                   cmap='coolwarm', 
                   center=0,
                   square=True,
                   linewidths=0.5,
                   fmt='.3f')
        plt.title('Correlation Matrix of Numerical Features')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        return fig