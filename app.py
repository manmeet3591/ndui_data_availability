import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim

# Initialize the Streamlit app
st.title("City Markers on Map")

# Function to get latitude and longitude from city names
def get_lat_lon(city):
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(city)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

# List of cities to display on the map
cities = ["New York", "London", "Tokyo", "Paris", "Delhi"]

# Create a map centered on the first city
city_coords = get_lat_lon(cities[0])
if city_coords:
    m = folium.Map(location=city_coords, zoom_start=4)
else:
    st.error("Could not locate the first city to center the map.")

# Add markers for each city
for city in cities:
    coords = get_lat_lon(city)
    if coords:
        folium.Marker(location=coords, popup=city).add_to(m)

# Display the map in the Streamlit app
st_folium(m, width=725)

st.write("Cities displayed: ", ", ".join(cities))
