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
from weather_api import get_weather

st.set_page_config(page_title="Weather Dashboard", page_icon="🌦️", layout="centered")

st.title("🌤️ Daddy's Weather Monitoring Station")
st.markdown("Get the latest weather updates for any city in the world.")

# Dropdown list of preset cities
preset_cities = {
    "Cranbrook, UK": "Cranbrook,GB",
    "Loughborough, UK": "Loughborough,GB",
    "Fuengirola, Spain": "Fuengirola,ES",
    "Bath, UK": "Bath,GB",
    "Singapore": "Singapore,SG",
    "Macclesfield, UK": "Macclesfield,GB",
}

st.markdown("### 📍 Choose a city from the dropdown or type your own:")

selected_city = st.selectbox("Select a preset city:", options=[""] + list(preset_cities.keys()))
typed_city = st.text_input("Or enter a city name (optionally with country code):")

# Decide which city to use
if selected_city:
    city = preset_cities[selected_city]
elif typed_city:
    city = typed_city
else:
    city = None

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

if city:
    weather = get_weather(city)
    if weather:
        st.subheader(f"Weather in {city.split(',')[0].title()} {weather_icon(weather['description'])}")

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
