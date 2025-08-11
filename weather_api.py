"""
import requests
from datetime import datetime

API_KEY = "30ef659613307c4974d4c6c3a036b90c"  # Your actual API key

def get_weather(city):
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    )
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "temp_min": data["main"]["temp_min"],
            "temp_max": data["main"]["temp_max"],
            "sunrise": datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M"),
            "sunset": datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M")
        }
    else:
        return None
"""

import requests
from datetime import datetime

API_KEY = "30ef659613307c4974d4c6c3a036b90c"  # Your OpenWeatherMap API key

def get_weather(city):
    # Add default country code if none given (change 'GB' if you want)
    if "," not in city:
        city_query = f"{city},GB"
    else:
        city_query = city

    # Step 1: Geocode to get latitude and longitude
    geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_query}&limit=1&appid={API_KEY}"
    geo_response = requests.get(geocode_url)
    if geo_response.status_code != 200:
        return None

    geo_data = geo_response.json()
    if not geo_data:
        return None  # City not found

    lat, lon = geo_data[0]['lat'], geo_data[0]['lon']

    # Step 2: Get weather using One Call API
    onecall_url = (
        f"https://api.openweathermap.org/data/2.5/onecall"
        f"?lat={lat}&lon={lon}&exclude=minutely,hourly,alerts"
        f"&units=metric&appid={API_KEY}"
    )
    weather_response = requests.get(onecall_url)
    if weather_response.status_code != 200:
        return None

    weather_data = weather_response.json()
    current = weather_data['current']
    today = weather_data['daily'][0]

    return {
        "temperature": current['temp'],
        "feels_like": current['feels_like'],
        "description": current['weather'][0]['description'],
        "humidity": current['humidity'],
        "wind_speed": current['wind_speed'],
        "temp_min": today['temp']['min'],
        "temp_max": today['temp']['max'],
        "sunrise": datetime.fromtimestamp(current['sunrise']).strftime('%H:%M'),
        "sunset": datetime.fromtimestamp(current['sunset']).strftime('%H:%M'),
    }

