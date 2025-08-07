import streamlit as st
from weather_api import get_weather

st.set_page_config(page_title="Weather Dashboard",page_icon="🌦️", layout="centered")

st.title("🌤️ Daddy's weather monitoring station")

st.markdown("Get the latest weather updates for any city in the world.")

st.markdown("### 📍 Enter a city to check its weather")

city = st.text_input("Enter a city name: (you may need to add country code eg UK!)")

if city:
    weather = get_weather(city)
    
    if weather:
        st.subheader(f"Weather in {city.title()}")
        st.write(f"🌡️**Temperature:** {weather['temperature']}°C")
        st.write(f"**Feels like:** {weather['feels_like']}°C")
        st.write(f"**Weather:** {weather['description'].title()}")
        st.write(f"😅**Humidity:** {weather['humidity']}%")
        st.write(f"**Wind Speed:** {weather['wind_speed']} m/s")
    else:
        st.error("Could not fetch weather data. Please check the city name.")
        st.success("Data loaded successfully!")  # After weather fetch

