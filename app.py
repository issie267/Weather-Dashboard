"""
import streamlit as st
from weather_api import get_weather

st.set_page_config(page_title="Weather Dashboard",page_icon="🌦️", layout="centered")

st.title("🌤️ Daddy's weather monitoring station")

st.markdown("Get the latest weather updates for any city in the world.")

st.markdown("### 📍 Enter a city to check its weather")

city = st.text_input("Enter a city name: (you may need to add country code eg UK!)")

def weather_icon(description):
    description=description.lower()
    if "cloud" in description:
        return "☁️"
    elif "rain" in description:
        return "🌧️"
    elif "clear" in description:
        return "☀️"
    elif "snow" in description:
        return "🌨️"
    elif "storm" in description:
        return "🌩️"
    else:
        return "🌡️"

if city:
    weather = get_weather(city)
    
    if weather:
        st.subheader(f"Weather in {city.title()} {weather_icon(weather['description'])}")

        
                # Metrics in a row
        col1, col2, col3 = st.columns(3)
        col1.metric("Temp", f"{weather['temperature']}°C", f"Feels {weather['feels_like']}°C")
        col2.metric("Min Temp", f"{weather['temp_min']}°C")
        col3.metric("Max Temp", f"{weather['temp_max']}°C")

        st.write(f"**Weather:** {weather['description'].title()}")
        st.write(f"💧 **Humidity:** {weather['humidity']}%")
        st.write(f"🌬️ **Wind Speed:** {weather['wind_speed']} m/s")
        st.write(f"🌅 **Sunrise:** {weather['sunrise']}")
        st.write(f"🌇 **Sunset:** {weather['sunset']}")
    else:
        st.error("City not found. Please try again.")
"""
import streamlit as st
from weather_api import get_weather_by_coords, get_weather

st.set_page_config(page_title="Weather Dashboard", page_icon="🌦️", layout="centered")

st.title("🌤️ Daddy's weather monitoring station")
st.markdown("Get the latest weather updates for any city in the world.")

# Preset places with lat/lon
places = {
    "": (None, None),  # blank option
    "Cranbrook, UK": (51.0850, 0.3520),
    "Loughborough, UK": (52.7723, -1.2051),
    "Fuengirola, Spain": (36.5399, -4.6248),
    "Bath, UK": (51.3758, -2.3599),
    "Singapore": (1.3521, 103.8198),
    "Macclesfield, UK": (53.2607, -2.1160),
}

def weather_icon(description):
    description = description.lower()
    if "cloud" in description:
        return "☁️"
    elif "rain" in description:
        return "🌧️"
    elif "clear" in description:
        return "☀️"
    elif "snow" in description:
        return "🌨️"
    elif "storm" in description:
        return "🌩️"
    else:
        return "🌡️"

st.markdown("### 📍 Select a place to see highs and lows daily:")
place = st.selectbox("Choose a preset location:", list(places.keys()))

st.markdown("### Or enter any city name (no highs/lows for typed cities):")
city = st.text_input("Enter a city name (add country code if needed):")

if place and place != "":
    lat, lon = places[place]
    weather = get_weather_by_coords(lat, lon)
    if weather:
        st.subheader(f"Weather in {place} {weather_icon(weather['description'])}")
        col1, col2, col3 = st.columns(3)
        col1.metric("Temp", f"{weather['temperature']}°C", f"Feels like {weather['feels_like']}°C")
        col2.metric("Min Temp", f"{weather['temp_min']}°C")
        col3.metric("Max Temp", f"{weather['temp_max']}°C")
        st.write(f"**Weather:** {weather['description'].title()}")
        st.write(f"💧 Humidity: {weather['humidity']}%")
        st.write(f"🌬️ Wind Speed: {weather['wind_speed']} m/s")
        st.write(f"🌅 Sunrise: {weather['sunrise']}")
        st.write(f"🌇 Sunset: {weather['sunset']}")
    else:
        st.error("Could not fetch weather data for this place.")
elif city:
    weather = get_weather(city)
    if weather:
        st.subheader(f"Weather in {city.title()} {weather_icon(weather['description'])}")
        st.metric("Temp", f"{weather['temperature']}°C", f"Feels like {weather['feels_like']}°C")
        st.write(f"**Weather:** {weather['description'].title()}")
        st.write(f"💧 Humidity: {weather['humidity']}%")
        st.write(f"🌬️ Wind Speed: {weather['wind_speed']} m/s")
        st.write("_Highs and lows not available for typed cities._")
    else:
        st.error("City not found. Please try again.")


