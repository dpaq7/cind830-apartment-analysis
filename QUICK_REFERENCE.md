# Quick Reference - CIND830 Assignment 2

## 🚀 Getting Started
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Download dataset
python scripts/download_data.py

# 3. Run analysis
jupyter notebook notebooks/apartment_analysis.ipynb
```

## 🔧 Common Commands

### Git Setup for GitHub
```bash
# Initialize repository
git init
git add .
git commit -m "Initial commit"

# Connect to GitHub (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/cind830-apartment-analysis.git
git branch -M main
git push -u origin main
```

### Dataset Issues
```bash
# If encoding errors occur:
# The notebook automatically handles this with multiple encoding attempts

# If dataset missing:
python scripts/download_data.py

# Manual download: https://doi.org/10.24432/C5X623
```

## 📂 Key Files

- **`notebooks/apartment_analysis.ipynb`** - Main analysis (works everywhere)
- **`src/models/apartment.py`** - Core Apartment class
- **`src/data/dataset_manager.py`** - Data loading with encoding fixes
- **`scripts/download_data.py`** - Dataset downloader
- **`requirements.txt`** - All dependencies

## 🛠️ Architecture

### Core Classes
- **Apartment**: Data model with encapsulation
- **DatasetManager**: Base data operations
- **PriceAnalysis**: Inheritance example with price-specific methods
- **LocationAnalysis**: Inheritance example with location methods
- **SearchAlgorithms**: Linear and binary search implementations
- **SortingAlgorithms**: Bubble and insertion sort
- **ApartmentVisualizer**: All plotting functions

### Assignment Requirements ✅
- ✅ Data Structures: Loading, cleaning, statistics
- ✅ Algorithms: Custom search/sort with performance comparison
- ✅ OOP: Classes, inheritance, polymorphism
- ✅ Visualization: Histogram, scatter, bar chart, heatmap

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Import errors | Use the single notebook - handles automatically |
| Encoding errors | Built into DatasetManager.load_data() |
| GitHub auth | Use Personal Access Token as password |
| Missing dataset | Run `python scripts/download_data.py` |

## 📊 What the Analysis Shows

1. **Price Distribution**: Significant variation with outliers
2. **Size-Price Correlation**: Positive relationship 
3. **Bedroom Premium**: Clear price increases with bedrooms
4. **Algorithm Performance**: Built-in sorting >> custom implementations
5. **Geographic Patterns**: Major metros dominate dataset

---

💡 **Pro Tip**: The single notebook (`apartment_analysis.ipynb`) handles all environments automatically - no setup needed!