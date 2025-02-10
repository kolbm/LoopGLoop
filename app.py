import streamlit as st
import numpy as np

def minimum_velocity_top(radius, g=10):
    return np.sqrt(g * radius)

def velocity_bottom(velocity_top, radius, g=10):
    return np.sqrt(velocity_top**2 + 2 * g * radius)

def calculate_radius(velocity_top, g=10):
    return velocity_top**2 / g

def will_fall(velocity_top, radius, g=10):
    return velocity_top < minimum_velocity_top(radius, g)

st.title("Vertical Loop Motion Calculator")



st.sidebar.header("Input Parameters")
loop_position = st.sidebar.selectbox("Select Loop Position:", ["Top of the Loop", "Bottom of the Loop"], key="loop_position")

# Displaying force diagram based on the loop position
if loop_position == "Top of the Loop":
    st.image("top_loop.png", caption="Forces at the Top of the Loop")
elif loop_position == "Bottom of the Loop":
    st.image("bottom_loop.png", caption="Forces at the Bottom of the Loop")
calculation_type = st.sidebar.selectbox("What would you like to solve for:", ["Centripetal Acceleration", "Tangential Velocity", "Radius of the Loop", "Mass", "Normal Force", "Gravitational Force", "Centripetal Force"], key="calculation_type")

if calculation_type in ["Normal Force", "Gravitational Force", "Centripetal Force"]:
    mass = st.sidebar.number_input("Mass (kg)", min_value=0.1, value=1.0, step=0.1)  # Mass is required for force calculations

if calculation_type in ["Normal Force", "Gravitational Force", "Centripetal Force"]:
    mass = st.sidebar.number_input("Mass (kg)", min_value=0.1, value=1.0, step=0.1)  # Mass is required for force calculations
loop_position = st.sidebar.selectbox("Select Loop Position:", ["Top of the Loop", "Bottom of the Loop"], key="loop_position")

# Displaying force diagram based on the loop position
if loop_position == "Top of the Loop":
    st.image("top_loop.png", caption="Forces at the Top of the Loop")
elif loop_position == "Bottom of the Loop":
    st.image("bottom_loop.png", caption="Forces at the Bottom of the Loop")

calculation_type = st.sidebar.selectbox("What would you like to solve for:", ["Centripetal Acceleration", "Tangential Velocity", "Radius of the Loop", "Mass", "Normal Force", "Gravitational Force", "Centripetal Force"], key="calculation_type")
option = st.sidebar.radio("Choose Calculation:", ["Calculate Minimum Velocity at Top", "Calculate Velocity at Bottom", "Check if Object Will Fall", "Calculate Loop Radius"], key="calculation_option")

g = 10  # Gravity (m/s²)

if option == "Calculate Minimum Velocity at Top":
    radius = st.sidebar.number_input("Loop Radius (m)", min_value=0.1, value=5.0, step=0.1)
    velocity_top = minimum_velocity_top(radius, g)
    st.write(f"Minimum Velocity Required at the Top: {velocity_top:.2f} m/s")

elif option == "Calculate Velocity at Bottom":
    radius = st.sidebar.number_input("Loop Radius (m)", min_value=0.1, value=5.0, step=0.1)
    velocity_top = st.sidebar.number_input("Velocity at Top (m/s)", min_value=0.0, value=5.0, step=0.1, key="velocity_bottom")
    velocity_bot = velocity_bottom(velocity_top, radius, g)
    st.write(f"Velocity at the Bottom: {velocity_bot:.2f} m/s")

elif option == "Check if Object Will Fall":
    radius = st.sidebar.number_input("Loop Radius (m)", min_value=0.1, value=5.0, step=0.1)
    velocity_top = st.sidebar.number_input("Velocity at Top (m/s)", min_value=0.0, value=5.0, step=0.1, key="check_fall")
    falls = will_fall(velocity_top, radius, g)
    if falls:
        st.error("The object will fall at the top of the loop!")
    else:
        st.success("The object will stay on track at the top of the loop.")

elif option == "Calculate Loop Radius":
    velocity_top = st.sidebar.number_input("Velocity at Top (m/s)", min_value=0.0, value=5.0, step=0.1, key="calculate_radius")
    radius = calculate_radius(velocity_top, g)
    st.write(f"Required Loop Radius: {radius:.2f} m")
