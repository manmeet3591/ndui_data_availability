import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Initialize the Streamlit app
st.title("NDUI data availability")

# Function to get latitude and longitude from city names with error handling
def get_lat_lon(city):
    geolocator = Nominatim(user_agent="your_app_name")  # Update with a unique app name
    try:
        location = geolocator.geocode(city, timeout=10)
        if location:
            return (location.latitude, location.longitude)
    except GeocoderTimedOut:
        st.error(f"Error: Geocoding for {city} timed out.")
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

st.write("NDUI data availability: ", ", ".join(cities))
