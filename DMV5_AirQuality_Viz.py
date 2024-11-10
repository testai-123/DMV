import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("AirQuality.csv")

# Display the first few rows and information about the dataset
print(data.head())
print(data.info())

# Check for missing values
print(data.isnull().sum())

# Remove missing values
data.dropna(inplace=True)
cleaned_data = data.dropna()

# Convert the 'Date' column to datetime format
cleaned_data['Date'] = pd.to_datetime(cleaned_data['Date'])

# Sort the data by 'Date' for time series plotting
cleaned_data.sort_values(by='Date', inplace=True)

# Create the line plot for AQI
plt.figure(figsize=(12, 6))
plt.plot(cleaned_data['Date'], cleaned_data['AQI'], label='AQI', color='blue', linewidth=2)
plt.xlabel('Date')
plt.ylabel('AQI')
plt.title('AQI Trend Over Time (Cleaned Data)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# Define the pollutants to plot
pollutants = ['PM2.5', 'PM10', 'CO']

# Create separate line plots for each pollutant
plt.figure(figsize=(12, 8))
plt.plot(cleaned_data['Date'], cleaned_data['PM2.5'], label=pollutant)
plt.xlabel('Date')
plt.ylabel('Concentration')
plt.title('PM2.5 Trends Over Time (Cleaned Data)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))
plt.plot(cleaned_data['Date'], cleaned_data['PM10'], label=pollutant)
plt.xlabel('Date')
plt.ylabel('Concentration')
plt.title('PM10 Trends Over Time (Cleaned Data)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))
plt.plot(cleaned_data['Date'], cleaned_data['CO'], label=pollutant)
plt.xlabel('Date')
plt.ylabel('Concentration')
plt.title('CO Trends Over Time (Cleaned Data)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()




# Group the data by 'Date' and calculate the mean AQI
aqi_by_date = cleaned_data.groupby('Date')['AQI'].mean().reset_index()

# Create a bar plot to compare AQI values across dates
plt.figure(figsize=(12, 6))
plt.bar(aqi_by_date['Date'], aqi_by_date['AQI'], color='blue', alpha=0.7)
plt.xlabel('Date')
plt.ylabel('Average AQI')
plt.title('Average AQI Across Dates')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

import seaborn as sns

pollutants = ['PM2.5', 'PM10', 'CO']

# Violin plot for PM2.5
plt.figure(figsize=(12, 6))
sns.violinplot(data=cleaned_data, x='AQI', y='PM2.5', palette='Set2')
plt.xlabel('AQI')
plt.ylabel('PM2.5')
plt.title('Violin Plot: Distribution of AQI for PM2.5')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.violinplot(data=cleaned_data, x='AQI', y='PM10', palette='Set2')
plt.xlabel('AQI')
plt.ylabel('PM10')
plt.title('Violin Plot: Distribution of AQI for PM2.5')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.violinplot(data=cleaned_data, x='AQI', y='CO', palette='Set2')
plt.xlabel('AQI')
plt.ylabel('CO')
plt.title('Violin Plot: Distribution of AQI for PM2.5')
plt.tight_layout()
plt.show()

# Similar violin plots for PM10 and CO...

x = df['PM2.5']
y = df['CO']  # Represent 'PM10' using bubble size
aqi_values = df['AQI']
bubble_size = df['PM10'] 

plt.figure(figsize=(12, 8))
plt.scatter(x, y, s = bubble_size, c=aqi_values, cmap='coolwarm', alpha=0.7)
plt.colorbar(label='AQI')
plt.grid(True)
plt.tight_layout()
plt.show()
