import requests
import folium

def get_weather_data(city):
    """Fetch weather data for a given city."""
    API_KEY = "3feca6bf43580bfaa2aa7edb85929cf1"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url).json()
    return response

def clean_data(data):
    """Clean and extract relevant weather information."""
    if data.get('cod') == 200:
        return {
            'temperature': data['main'].get('temp'),
            'humidity': data['main'].get('humidity'),
            'wind_speed': data['wind'].get('speed'),
            'latitude': data['coord'].get('lat'),
            'longitude': data['coord'].get('lon')
        }
    else:
        print(f"Error: {data.get('message')}")
        return None

def create_weather_map(weather_data):
    """Generate a map with weather data points."""
    map_center = [weather_data[0]['latitude'], weather_data[0]['longitude']]
    weather_map = folium.Map(location=map_center, zoom_start=4)

    for data in weather_data:
        popup_content = (
            f"<strong>Temperature:</strong> {data['temperature']} K<br>"
            f"<strong>Humidity:</strong> {data['humidity']}%<br>"
            f"<strong>Wind Speed:</strong> {data['wind_speed']} m/s"
        )
        folium.Marker(
            location=[data['latitude'], data['longitude']],
            popup=folium.Popup(popup_content, parse_html=True)
        ).add_to(weather_map)

    weather_map.save('weather_map.html')
    print('Map saved as "weather_map.html".')

def main():
    """Main function to get weather data and create a map."""
    cities = ["London", "New York", "Tokyo"]
    weather_data = []

    for city in cities:
        data = get_weather_data(city)
        cleaned_data = clean_data(data)
        if cleaned_data:
            weather_data.append(cleaned_data)

    if weather_data:
        create_weather_map(weather_data)

if __name__ == "__main__":
    main()
