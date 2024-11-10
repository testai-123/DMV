import pandas as pd
from scipy import stats

# Load dataset
df = pd.read_csv("C:\\Users\\aksha\\Downloads\\DMV4.csv")

# Clean column names (spaces and special characters removed)
df.columns = df.columns.str.replace(' ', '_').str.replace(r'\W', '', regex=True)

# Example data cleaning display
print(df.head())

# Handle missing values (example: fill missing prices with the median)
df['Price'] = df['Price'].fillna(df['Price'].median())

# Calculating Z-scores for the 'Price' column to detect outliers
df['z_score'] = stats.zscore(df['Price'])

# Define a threshold for outliers (Z-score threshold: 3)
threshold = 3
outliers_mask = (df['z_score'] > threshold) | (df['z_score'] < -threshold)

# Extract and print outliers
outliers = df[outliers_mask]
print(outliers)

# Handle outliers (e.g., replace with median value)
df.loc[outliers.index, 'Price'] = df['Price'].median()

# Final dataset view after cleaning
print(df['Price'])

avg_price_by_neighborhood = df.groupby('Neighborhood')['Price'].mean()
print("Average Sale Price by Neighborhood:")
print(avg_price_by_neighborhood)

# Final dataset after cleaning and transformations
print("Final Dataset after Cleaning and Transformations:")
print(df.head())
