import streamlit as st
import requests

# API Setup
API_KEY = "08d4aa006475247431fb0cb82de44551"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# App Title
st.title("Live Weather Checker & Smart Advice")

# User Input
city = st.text_input("Enter city name:")

if city:
    # Set parameters and send request
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        # Extract weather data
        temperature = data['main']['temp']
        weather = data['weather'][0]['main']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Show results
        st.subheader(f"Weather in {city.title()}")
        st.write(f"Temperature: {temperature} °C")
        st.write(f"Condition: {weather}")
        st.write(f"Humidity: {humidity}%")
        st.write(f"Wind Speed: {wind_speed} m/s")

        # Smart alerts
        if weather.lower() in ['rain', 'drizzle', 'thunderstorm']:
            st.warning(" It might rain today. Take your umbrella and stay dry")
        elif weather.lower() in ['clear']:
            if temperature > 30:
                st.warning(" The sun is blazing hot today. Drink lots of water and wear sunscreen.")
            elif temperature > 20:
                st.success(" It's a beautiful sunny day. Perfect for a walk")
            else:
                st.info("It's sunny but a bit chilly. Wear something cozy.")
        elif weather.lower() in ['clouds']:
            st.info("It's a bit cloudy today. Enjoy the cool breeze.")
        elif weather.lower() in ['snow']:
            st.warning(" It's snowing.  Dress warmly and stay safe.")
        else:
            st.info("Weather seems moderate today. Have a great day")

        # Extra temperature advice
        if temperature > 35:
            st.warning("It's extremely hot. Stay indoors if possible and stay hydrated.")
        elif temperature < 10:
            st.warning("It's very cold. Bundle up and keep warm.")
        elif 10 <= temperature <= 20:
            st.info("A light jacket should be fine for today.")
        elif 20 < temperature <= 30:
            st.success("The weather is just right. Enjoy")

    else:
        st.error("Could not retrieve weather data. Please check the city name and try again.")
