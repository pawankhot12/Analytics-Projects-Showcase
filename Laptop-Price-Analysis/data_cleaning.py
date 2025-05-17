# data_cleaning.py

"""
Laptop Price Analysis - Data Cleaning Script
Author: PAWAN KHOT
Date: 2025-13-05
Description: Loads and cleans the laptop_prices.csv dataset for analysis.
"""

import pandas as pd

# Load the dataset (same folder)
try:
    df = pd.read_csv("laptop_prices.csv", encoding='ISO-8859-1')  # Try UTF-8 first if this fails
    print(" Dataset loaded successfully!")
except Exception as e:
    print(" Failed to load dataset:", e)
    exit()

# Display first few rows
print("\n First 5 rows:")
print(df.head())

# Dataset shape
print(f"\n Dataset contains {df.shape[0]} rows and {df.shape[1]} columns")

# Check and remove duplicates
duplicates = df.duplicated().sum()
print(f"\n Duplicate rows: {duplicates}")
df = df.drop_duplicates()
print(f" Duplicates removed. New shape: {df.shape}")

# Print column names
print("\n Columns:")
print(df.columns.tolist())

# Save cleaned file
df.to_csv("laptop_prices_cleaned.csv", index=False)
print("\n Cleaned dataset saved as: laptop_prices_cleaned.csv")
