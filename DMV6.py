import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Retail_Sales.csv")

# Display dataset information and the first few rows
print(df.info())
print(df)

# Group sales by region and calculate total sales per region
sales_by_region = df.groupby('Region')['Sales_Amount'].sum().reset_index()
print(sales_by_region)

# Create a pie chart to show sales distribution by region
plt.figure(figsize=(8, 8))
plt.pie(sales_by_region['Sales_Amount'], labels=sales_by_region['Region'], autopct='%1.1f%%', startangle=140)
plt.title('Sales Distribution by Region')
plt.axis('equal')  # Ensure the pie is drawn as a circle
plt.show()

# Sort regions by highest sales
top_performing_regions = sales_by_region.sort_values(by='Sales_Amount', ascending=False)

# Print the top-performing regions
print("Top-performing regions based on highest sales amount:")
print(top_performing_regions)

# Group sales by both region and product category
sales_by_region_category = df.groupby(['Region', 'Product_category'])['Sales_Amount'].sum().reset_index()

# Display the grouped sales data by region and product category
print(sales_by_region_category)

# Plot a stacked bar chart to compare sales by region and product category
ax = sales_by_region_category.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.title('Sales Comparison by Region and Product Category')
plt.legend(title='Product Category', loc='upper right', bbox_to_anchor=(1.15, 1))

# Display the plot
plt.show()
