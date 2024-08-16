import json
import streamlit as st
import requests

api = "http://api.weatherapi.com/v1/current.json?key=424ae1ef6bb1459e9cd91840241408&q=London&aqi=no"
getApi = requests.get(api).json()

st.title("B WEATHER APPLICATION")

user_option = st.text_input("Enter Location", placeholder="Your Present Location")
st.subheader("WEATHER INFORMATION")

user_location = getApi["location"]["name"]
temperature = getApi["current"]["temp_c"]
atmospheric = getApi["current"]["condition"]["text"]
wind_speed = getApi["current"]["wind_kph"]
wind_degree = getApi["current"]["wind_degree"]
wind_dir = getApi["current"]["wind_dir"]
precipitation = getApi["current"]["precip_mm"]
humidity = getApi["current"]["humidity"]
DewPoint = getApi["current"]["dewpoint_c"]
ultraviolet = getApi["current"]["uv"]
# Amount_of_carbon_in_the_air = getApi["current"]["air_quality"]["co"]
# if not user_option == user_location:
#     st.warning("Please Enter a Location")

if user_option == user_location:
    st.info = {f"""Weather Information below based on your present location\n
Temperature: {temperature}_c\n
Atmospheric Condition: {atmospheric}\n
Wind Speed: {wind_speed}\n
Wind Degree & Direction: {wind_degree} + {wind_dir}\n
Precipitation: {precipitation}\n
Humidity: {humidity}\n
Dew Point: {DewPoint}\n
Ultraviolet: {ultraviolet}
"""}

elif user_option != user_location:
    st.warning(f"{user_option} weather forecast is not available at the moment")
else:
    st.error("Invalid")


