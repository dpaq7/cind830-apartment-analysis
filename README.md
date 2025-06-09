# CIND830 Assignment 2: Apartment Rental Data Analysis

A modular Python project for analyzing apartment rental classified data, demonstrating data structures, algorithms, object-oriented programming, and data visualization.

## Project Structure

```
├── src/                          # Source code modules
│   ├── models/                   # Data models
│   │   ├── __init__.py
│   │   └── apartment.py          # Apartment class definition
│   ├── data/                     # Data management modules
│   │   ├── __init__.py
│   │   ├── dataset_manager.py    # Base data management class
│   │   ├── price_analysis.py     # Price analysis (inheritance demo)
│   │   └── location_analysis.py  # Location analysis (inheritance demo)
│   ├── algorithms/               # Custom algorithm implementations
│   │   ├── __init__.py
│   │   ├── search.py            # Linear and binary search
│   │   └── sorting.py           # Bubble sort and insertion sort
│   ├── visualization/            # Plotting and visualization
│   │   ├── __init__.py
│   │   └── plots.py             # Visualization utilities
│   └── utils/                    # Utility functions
│       └── __init__.py
├── notebooks/                    # Jupyter notebooks
│   └── apartment_analysis.ipynb  # Main analysis notebook
├── tests/                        # Unit tests (optional)
├── config/                       # Configuration files
├── apartments_for_rent_classified_100K.csv  # Dataset
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## Features

### 1. Data Structures
- **Data Loading**: CSV parsing and DataFrame operations
- **Data Cleaning**: Missing value handling and type conversions
- **Descriptive Statistics**: Mean, median, mode calculations using NumPy
- **Object Creation**: Converting raw data to structured Apartment objects

### 2. Algorithms
- **Search Algorithms**:
  - Linear search for apartments by price and location
  - Binary search with performance comparison
- **Sorting Algorithms**:
  - Custom bubble sort implementation
  - Custom insertion sort implementation
  - Performance comparison with built-in sorting

### 3. Object-Oriented Programming
- **Encapsulation**: Apartment class with proper attribute management
- **Inheritance**: PriceAnalysis and LocationAnalysis extend DatasetManager
- **Polymorphism**: Overridden methods for specialized behavior
- **Modular Design**: Separation of concerns across multiple classes

### 4. Visualization
- **Histogram**: Price distribution with outlier identification
- **Scatter Plot**: Square feet vs price correlation analysis
- **Bar Chart**: Average price by number of bedrooms
- **Heatmap**: Correlation matrix for numerical features
- **Dashboard**: Comprehensive multi-plot visualization

## Installation

1. Clone or download the project files:
   ```bash
   git clone https://github.com/YOUR_USERNAME/cind830-apartment-analysis.git
   cd cind830-apartment-analysis
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the dataset** using the provided script:
   ```bash
   python scripts/download_data.py
   ```
   
   This script will:
   - Automatically download the dataset from UCI ML Repository
   - Save it as `apartments_for_rent_classified_100K.csv`
   - Verify the dataset structure
   
   **Alternative**: If automatic download fails, the script provides manual download instructions.

## Usage

### Running the Analysis

1. **Ensure dataset is downloaded** (see Installation step 3)

2. Open Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

3. Navigate to `notebooks/apartment_analysis.ipynb`

4. Run all cells to execute the complete analysis

### Using Individual Modules

```python
# Import modules
from src.models.apartment import Apartment
from src.data.dataset_manager import DatasetManager
from src.data.price_analysis import PriceAnalysis
from src.algorithms.search import SearchAlgorithms
from src.visualization.plots import ApartmentVisualizer

# Load and analyze data
data_path = 'apartments_for_rent_classified_100K.csv'
price_analyzer = PriceAnalysis(data_path)
price_analyzer.load_data()
price_analyzer.clean_data()
apartments = price_analyzer.create_apartments()

# Perform analysis
stats = price_analyzer.compute_price_statistics()
denver_apts = SearchAlgorithms.search_by_city(apartments, "Denver")

# Create visualizations
visualizer = ApartmentVisualizer()
fig = visualizer.plot_price_histogram(apartments)
```

## Dataset

The analysis uses the "Apartment for Rent Classified" dataset from the UCI Machine Learning Repository:
- **Size**: ~100,000 rental listings
- **Features**: 21 attributes including price, location, size, amenities
- **Source**: UCI ML Repository (https://doi.org/10.24432/C5X623)

## Key Insights

1. **Price Distribution**: Significant variation with identifiable outliers
2. **Size-Price Correlation**: Strong positive relationship between square footage and price
3. **Bedroom Premium**: Clear price increases with additional bedrooms
4. **Algorithm Performance**: Built-in sorting outperforms custom implementations
5. **Geographic Patterns**: Metropolitan areas dominate the dataset

## Assignment Requirements Met

- ✅ **Data Structures**: Loading, cleaning, and statistical analysis
- ✅ **Algorithms**: Custom search and sorting with performance comparison
- ✅ **OOP**: Classes, inheritance, and polymorphism demonstration
- ✅ **Visualization**: Multiple plot types with proper formatting

## Dependencies

- Python 3.7+
- pandas: Data manipulation and analysis
- numpy: Numerical computing
- matplotlib: Basic plotting
- seaborn: Statistical visualization
- jupyter: Interactive notebook environment

## Author

CIND830 Assignment 2 - Data Science Program