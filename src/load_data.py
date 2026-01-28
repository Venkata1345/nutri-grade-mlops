# src/load_data.py
import pandas as pd
import os

def load_data():
    # URL to the raw CSV on GitHub
    url = "https://raw.githubusercontent.com/Enjia/Nutrition-Facts-for-McDonald-s-Menu/master/menu.csv"
    
    print(f"⬇️  Downloading data from {url}...")
    df = pd.read_csv(url)
    
    # Basic cleaning: Select only relevant columns for our regression task
    # We want to predict 'Calories' using the other metrics
    features = ['Item', 'Calories', 'Total Fat', 'Carbohydrates', 'Protein', 'Sugars']
    df = df[features]
    
    # Rename columns to be Python-friendly (lowercase, no spaces)
    df.columns = ['item', 'calories', 'total_fat', 'carbs', 'protein', 'sugar']
    
    # Ensure data folder exists
    os.makedirs('data', exist_ok=True)
    
    # Save locally
    output_path = 'data/menu.csv'
    df.to_csv(output_path, index=False)
    print(f"✅ Data saved to {output_path} ({len(df)} rows)")

if __name__ == "__main__":
    load_data()