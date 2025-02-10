import streamlit as st
import numpy as np

def minimum_velocity_top(radius, g=10):
    return np.sqrt(g * radius)

def velocity_bottom(velocity_top, radius, g=10):
    return np.sqrt(velocity_top**2 + 2 * g * radius)

def will_fall(velocity_top, radius, g=10):
    return velocity_top < minimum_velocity_top(radius, g)

st.title("Vertical Loop Motion Calculator")

st.sidebar.header("Input Parameters")
option = st.sidebar.radio("Choose Calculation:",
                          ["Calculate Velocity at Top", "Calculate Velocity at Bottom", "Check if Object Will Fall", "Calculate Loop Radius"])

radius = st.sidebar.number_input("Loop Radius (m)", min_value=0.1, value=5.0, step=0.1)

g = 10  # Gravity (m/s²)

if option == "Calculate Velocity at Top":
    velocity_top = minimum_velocity_top(radius, g)
    st.write(f"Minimum Velocity Required at the Top: {velocity_top:.2f} m/s")

elif option == "Calculate Velocity at Bottom":
    velocity_top = st.sidebar.number_input("Velocity at Top (m/s)", min_value=0.0, value=5.0, step=0.1, key=f"velocity_top_{option.replace(' ', '_')}_{option}")
    velocity_bot = velocity_bottom(velocity_top, radius, g)
    st.write(f"Velocity at the Bottom: {velocity_bot:.2f} m/s")

elif option == "Check if Object Will Fall":
    velocity_top = st.sidebar.number_input("Velocity at Top (m/s)", min_value=0.0, value=5.0, step=0.1, key=f"velocity_top_{option.replace(' ', '_')}_{option}")
    falls = will_fall(velocity_top, radius, g)
    if falls:
        st.error("The object will fall at the top of the loop!")
    else:
        st.success("The object will stay on track at the top of the loop.")

elif option == "Calculate Loop Radius":
    velocity_top = st.sidebar.number_input("Velocity at Top (m/s)", min_value=0.0, value=5.0, step=0.1, key=f"velocity_top_{option.replace(' ', '_')}_{option}")
    radius = (velocity_top ** 2) / g
    st.write(f"Required Loop Radius: {radius:.2f} m")
    velocity_top = st.sidebar.number_input("Velocity at Top (m/s)", min_value=0.0, value=5.0, step=0.1, key=f"velocity_top_{option.replace(' ', '_')}_{option}")
    falls = will_fall(velocity_top, radius, g)
    if falls:
        st.error("The object will fall at the top of the loop!")
    else:
        st.success("The object will stay on track at the top of the loop.")
