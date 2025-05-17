"""
Laptop Price Analysis - Column Cleaning & Feature Engineering
Author: PAWAN KHOT
Date: 2025-05-13
"""

import pandas as pd

# Load cleaned data
df = pd.read_csv("laptop_prices_cleaned.csv")
print(" Loaded cleaned data")

# Show actual column names
print("Original columns:")
print(df.columns.tolist())

# 🔧 Normalize column names (recommended)
df.columns = df.columns.str.strip().str.lower()

# --- Clean 'ram' column only if needed ---
if df['ram'].dtype == 'object':
    df['ram'] = df['ram'].str.replace('gb', '', case=False, regex=False).astype(int)

# --- Clean 'weight' column only if needed ---
if df['weight'].dtype == 'object':
    df['weight'] = df['weight'].str.replace('kg', '', regex=False).astype(float)

# --- Convert storage strings like '256GB' or '1TB' to integers (in GB) ---
def convert_to_int(value):
    if pd.isnull(value):
        return 0
    value = str(value).upper()
    if 'TB' in value:
        return int(float(value.replace('TB', '').strip()) * 1024)
    elif 'GB' in value:
        return int(value.replace('GB', '').strip())
    return 0

#  Apply conversion to normalized column names
if 'primarystorage' in df.columns and 'secondarystorage' in df.columns:
    df['primarystorage'] = df['primarystorage'].apply(convert_to_int)
    df['secondarystorage'] = df['secondarystorage'].apply(convert_to_int)
    df['totalstorage'] = df['primarystorage'] + df['secondarystorage']
else:
    print(" Storage columns missing! Skipping storage conversion...")

# --- Optional: Extract ssd/hdd if needed from a combined column (not used here) ---
# def extract_storage(row):
#     hdd = 0
#     ssd = 0
#     for item in str(row).split('+'):
#         item = item.strip().lower()
#         if 'hdd' in item:
#             hdd = int(item.replace('tb', '000').replace('gb', '').replace('hdd', '').strip())
#         elif 'ssd' in item:
#             ssd = int(item.replace('tb', '000').replace('gb', '').replace('ssd', '').strip())
#     return pd.Series([ssd, hdd])

# --- Ensure price is numeric ---
if 'price' in df.columns:
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df.dropna(subset=['price'], inplace=True)

#  Save final version
df.to_csv("laptop_prices_transformed.csv", index=False)
print(" Transformed dataset saved as laptop_prices_transformed.csv")

#  Preview cleaned data
preview_cols = ['ram', 'weight', 'primarystorage', 'secondarystorage', 'totalstorage', 'price']
existing_preview_cols = [col for col in preview_cols if col in df.columns]
print("\n Sample Data:")
print(df[existing_preview_cols].head())
