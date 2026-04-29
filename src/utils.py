import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime
import os

def generate_synthetic_data(filepath, num_rows=1000):
    """Generates realistic synthetic trade data and saves to CSV."""
    np.random.seed(42)
    random.seed(42)
    
    commodities = [
        "Petroleum Products", "Drug Formulations, Biologicals", "Pearl, Precious, Semiconducting Stones", 
        "Iron And Steel", "Telecom Instruments", "Motor Vehicles/Cars", "Gold And Oth Precious Metal Jewelry",
        "Marine Products", "Electric Machinery And Equipme", "Aluminium, Products Of Alumin"
    ]
    
    countries = ["USA", "UAE", "Netherlands", "China", "Singapore", "UK", "Germany", "Bangladesh", "Nepal", "Saudi Arabia"]
    years = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
    
    data = []
    for _ in range(num_rows):
        commodity = random.choices(commodities, weights=[20, 15, 12, 10, 8, 8, 7, 7, 7, 6], k=1)[0]
        country = random.choices(countries, weights=[18, 15, 10, 9, 8, 8, 8, 8, 8, 8], k=1)[0]
        year = random.choice(years)
        
        # Base value with some variation
        base_value = np.random.uniform(10, 500)
        # Apply year growth multiplier (slight dip in 2020, steady growth after)
        if year == 2020:
            growth_mult = 0.8
        elif year > 2020:
            growth_mult = 1.0 + (year - 2020) * 0.1
        else:
            growth_mult = 1.0
        
        value = base_value * growth_mult * (1 if commodity != "Petroleum Products" else 2.5)
        quantity = value * np.random.uniform(0.5, 2.0)
        
        data.append({
            "COMMODITY": commodity,
            "COUNTRY": country,
            "YEAR": year,
            "VALUE": value,
            "QUANTITY": quantity
        })
        
    df = pd.DataFrame(data)
    
    # Introduce anomalies for data cleaning demonstration
    # 1. Duplicates
    df = pd.concat([df, df.sample(20, random_state=42)], ignore_index=True)
    # 2. Missing values
    for col in ["VALUE", "QUANTITY"]:
        df.loc[df.sample(15, random_state=42).index, col] = np.nan
    # 3. Inconsistent categories
    df.loc[df.sample(10, random_state=42).index, "COUNTRY"] = "u.s.a."
    df.loc[df.sample(10, random_state=43).index, "COUNTRY"] = "u.a.e."
    # 4. Negative values
    df.loc[df.sample(5, random_state=44).index, "VALUE"] = -50.0
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)
    return len(df)

def clean_data(df):
    """Cleans data and returns valid dataframe along with logs."""
    initial_count = len(df)
    
    # 1. Remove duplicates
    df_clean = df.drop_duplicates()
    dupe_count = initial_count - len(df_clean)
    
    # 2. Handle missing values
    missing_mask = df_clean[['VALUE', 'QUANTITY']].isnull().any(axis=1)
    missing_count = missing_mask.sum()
    df_clean = df_clean.dropna(subset=['VALUE', 'QUANTITY'])
    
    # 3. Standardize text
    df_clean['COUNTRY'] = df_clean['COUNTRY'].replace({"u.s.a.": "USA", "u.a.e.": "UAE"})
    df_clean['COMMODITY'] = df_clean['COMMODITY'].str.title()
    
    # 4. Validate and fix logic (no negative values)
    negative_mask = (df_clean['VALUE'] < 0) | (df_clean['QUANTITY'] < 0)
    negative_count = negative_mask.sum()
    df_clean = df_clean[~negative_mask]
    
    final_count = len(df_clean)
    
    stats = {
        "initial_count": initial_count,
        "final_count": final_count,
        "dupe_count": dupe_count,
        "missing_count": missing_count,
        "negative_count": negative_count
    }
    return df_clean, stats

def generate_validation_log(log_path, stats):
    """Generates a professional data validation report."""
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    log_content = f"Records before cleaning: {stats['initial_count']}\n"
    log_content += f"Records after cleaning: {stats['final_count']}\n\n"
    log_content += "Validation Steps:\n"
    log_content += "- Removed duplicates\n"
    log_content += "- Handled missing values\n"
    log_content += "- Standardized country names\n"
    log_content += "- Verified numeric fields (no negative values)\n\n"
    log_content += "Result:\n"
    log_content += "Dataset ensured for high integrity and reliability\n"
    
    with open(log_path, "w") as f:
        f.write(log_content)

def plot_top_commodities(df, output_path):
    """Generates a formal bar chart of top commodities."""
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(12, 7))
    
    top_commodities = df.groupby('COMMODITY')['VALUE'].sum().sort_values(ascending=False).head(10)
    
    ax = sns.barplot(x=top_commodities.values, y=top_commodities.index, hue=top_commodities.index, palette="Blues_r", legend=False)
    
    plt.title("Top 10 Export Commodities by Cumulative Value", fontsize=15, fontweight='bold', pad=15)
    plt.xlabel("Total Export Value (Millions USD)", fontsize=12, fontweight='bold')
    plt.ylabel("Commodity Category", fontsize=12, fontweight='bold')
    
    # Format x-axis with commas
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    
    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300)
    plt.close()

def plot_export_trends(df, output_path):
    """Generates a formal line chart of export trends."""
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    
    yearly_trends = df.groupby('YEAR')['VALUE'].sum().reset_index()
    
    ax = sns.lineplot(data=yearly_trends, x='YEAR', y='VALUE', marker='o', markersize=8, linewidth=2.5, color='#1f497d')
    
    plt.title("Year-wise Export Aggregate Growth Trend (2018-2024)", fontsize=15, fontweight='bold', pad=15)
    plt.xlabel("Financial Year", fontsize=12, fontweight='bold')
    plt.ylabel("Total Export Value (Millions USD)", fontsize=12, fontweight='bold')
    plt.xticks(yearly_trends['YEAR'])
    
    # Format y-axis
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    
    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300)
    plt.close()
