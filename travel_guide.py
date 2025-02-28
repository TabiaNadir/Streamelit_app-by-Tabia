import streamlit as st
from scraper import get_tourist_places
from api_services import get_weather

st.title("🌍 AI-Powered Travel Guide")
st.write("Enter a city name and explore the best places to visit!")

city = st.text_input("Enter City Name", "")

if city:
    st.write(f"Fetching details for **{city}**...")

    places = get_tourist_places(city)
    st.write("### ✨ Top Tourist Places:")
    for place in places:
        st.write(f"- {place}")

    weather = get_weather(city)
    st.write("### 🌦️ Weather Info:")
    st.write(weather)

    