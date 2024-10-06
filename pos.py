# celestial_position_app.py
import streamlit as st
import numpy as np
from datetime import datetime, timedelta


def calculate_position(a, e, i, omega, w, nu, time_increment):
   
    i_rad = np.radians(i)
    omega_rad = np.radians(omega)
    w_rad = np.radians(w)
    nu_rad = np.radians(nu)

    mu = 398600 
    n = np.sqrt(mu / (a**3))

    
    M = n * time_increment.total_seconds()  

    # Eccentric anomaly (E) using Kepler's equation
    E = M  # Initial guess
    for _ in range(10):  # Iterate to solve for E
        E = M + e * np.sin(E)

    # True anomaly (nu) from E
    nu = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2), np.sqrt(1 - e) * np.cos(E / 2))

    # Distance (r)
    r = a * (1 - e * np.cos(E))

    # Position in 3D space (x, y, z)
    x = r * (np.cos(omega_rad) * np.cos(w_rad + nu) - np.sin(omega_rad) * np.sin(w_rad + nu) * np.cos(i_rad))
    y = r * (np.sin(omega_rad) * np.cos(w_rad + nu) + np.cos(omega_rad) * np.sin(w_rad + nu) * np.cos(i_rad))
    z = r * (np.sin(i_rad) * np.sin(w_rad + nu))

    return {'x': x, 'y': y, 'z': z}

# Streamlit UI
st.title("Celestial Position Calculator")

# Input fields for Keplerian parameters
a = st.number_input("Semi-major axis (a in km):", value=10000.0)
e = st.number_input("Eccentricity (e):", value=0.1)
i = st.number_input("Inclination (i in degrees):", value=10.0)
omega = st.number_input("Right Ascension of Ascending Node (Ω in degrees):", value=0.0)
w = st.number_input("Argument of Periapsis (ω in degrees):", value=0.0)
nu = st.number_input("True Anomaly (ν in degrees):", value=0.0)

# Button to calculate position
if st.button("Calculate Position"):
    # Calculate position after 1 hour
    now = datetime.utcnow()
    time_increment = timedelta(hours=1)  # Update after 1 hour
    pos = calculate_position(a, e, i, omega, w, nu, time_increment)
    
    # Display the results
    st.write(f"Position after 1 hour: (x: {pos['x']:.2f}, y: {pos['y']:.2f}, z: {pos['z']:.2f})")

# Optional: Add a refresh button
if st.button("Refresh Position"):
    # Calculate position with current inputs
    pos = calculate_position(a, e, i, omega, w, nu, time_increment)
    st.write(f"Current Position: (x: {pos['x']:.2f}, y: {pos['y']:.2f}, z: {pos['z']:.2f})")
