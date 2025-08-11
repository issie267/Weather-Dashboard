
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

API_KEY = "30ef659613307c4974d4c6c3a036b90c"  # replace with your OpenWeatherMap API key

def get_weather(city):
    # Try geocoding API first to get lat/lon
    geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    geo_response = requests.get(geocode_url)

    if geo_response.status_code == 200 and geo_response.json():
        geo_data = geo_response.json()[0]
        lat, lon = geo_data['lat'], geo_data['lon']

        # One Call API for detailed weather + daily forecast
        onecall_url = (
            f"https://api.openweathermap.org/data/2.5/onecall"
            f"?lat={lat}&lon={lon}&exclude=minutely,hourly,alerts&units=metric&appid={API_KEY}"
        )
        weather_response = requests.get(onecall_url)

        if weather_response.status_code == 200:
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

    # If geocoding failed or One Call failed, fallback to old current weather API
    fallback_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    fallback_response = requests.get(fallback_url)

    if fallback_response.status_code == 200:
        data = fallback_response.json()
        main = data['main']
        weather_desc = data['weather'][0]

        return {
            "temperature": main['temp'],
            "feels_like": main['feels_like'],
            "description": weather_desc['description'],
            "humidity": main['humidity'],
            "wind_speed": data['wind']['speed'],
            "temp_min": main['temp_min'],
            "temp_max": main['temp_max'],
            "sunrise": datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M'),
            "sunset": datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M'),
        }

    # If both fail, return None
    return None

"""
