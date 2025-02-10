import streamlit as st
import numpy as np

def calculate_centripetal_acceleration(v, r):
    return v**2 / r

def calculate_tangential_velocity(a, r):
    return np.sqrt(a * r)

def calculate_radius(v, a):
    return v**2 / a

def calculate_centripetal_force(m, v, r):
    return m * v**2 / r

def calculate_gravitational_force(m, g=10):
    return m * g

def calculate_normal_or_tension_force(m, v, r, g=10):
    return m * (v**2 / r + g)

st.title("Vertical Loop Motion Calculator")

st.sidebar.header("Input Parameters")
loop_position = st.sidebar.selectbox("Select Loop Position:", ["Top of the Loop", "Bottom of the Loop"], key="unique_loop_position")

calculation_type = st.sidebar.selectbox("What would you like to solve for:", ["Centripetal Acceleration", "Tangential Velocity", "Radius of the Loop", "Mass", "Centripetal Force", "Normal/Tension Force", "Gravitational Force"], key="unique_calculation_type")

g = 10  # Gravity (m/s²)

if calculation_type == "Centripetal Acceleration":
    radius = st.sidebar.number_input("Radius (m)", min_value=0.1, value=5.0, step=0.1)
    velocity = st.sidebar.number_input("Tangential Velocity (m/s)", min_value=0.0, value=5.0, step=0.1)
    acceleration = calculate_centripetal_acceleration(velocity, radius)
    st.write(f"Centripetal Acceleration: {acceleration:.2f} m/s²")

elif calculation_type == "Tangential Velocity":
    acceleration = st.sidebar.number_input("Centripetal Acceleration (m/s²)", min_value=0.1, value=5.0, step=0.1)
    radius = st.sidebar.number_input("Radius (m)", min_value=0.1, value=5.0, step=0.1)
    velocity = calculate_tangential_velocity(acceleration, radius)
    st.write(f"Tangential Velocity: {velocity:.2f} m/s")

elif calculation_type == "Radius of the Loop":
    velocity = st.sidebar.number_input("Tangential Velocity (m/s)", min_value=0.0, value=5.0, step=0.1)
    acceleration = st.sidebar.number_input("Centripetal Acceleration (m/s²)", min_value=0.1, value=5.0, step=0.1)
    radius = calculate_radius(velocity, acceleration)
    st.write(f"Radius of the Loop: {radius:.2f} m")

elif calculation_type == "Mass":
    acceleration = st.sidebar.number_input("Acceleration (m/s²)", min_value=0.1, value=5.0, step=0.1)
    st.write("Mass input required for specific calculations later.")

elif calculation_type == "Centripetal Force":
    radius = st.sidebar.number_input("Radius (m)", min_value=0.1, value=5.0, step=0.1)
    velocity = st.sidebar.number_input("Tangential Velocity (m/s)", min_value=0.0, value=5.0, step=0.1)
    mass = st.sidebar.number_input("Mass (kg)", min_value=0.1, value=1.0, step=0.1)
    force = calculate_centripetal_force(mass, velocity, radius)
    st.write(f"Centripetal Force: {force:.2f} N")

elif calculation_type == "Normal/Tension Force":
    radius = st.sidebar.number_input("Radius (m)", min_value=0.1, value=5.0, step=0.1)
    velocity = st.sidebar.number_input("Tangential Velocity (m/s)", min_value=0.0, value=5.0, step=0.1)
    mass = st.sidebar.number_input("Mass (kg)", min_value=0.1, value=1.0, step=0.1)
    force = calculate_normal_or_tension_force(mass, velocity, radius, g)
    st.write(f"Normal/Tension Force: {force:.2f} N")

elif calculation_type == "Gravitational Force":
    mass = st.sidebar.number_input("Mass (kg)", min_value=0.1, value=1.0, step=0.1)
    force = calculate_gravitational_force(mass, g)
    st.write(f"Gravitational Force: {force:.2f} N")
