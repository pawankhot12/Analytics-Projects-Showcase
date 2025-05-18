#  Laptop Price Analysis

## Overview
This project explores, analyzes, and predicts laptop prices using a real-world dataset. The workflow covers data cleaning, exploratory data analysis (EDA), feature engineering, regression modeling, and insightful visualizations. The goal is to understand the key factors influencing laptop prices and build a predictive model to estimate prices based on laptop specifications.

---

## Project Structure

- `data_cleaning.ipynb` / `data_cleaning.py` — Data cleaning and preprocessing scripts
- `laptop_price_eda.ipynb` — Exploratory Data Analysis (EDA) notebook with visualizations and insights
- `laptop_price_regression.ipynb` — Regression modeling and evaluation
- `laptop_prices.csv` — Raw dataset
- `laptop_prices_cleaned.csv` — Cleaned dataset
- `requirements.txt` — Python dependencies

---

## Key Features

- **Data Cleaning:** Handles duplicates and missing values for reliable analysis.
- **EDA:** Visualizes distributions, relationships, and correlations using pie charts, histograms, boxplots, scatter plots, and heatmaps.
- **Feature Engineering:** Encodes categorical variables and creates new features for modeling.
- **Modeling:** Implements Linear Regression and optionally tree-based models (Random Forest, XGBoost).
- **Evaluation:** Assesses models using MAE, RMSE, R², and visualizes actual vs. predicted prices and residuals.
- **Insights:** Summarizes findings and provides actionable recommendations.

---

## Usage

1. **Clone the repository**
   ```bash
   git clone <https://github.com/pawankhot12/Analytics-Projects-Showcase.git>
   cd Laptop-Price-Analysis
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the notebooks**
   - Open `data_cleaning.ipynb` and run all cells to clean the data.
   - Open `laptop_price_eda.ipynb` for EDA and insights.
   - Open `laptop_price_regression.ipynb` for modeling and predictions.

---

## Results & Insights

- **Most laptops are Windows-based; Apple laptops are generally more expensive.**
- **RAM and CPU brand are strong predictors of price.**
- **The regression model achieves a reasonable RMSE and R², indicating good predictive performance.**
- **Visualizations reveal outliers and trends, guiding further feature engineering and model improvement.**

---

## Next Steps

- Experiment with advanced models (Random Forest, XGBoost)
- Perform hyperparameter tuning and cross-validation
- Deploy a simple web app (e.g., Streamlit) for interactive price prediction

---

## Project Theme & Idea

The project aims to **demystify laptop pricing** by analyzing the impact of specifications (brand, RAM, CPU, storage, etc.) on price. By combining data science techniques and clear visual storytelling, it empowers both buyers and sellers to make informed decisions in the laptop market.

---

## Author

**Pawan Khot**

---

*For questions or collaboration, please contact: pawan.khot1272004@gmail.com
