import streamlit as st
from weather_api import get_weather

st.set_page_config(page_title="Weather Dashboard", layout="centered")

st.title("🌤️ Weather Dashboard")

city = st.text_input("Enter a city name:")

if city:
    weather = get_weather(city)
    
    if weather:
        st.subheader(f"Weather in {city.title()}")
        st.write(f"**Temperature:** {weather['temperature']}°C")
        st.write(f"**Feels like:** {weather['feels_like']}°C")
        st.write(f"
