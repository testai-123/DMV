'''
Data Loading, Storage and File Formats
Problem Statement: Analyzing Sales Data from Multiple File Formats
Dataset: Sales data in multiple file formats (e.g., CSV, Excel, JSON)
Description: The goal is to load and analyze sales data from different file formats, including
CSV, Excel, and JSON, and perform data cleaning, transformation, and analysis on the
dataset.
Tasks to Perform:
Obtain sales data files in various formats, such as CSV, Excel, and JSON.
1. Load the sales data from each file format into the appropriate data structures or
dataframes.
2. Explore the structure and content of the loaded data, identifying any inconsistencies,
missing values, or data quality issues.
3. Perform data cleaning operations, such as handling missing values, removing
duplicates, or correcting inconsistencies.
4. Convert the data into a unified format, such as a common dataframe or data structure,
to enable seamless analysis.
Data Loading, Storage and File Formats
Problem Statement: Analyzing Sales Data from Multiple File Formats
Dataset: Sales data in multiple file formats (e.g., CSV, Excel, JSON)
Description: The goal is to load and analyze sales data from different file formats, including
CSV, Excel, and JSON, and perform data cleaning, transformation, and analysis on the
dataset.
Tasks to Perform:
Obtain sales data files in various formats, such as CSV, Excel, and JSON.
1. Load the sales data from each file format into the appropriate data structures or
dataframes.
2. Explore the structure and content of the loaded data, identifying any inconsistencies,
missing values, or data quality issues.
3. Perform data cleaning operations, such as handling missing values, removing
duplicates, or correcting inconsistencies.
4. Convert the data into a unified format, such as a common dataframe or data structure,
to enable seamless analysis.

'''


import pandas as pd
import matplotlib.pyplot as plt

# Load the sales data
sales_data = pd.read_csv("sample_7.csv")

# Display the first few rows and basic info
print("Data Preview:")
print(sales_data.head())
print("\nData Information:")
print(sales_data.info())

# Handle missing values and clean data
sales_data['Sales'].fillna(0, inplace=True)
sales_data['Sales'] = sales_data['Sales'].astype(int)
sales_data['Channel'].fillna('Not known', inplace=True)
sales_data['Channel'] = sales_data['Channel'].replace(['offline', 'online'], [0, 1])

# Split 'start_date' into 'Year', 'Month', and 'Day' for additional datasets
df_file1 = pd.read_csv('file1_7.csv')
df_file2 = pd.read_csv('file2_7.csv')
df_file1[['Year', 'Month', 'Day']] = df_file1['start_date'].str.split('-', expand=True)
df_file2[['Year', 'Month', 'Day']] = df_file2['start_date'].str.split('-', expand=True)

# Merge the two datasets
merged_df = pd.concat([df_file1, df_file2], ignore_index=True)
print("\nMerged DataFrame:")
print(merged_df.head())

# Descriptive statistics and analysis
print("\nDescriptive Statistics:")
print(sales_data.describe())

total_sales = sales_data['Sales'].sum()
average_order_value = sales_data['Sales'].mean()
product_category_distribution = sales_data['P Type'].value_counts(normalize=True)

print(f"\nTotal Sales: {total_sales}")
print(f"Average Order Value: {average_order_value:.2f}")
print("\nProduct Category Distribution:\n", product_category_distribution)

grouped_sales = sales_data.groupby('P Type')['Sales'].sum()

# Visualization: Total Sales by Product Type
plt.figure(figsize=(10, 6))
grouped_sales.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Product Type')
plt.xlabel('Product Type')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Pie chart: Product Category Distribution
plt.figure(figsize=(8, 8))
product_category_distribution = sales_data['P Type'].value_counts()
plt.pie(product_category_distribution, labels=product_category_distribution.index, autopct='%1.1f%%', startangle=140)
plt.title('Product Category Distribution')
plt.tight_layout()
plt.show()
