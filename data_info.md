# Dataset Information

## Apartment for Rent Classified Dataset

### Source
- **Repository**: UCI Machine Learning Repository
- **DOI**: https://doi.org/10.24432/C5X623
- **Dataset ID**: 555
- **Citation**: Apartment for Rent Classified [Dataset]. (2019). UCI Machine Learning Repository.

### Overview
This dataset contains approximately 100,000 apartment rental listings from the USA, scraped from classified advertisement websites. It provides comprehensive information about rental properties including pricing, location, amenities, and property characteristics.

### Dataset Characteristics
- **Number of Instances**: ~100,000
- **Number of Features**: 21
- **Feature Types**: Mixed (numerical, categorical, text)
- **Missing Values**: Yes (varies by feature)
- **File Size**: ~50-70 MB
- **Format**: CSV with semicolon (;) separators

### Features Description

| Feature | Type | Description |
|---------|------|-------------|
| `id` | Numerical | Unique identifier for each listing |
| `category` | Categorical | Type of housing (typically "housing/rent/apartment") |
| `title` | Text | Title of the rental listing |
| `body` | Text | Full description/body text of the listing |
| `amenities` | Categorical | Available amenities (may be null) |
| `bathrooms` | Numerical | Number of bathrooms |
| `bedrooms` | Numerical | Number of bedrooms |
| `currency` | Categorical | Currency type (typically "USD") |
| `fee` | Categorical | Information about fees |
| `has_photo` | Categorical | Whether listing includes photos |
| `pets_allowed` | Categorical | Pet policy (Cats, Dogs, None, etc.) |
| `price` | Numerical | Monthly rental price |
| `price_display` | Text | Formatted price string |
| `price_type` | Categorical | Type of pricing (typically "Monthly") |
| `square_feet` | Numerical | Size of apartment in square feet |
| `address` | Text | Street address |
| `cityname` | Categorical | City name |
| `state` | Categorical | US state abbreviation |
| `latitude` | Numerical | Geographic latitude coordinate |
| `longitude` | Numerical | Geographic longitude coordinate |
| `source` | Categorical | Data source/website |
| `time` | Numerical | Unix timestamp of listing |

### Key Statistics (Approximate)
- **Price Range**: $400 - $15,000+ per month
- **Square Feet Range**: 200 - 5,000+ sq ft
- **Bedrooms**: 0-6+ bedrooms
- **Bathrooms**: 0.5-6+ bathrooms
- **Geographic Coverage**: All 50 US states
- **Major Cities**: New York, Los Angeles, Chicago, Houston, Phoenix, etc.

### Data Quality Notes
- Some listings may have missing values for amenities, square footage, or coordinates
- Price data is generally complete and reliable
- Geographic coordinates are available for most listings
- Text fields (title, body) may contain inconsistent formatting

### Potential Use Cases
- Rental price prediction modeling
- Geographic analysis of housing markets
- Amenity impact on pricing
- Market trends analysis
- Location-based recommendations
- Housing affordability studies

### Download Instructions
Use the provided download script to automatically fetch the dataset:
```bash
python scripts/download_data.py
```

This script will attempt to download directly from UCI ML Repository using the `ucimlrepo` package. If automatic download fails, it provides manual download instructions.