# 📊 Advertising Sales Regression Analysis

A comprehensive exploratory data analysis project investigating the relationship between advertising spend across multiple channels (TV, Radio, Newspaper) and product sales.

## 🎯 Project Overview

This project performs detailed exploratory data analysis (EDA) on the **Advertising dataset** to uncover correlations and patterns between advertising investments across different media channels and their direct impact on sales performance. The analysis combines statistical visualization and regression analysis to provide actionable insights into advertising effectiveness.

## 📈 Dataset

The analysis uses the **Advertising dataset** containing 200 observations with the following features:

| Feature | Description | Unit |
|---------|-------------|------|
| **TV** | Advertising spend on television | $1000s |
| **Radio** | Advertising spend on radio | $1000s |
| **Newspaper** | Advertising spend on newspapers | $1000s |
| **Sales** | Product sales | 1000s of units |

## 📁 Project Structure

```
regression/
├── READ.md                    # Project documentation (this file)
├── regression.py              # Main analysis and visualization script
├── Advertising.csv            # Dataset (200 rows, 4 columns)
└── requirements.txt           # Python dependencies
```

## ✨ Key Features

### 📊 Data Exploration
- Load and parse the Advertising dataset
- Generate comprehensive data summaries
- Identify data types, null values, and basic statistics
- Analyze data distribution and uniqueness
- Display first few records and statistical overview

### 🧹 Data Cleaning
- Remove extraneous columns (e.g., unnamed index)
- Prepare clean, analysis-ready dataframe
- Ensure data integrity for downstream analysis

### 📉 Visualizations
The project generates visualization comparisons and regression analysis:

1. **Distribution Plots** (2×2 subplot grid)
   - Sales distribution (red)
   - TV spending distribution (blue)
   - Radio spending distribution (orange)
   - Newspaper spending distribution (purple)

2. **Regression Joint Plots**
   - Newspaper vs Sales with linear regression fit
   - Radio vs Sales with linear regression fit
   - Correlation coefficients and trend lines

## 🛠️ Requirements

- **Python** 3.7+
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computation
- **seaborn** - Statistical visualization
- **matplotlib** - Plotting library

## 📦 Installation & Setup

### Step 1: Install Dependencies
```bash
pip install pandas numpy seaborn matplotlib
```

### Step 2: Prepare Dataset
Ensure Advertising dataset is at:
```
/home/melancholy/Downloads/Advertising.csv
```

### Step 3: Run Analysis
```bash
python regression.py
```

## 🚀 Usage & Output

Running the script performs these steps:

1. **Data Loading & Exploration**
   - Display first 5 rows
   - Show dataset dimensions
   - List null values
   - Print data types and info
   - Calculate unique value counts

2. **Data Cleaning**
   - Remove unnamed index column
   - Create clean DataFrame copy

3. **Generate Visualizations**
   - Display distribution comparison plot
   - Show Newspaper-Sales regression analysis
   - Show Radio-Sales regression analysis

## 📊 Expected Console Output

```
       TV  Radio  Newspaper  Sales
0  230.1   37.8        69.2   22.1
1   44.5   39.3        45.1   10.4
...

Dataset shape: (200, 4)
Columns: ['TV', 'Radio', 'Newspaper', 'Sales']
Null values: 0
```

## 💡 Key Insights

- **TV Advertising**: Strongest correlation with sales, most impactful channel
- **Radio Advertising**: Moderate positive relationship with sales
- **Newspaper Advertising**: Weaker correlation, limited predictive power
- **Sales Distribution**: Appears normally distributed around mean
- **Budget Allocation**: Optimal allocation favors TV over other channels

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| `FileNotFoundError` | Check dataset path at `/home/melancholy/Downloads/Advertising.csv` |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| Plots not displaying | Ensure matplotlib backend configured; may need `%matplotlib inline` in Jupyter |
| Memory issues | Dataset is small; check available RAM |

## 🚀 Future Enhancements

- Build predictive linear regression models with scikit-learn
- Implement multi-channel interaction analysis
- Add statistical metrics (R², RMSE, correlation coefficients)
- Create heatmaps for correlation matrices
- Develop residual analysis and diagnostic plots
- Add hypothesis testing for significance
- Create export functionality for results
- Implement cross-validation for model robustness

## 📚 Code Reference

The `regression.py` script structure:

```python
# 1. Import libraries
# 2. Load data from CSV
# 3. Explore and summarize data
# 4. Remove unnecessary columns
# 5. Create distribution plots (2x2 grid)
# 6. Generate regression joint plots
# 7. Display all visualizations
```

## 📄 Dataset Source

The Advertising dataset is sourced from:
- **Original Source**: "An Introduction to Statistical Learning" textbook
- **Format**: CSV with headers
- **Size**: 200 rows, 4 numeric columns
- **Domain**: Marketing analytics and advertising effectiveness

## 📝 Notes

- All monetary values are in thousands of dollars
- Sales values are in thousands of units
- Dataset contains no missing values
- Suitable for regression analysis and correlation studies

## 🔗 Related Concepts

- **Linear Regression**: Modeling relationships between variables
- **Exploratory Data Analysis (EDA)**: Understanding data characteristics
- **Correlation Analysis**: Measuring variable relationships
- **Data Visualization**: Communicating patterns visually

---

**Last Updated**: 2026-07-17  
**Status**: Active Development  
**License**: Open Source