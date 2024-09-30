import streamlit as st

# Initialize the Streamlit app
st.title("NDUI Data Availability")

# Description
st.write("Below is a list of cities organized by continent. If you want to request a city outside of this list, please fill out [this form](https://example.com/form).")

# Cities categorized by continents
st.subheader("North America")
st.write("""
- **Austin Region**: Austin, Houston, San Antonio, Dallas, Fort Worth  
- **LA Region**: LA, San Diego, Ensenada, Mexicali, San Jose, San Francisco, Las Vegas, Fresno  
- **Albuquerque Region**: Las Cruces, Alamogordo, Gallup, Santa Fe, Taos, Durango  
- **Denver Region**: Denver, Boulder, Colorado Springs, Pueblo, Cheyenne  
- **Portland Region**: Salem, Corvallis, Eugene, Newport, Lincoln City, Bend, Olympia  
- **Louisville Region**: Louisville, Nashville, Indianapolis, Cincinnati, Blomington, Evansville, Lexington, Bowling Green, Clarksville, Paducah  
- **Washington DC Region**: Washington DC, Richmond, Ocean City, Baltimore, Pittsburgh, Philadelphia, New York  
- **Kansas City Region**: Kansas City, Memphis, St. Louis  
- **Columbus Region**: Columbus, Akron, Cleveland  
- **Minneapolis Region**: Minneapolis, Rochester, St. Cloud  
- **Seattle Region**: Seattle, Tacoma, Victoria, Vancouver
""")

st.subheader("Asia")
st.write("""
- **Delhi Region**: Delhi, Chandigarh, Meerut, Dehradun, Patiala, Gurgaon, Alwar, Mathura, Aligarh, Agra, Rampur, Bareily  
- **Hong Kong Region**: Hong Kong, Macao, Guangzhou, Qingyuan, Shaoguan, Huizhou, Heyuan, Yangjiang, Yunfu, Shanwei  
- **Dubai Region**: Dubai, Abu Dhabi, Al Ain, Sohar, Ras Al-Khaimah  
- **Tokyo Region**: Tokyo, Yokohama, Niigata, Honshu  
- **Dhaka Region**: Dhaka, Kolkata, Khulna, Jashore, Kuakata, Barishal, Cumilla, Bogura, Mymensingh  
- **Shanghai Region**: Shanghai, Taizhou, Hangzhou, Suzhou, Nanjing, Yancheng
""")

st.subheader("Australia")
st.write("""
- **Melbourne Region**: Melbourne, Shepparton, Canberra, Geelong
""")

st.subheader("Europe")
st.write("""
- **London Region**: London, Bournemouth, Exeter, Plymouth, Bristol, Cardiff, Oxford, Birmingham, Cambridge, Norwich  
- **Berlin Region**: Berlin, Dresden, Leipzig, Magdeburg, Potsdam, Hanover, Poznan, Zeilona Gora, Szczecin
""")

st.subheader("South America")
st.write("""
- **Sao Paulo Region**: Campinas, Sao Carlos, Rio de Janeiro  
- **Mexico City Region**: Mexico City, Santiago de Quertaro, Toluca, Cuernavaca, Morelia, Chilpancingo, Tehuacan, Puebla
""")

st.subheader("Africa")
st.write("""
- **Cairo Region**: Tanta, Faiyum, Al Fashn, Maghagha, Suez, 10th of Ramadan City, Ismailia, Zagazig, Banha, Mansoura, Tanta, Damanhour, El Sadat City
""")

# Form link
st.write("If you want to request a city outside this list, please fill out [this form](https://forms.gle/fU1Mukg1UAwne8AT6).")
