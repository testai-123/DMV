import pandas as pd
import matplotlib.pyplot as plt

# Load the sales data from CSV file
sales_data = pd.read_csv("sample_7.csv")
print("CSV Data Preview:")
print(sales_data.head())

# Display basic information from the CSV data
print("\nData Information:")
print(sales_data.info())

# Step 2: Identify Inconsistencies Before Cleaning
# Check for duplicate rows in the CSV data
print("\nDuplicate rows in CSV data:", sales_data.duplicated().sum())

# Check for missing values in the CSV data
print("\nMissing values in CSV data:\n", sales_data.isnull().sum())

# Step 3: Data Cleaning (Handle missing values and duplicates simultaneously)
# Remove duplicates
sales_data.drop_duplicates(inplace=True)

# Fill missing values for 'Sales' and convert to integer
sales_data['Sales'].fillna(0, inplace=True)
sales_data['Sales'] = sales_data['Sales'].astype(int)

# Fill missing values for 'Channel' and convert to numeric (0 = offline, 1 = online)
sales_data['Channel'].fillna('Not known', inplace=True)
sales_data['Channel'] = sales_data['Channel'].replace(['offline', 'online'], [0, 1])

# Step 4: Data Transformation
# Split 'start_date' into separate 'Year', 'Month', and 'Day' columns
sales_data[['Year', 'Month', 'Day']] = sales_data['start_date'].str.split('-', expand=True)

# Additional data merging from other files, if available
df_file1 = pd.read_csv('file1_7.csv')
df_file2 = pd.read_csv('file2_7.csv')
merged_df = pd.concat([df_file1, df_file2], ignore_index=True)
print("\nMerged DataFrame:")
print(merged_df.head())

# Step 5: Descriptive Statistics and Analysis
# Total sales, average order value, product category distribution
total_sales = sales_data['Sales'].sum()
average_order_value = sales_data['Sales'].mean()
product_category_distribution = sales_data['P Type'].value_counts(normalize=True)

print(f"\nTotal Sales: {total_sales}")
print(f"Average Order Value: {average_order_value:.2f}")
print("\nProduct Category Distribution:\n", product_category_distribution)

# Additional Metrics:
# Average sales by channel
average_sales_by_channel = sales_data.groupby('Channel')['Sales'].mean()
print("\nAverage Sales by Channel:\n", average_sales_by_channel)

# Average sales by month
sales_data['Month'] = sales_data['Month'].astype(int)  # Ensure 'Month' is numeric
average_sales_by_month = sales_data.groupby('Month')['Sales'].mean()
print("\nAverage Sales by Month:\n", average_sales_by_month)

# Aggregated sales by product type
grouped_sales = sales_data.groupby('P Type')['Sales'].sum()

# Step 6: Visualizations
# Bar plot: Total Sales by Product Type
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
plt.pie(product_category_distribution, labels=product_category_distribution.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Product Category Distribution')
plt.tight_layout()
plt.show()

# Optional Visualization - Box plot of Sales by Channel
plt.figure(figsize=(10, 6))
sales_data.boxplot(column='Sales', by='Channel', grid=False)
plt.title('Sales Distribution by Channel')
plt.suptitle('')
plt.xlabel('Channel (0: Offline, 1: Online)')
plt.ylabel('Sales')
plt.show()

# Line plot: Average Sales by Month for seasonal trend analysis
plt.figure(figsize=(10, 6))
average_sales_by_month.plot(kind='line', marker='o', color='orange')
plt.title('Average Sales by Month')
plt.xlabel('Month')
plt.ylabel('Average Sales')
plt.grid(True)
plt.tight_layout()
plt.show()
