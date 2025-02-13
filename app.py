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

def calculate_normal_force_bottom(m, v, r, g=10):
    """Calculate the normal force at the bottom of the loop."""
    return m * (v**2 / r + g)

def calculate_normal_force_top(m, v, r, g=10):
    """Calculate the normal force at the top of the loop."""
    return m * (v**2 / r - g)


st.title("Vertical Loop Motion Calculator")

st.sidebar.header("Input Parameters")
loop_position = st.sidebar.selectbox("Select Loop Position:", ["Top of the Loop", "Bottom of the Loop"], key="unique_loop_position")

# Displaying force diagram based on the loop position
try:
    if loop_position == "Top of the Loop":
        st.image("top_loop.png", caption="Forces at the Top of the Loop")
    elif loop_position == "Bottom of the Loop":
        st.image("bottom_loop.png", caption="Forces at the Bottom of the Loop")
except FileNotFoundError:
    st.warning("Image not found. Please ensure 'top_loop.png' and 'bottom_loop.png' are in the correct directory.")

calculation_type = st.sidebar.selectbox("What would you like to solve for:", ["Centripetal Acceleration", "Tangential Velocity", "Radius of the Loop", "Mass", "Centripetal Force", "Normal/Tension Force", "Gravitational Force"], key="unique_calculation_type")

g = 10  # Gravity (m/s²)

if calculation_type == "Centripetal Acceleration":
    st.latex(r"a_c = \frac{{v_T}^2}{r}")
    radius = st.sidebar.number_input("Radius (m)", min_value=0.1, value=5.0, step=0.1)
    velocity = st.sidebar.number_input("Tangential Velocity (m/s)", min_value=0.0, value=5.0, step=0.1)
    acceleration = calculate_centripetal_acceleration(velocity, radius)
    st.write(f"Centripetal Acceleration: {acceleration:.2f} m/s²")

elif calculation_type == "Tangential Velocity":
    st.latex(r"{v_T} = \sqrt{a_c \cdot r}")
    acceleration = st.sidebar.number_input("Centripetal Acceleration (m/s²)", min_value=0.1, value=5.0, step=0.1)
    radius = st.sidebar.number_input("Radius (m)", min_value=0.1, value=5.0, step=0.1)
    velocity = calculate_tangential_velocity(acceleration, radius)
    st.write(f"Tangential Velocity: {velocity:.2f} m/s")

elif calculation_type == "Radius of the Loop":
    st.latex(r"r = \frac{{v_T}^2}{a_c}")
    velocity = st.sidebar.number_input("Tangential Velocity (m/s)", min_value=0.0, value=5.0, step=0.1)
    acceleration = st.sidebar.number_input("Centripetal Acceleration (m/s²)", min_value=0.1, value=5.0, step=0.1)
    radius = calculate_radius(velocity, acceleration)
    st.write(f"Radius of the Loop: {radius:.2f} m")

elif calculation_type == "Centripetal Force":
    st.latex(r"F_c = m \cdot \frac{{v_T}^2}{r}")
    radius = st.sidebar.number_input("Radius (m)", min_value=0.1, value=5.0, step=0.1)
    velocity = st.sidebar.number_input("Tangential Velocity (m/s)", min_value=0.0, value=5.0, step=0.1)
    mass = st.sidebar.number_input("Mass (kg)", min_value=0.1, value=1.0, step=0.1)
    force = calculate_centripetal_force(mass, velocity, radius)
    st.write(f"Centripetal Force: {force:.2f} N")

elif calculation_type == "Gravitational Force":
    st.latex(r"F_g = m \cdot g")
    mass = st.sidebar.number_input("Mass (kg)", min_value=0.1, value=1.0, step=0.1)
    force = calculate_gravitational_force(mass, g)
    st.write(f"Gravitational Force: {force:.2f} N")

elif calculation_type == "Normal/Tension Force":
    radius = st.sidebar.number_input("Radius (m)", min_value=0.1, value=5.0, step=0.1)
    velocity = st.sidebar.number_input("Tangential Velocity (m/s)", min_value=0.0, value=5.0, step=0.1)
    mass = st.sidebar.number_input("Mass (kg)", min_value=0.1, value=1.0, step=0.1)

    if loop_position == "Bottom of the Loop":
        st.latex(r"F_N = m \left( \frac{{v_T}^2}{r} + g \right)")
        force = calculate_normal_force_bottom(mass, velocity, radius, g)
        st.write(f"Normal/Tension Force at the Bottom: {force:.2f} N")
    elif loop_position == "Top of the Loop":
        st.latex(r"F_N = m \left( \frac{{v_T}^2}{r} - g \right)")
        force = calculate_normal_force_top(mass, velocity, radius, g)
        st.write(f"Normal/Tension Force at the Top: {force:.2f} N")

 
