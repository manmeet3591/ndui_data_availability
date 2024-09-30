import streamlit as st
import pydeck as pdk
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Initialize the Streamlit app
st.title("NDUI Data Availability")

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
coords_list = []

# Fetch latitude and longitude for each city
for city in cities:
    coords = get_lat_lon(city)
    if coords:
        coords_list.append({"name": city, "lat": coords[0], "lon": coords[1]})
    else:
        st.error(f"Could not fetch coordinates for {city}")

# URL to the custom marker icon (Google Maps-like pin)
icon_url = "https://upload.wikimedia.org/wikipedia/commons/e/ec/RedDot.svg"

# Add icon details to each city coordinate
for coord in coords_list:
    coord["icon_data"] = {
        "url": icon_url,
        "width": 128,  # Adjust size of the icon
        "height": 128,
        "anchorY": 128,  # Position the icon correctly
    }

# Convert the list of coordinates into a Pydeck IconLayer
icon_layer = pdk.Layer(
    "IconLayer",
    data=coords_list,
    get_icon="icon_data",
    get_position="[lon, lat]",
    get_size=4,  # Size of the icon relative to other elements
    pickable=True,
)

# Create the Pydeck view for the entire globe
view_state = pdk.ViewState(latitude=0, longitude=0, zoom=1, bearing=0, pitch=0)

# Render the 3D globe in Streamlit
r = pdk.Deck(
    layers=[icon_layer],
    initial_view_state=view_state,
    tooltip={"text": "{name}"},
)

st.pydeck_chart(r)

# import streamlit as st
# import pydeck as pdk
# from geopy.geocoders import Nominatim
# from geopy.exc import GeocoderTimedOut

# # Initialize the Streamlit app
# st.title("NDUI data availability")

# # Function to get latitude and longitude from city names with error handling
# def get_lat_lon(city):
#     geolocator = Nominatim(user_agent="your_app_name")  # Update with a unique app name
#     try:
#         location = geolocator.geocode(city, timeout=10)
#         if location:
#             return (location.latitude, location.longitude)
#     except GeocoderTimedOut:
#         st.error(f"Error: Geocoding for {city} timed out.")
#         return None

# # List of cities to display on the map
# cities = ["New York", "London", "Tokyo", "Paris", "Delhi"]
# coords_list = []

# # Fetch latitude and longitude for each city
# for city in cities:
#     coords = get_lat_lon(city)
#     if coords:
#         coords_list.append({"name": city, "lat": coords[0], "lon": coords[1]})
#     else:
#         st.error(f"Could not fetch coordinates for {city}")

# # Convert the list of coordinates into a Pydeck layer
# layer = pdk.Layer(
#     "ScatterplotLayer",
#     coords_list,
#     get_position='[lon, lat]',
#     get_color='[200, 30, 0, 160]',
#     get_radius=500000,
#     pickable=True,
# )

# # Create the Pydeck view for the entire globe
# view_state = pdk.ViewState(latitude=0, longitude=0, zoom=1, bearing=0, pitch=0)

# # Render the 3D globe in Streamlit
# r = pdk.Deck(
#     layers=[layer],
#     initial_view_state=view_state,
#     tooltip={"text": "{name}"},
# )

# st.pydeck_chart(r)

# import streamlit as st
# import folium
# from streamlit_folium import st_folium
# from geopy.geocoders import Nominatim
# from geopy.exc import GeocoderTimedOut
# from folium.plugins import MarkerCluster

# # Initialize the Streamlit app
# st.title("NDUI data availability")

# # Function to get latitude and longitude from city names with error handling
# def get_lat_lon(city):
#     geolocator = Nominatim(user_agent="your_app_name")  # Update with a unique app name
#     try:
#         location = geolocator.geocode(city, timeout=10)
#         if location:
#             return (location.latitude, location.longitude)
#     except GeocoderTimedOut:
#         st.error(f"Error: Geocoding for {city} timed out.")
#         return None

# # List of cities to display on the map
# cities = ["New York", "London", "Tokyo", "Paris", "Delhi"]

# # Create a map centered on the first city
# city_coords = get_lat_lon(cities[0])
# if city_coords:
#     m = folium.Map(location=city_coords, zoom_start=4)
# else:
#     st.error("Could not locate the first city to center the map.")

# # Add a marker cluster to group nearby cities (optional, for better performance)
# marker_cluster = MarkerCluster().add_to(m)

# # Add pin-like markers for each city
# for city in cities:
#     coords = get_lat_lon(city)
#     if coords:
#         # Using folium Icon to simulate Google Maps marker (pin-style)
#         folium.Marker(
#             location=coords,
#             popup=folium.Popup(city, parse_html=True),
#             icon=folium.Icon(color='red', icon='info-sign')  # Simulate Google Maps pin with red marker
#         ).add_to(marker_cluster)

# # Display the map in the Streamlit app
# st_folium(m, width=725)

# st.write("Cities displayed: ", ", ".join(cities))
########################################

# import streamlit as st
# import pydeck as pdk
# from geopy.geocoders import Nominatim
# from geopy.exc import GeocoderTimedOut

# # Initialize the Streamlit app
# st.title("NDUI data availability")

# # Function to get latitude and longitude from city names with error handling
# def get_lat_lon(city):
#     geolocator = Nominatim(user_agent="your_app_name")  # Update with a unique app name
#     try:
#         location = geolocator.geocode(city, timeout=10)
#         if location:
#             return (location.latitude, location.longitude)
#     except GeocoderTimedOut:
#         st.error(f"Error: Geocoding for {city} timed out.")
#         return None

# # List of cities to display on the map
# cities = ["New York", "London", "Tokyo", "Paris", "Delhi"]
# coords_list = []

# # Fetch latitude and longitude for each city
# for city in cities:
#     coords = get_lat_lon(city)
#     if coords:
#         coords_list.append({"name": city, "lat": coords[0], "lon": coords[1]})
#     else:
#         st.error(f"Could not fetch coordinates for {city}")

# # Convert the list of coordinates into a Pydeck layer
# layer = pdk.Layer(
#     "ScatterplotLayer",
#     coords_list,
#     get_position='[lon, lat]',
#     get_color='[200, 30, 0, 160]',
#     get_radius=500000,
#     pickable=True,
# )

# # Create the Pydeck view
# view_state = pdk.ViewState(latitude=20, longitude=0, zoom=1, bearing=0, pitch=45)

# # Render the 3D globe in Streamlit
# r = pdk.Deck(
#     layers=[layer],
#     initial_view_state=view_state,
#     tooltip={"text": "{name}"},
# )

# st.pydeck_chart(r)
###########################################

# import streamlit as st
# import folium
# from streamlit_folium import st_folium
# from geopy.geocoders import Nominatim
# from geopy.exc import GeocoderTimedOut

# # Initialize the Streamlit app
# st.title("NDUI data availability")

# # Function to get latitude and longitude from city names with error handling
# def get_lat_lon(city):
#     geolocator = Nominatim(user_agent="your_app_name")  # Update with a unique app name
#     try:
#         location = geolocator.geocode(city, timeout=10)
#         if location:
#             return (location.latitude, location.longitude)
#     except GeocoderTimedOut:
#         st.error(f"Error: Geocoding for {city} timed out.")
#         return None

# # List of cities to display on the map
# cities = ["New York", "London", "Tokyo", "Paris", "Delhi"]

# # Create a map centered on the first city
# city_coords = get_lat_lon(cities[0])
# if city_coords:
#     m = folium.Map(location=city_coords, zoom_start=4)
# else:
#     st.error("Could not locate the first city to center the map.")

# # Add markers for each city
# for city in cities:
#     coords = get_lat_lon(city)
#     if coords:
#         folium.Marker(location=coords, popup=city).add_to(m)

# # Display the map in the Streamlit app
# st_folium(m, width=725)

# st.write("NDUI data availability: ", ", ".join(cities))
