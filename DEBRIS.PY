import streamlit as st
import requests
import pandas as pd
import io

# Function to fetch NEO data from NASA API
def fetch_neo_data(params):
    url = "https://ssd.jpl.nasa.gov/api/neo/export"
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return pd.read_csv(io.StringIO(response.text))
    else:
        st.error(f"Error fetching NEO data: {response.status_code} - {response.text}")
        return None

# Function to fetch TLE data from the TLE API
def fetch_tle_data():
    url = "https://tle.debris.stsci.edu/neo_tle.txt"
    response = requests.get(url)
    if response.status_code == 200:
        tle_data = response.text.strip().splitlines()
        # Creating DataFrame from TLE data
        return pd.DataFrame([line.split() for line in tle_data[1:]], columns=tle_data[0].split())
    else:
        st.error(f"Error fetching TLE data: {response.status_code} - {response.text}")
        return None

# Create a Streamlit app
st.title("Small Body Database")

# Create a form to select parameters for NEO data
with st.form("select_parameters"):
    kind = st.selectbox("Limit by Object Kind/Group", ["neo", "pha"])
    orbit_class = st.selectbox("Limit By Orbit Class", ["Apollo", "Aten", "Amor"])
    fields = st.multiselect("Select Keplerian parameters", ["e", "a", "i", "peri", "M", "n"])

    # Create a submit button
    submitted = st.form_submit_button("Get NEO Results")

# If the form is submitted, retrieve the NEO data
if submitted:
    params = {
        "kind": kind,
        "orbit_class": orbit_class,
        "output": "csv",
        "fields": ",".join(fields)
    }
    neo_df = fetch_neo_data(params)
    if neo_df is not None:
        st.write(neo_df)

# Create a form to select parameters for TLE data
with st.form("select_tle_parameters"):
    tle_fields = st.multiselect("Select TLE fields", [
        "Satellite Catalog Number", "Elset Classification", "International Designator", 
        "Epoch Time (UTC)", "1st Derivative of Mean Motion", "2nd Derivative of Mean Motion", 
        "B* Drag Term", "Element Set Type", "Element Number", "Checksum1", 
        "Orbit Inclination", "RA of Ascending Node", "Eccentricity", 
        "Argument of Perigee", "Mean Anomaly", "Mean Motion", 
        "Revolution Number at Epoch", "Checksum2"
    ])

    # Create a submit button
    tle_submitted = st.form_submit_button("Get TLE Results")

# If the form is submitted, retrieve the TLE data
if tle_submitted:
    tle_df = fetch_tle_data()
    if tle_df is not None:
        # Filter TLE DataFrame if specific fields are selected
        if tle_fields:
            tle_df = tle_df[tle_fields]
        st.write(tle_df)
