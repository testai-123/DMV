import requests

API_KEY = '3feca6bf43580bfaa2aa7edb85929cf1'
CITY = 'Pune'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

params = {
    'q': CITY,
    'appid': API_KEY,
    'units': 'metric'  # Use 'imperial' for Fahrenheit
}

response = requests.get(BASE_URL, params=params)
weather_data = response.json()

print(weather_data)  # Check the response structure

temperature = weather_data['main']['temp']
humidity = weather_data['main']['humidity']
wind_speed = weather_data['wind']['speed']
precipitation = weather_data.get('rain', {}).get('1h', 0)  # 1-hour precipitation

print(f'Temperature: {temperature}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} m/s, Precipitation: {precipitation} mm')

import pandas as pd

# Example DataFrame
data = {
    'temperature': [temperature],
    'humidity': [humidity],
    'wind_speed': [wind_speed],
    'precipitation': [precipitation]
}

df = pd.DataFrame(data)

# Handling missing values
df.fillna(0, inplace=True)

average_temperature = df['temperature'].mean()
max_temperature = df['temperature'].max()
min_temperature = df['temperature'].min()

print(f'Avg: {average_temperature}, Max: {max_temperature}, Min: {min_temperature}')
