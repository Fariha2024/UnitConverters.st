import streamlit as st
from pint import UnitRegistry
import requests
from components.header import load_header  # Import the header function

# ✅ Move this to the top
st.set_page_config(page_title="Universal Unit Converter", page_icon="📏", layout="wide")

# Load Header
load_header()

# Initialize UnitRegistry
ureg = UnitRegistry()

    
# Custom CSS for Styling
st.markdown(
    f"""
    <style>
        body, .stApp {{
            background-color:#f8f8f8 ;
        }}
        .stTextInput input, .stNumberInput input {{
            background-color: #eaf2e7!important;
            color: #277e07   !important;
            font-size: 16px;
        }}
        .stSelectbox div {{
            background-color: #f8f8f8 !important;
            color:#277e07 !important;
        }}
        .stButton button {{
            background-color: #f8f8f8 !important;
            color: #f8f8f8  !important;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
        }}

      .stNumberInput, .stSelectbox {{
        background-color: #eaf2e7;
        padding: 10px;
        border-radius: 10px;
       }}
        .stSuccess {{
            color: #277e07;
        }}
        .stError {{
            color: #dc3545;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #277e07;
            color: #277e07 !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)


# Sidebar Navigation
import streamlit as st

# Sidebar Navigation (with unique key)
page = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "📏 Universal Unit Converter", "🧮 BMI Calculator", "💰 Interest Calculator", "📚 Help & FAQs", "📐 Common Unit System"],
    key="unique_navigation_key"
)

# Function to jump to the selected section
def navigate_to_section(title):
    st.markdown(f"<h2 style='color:#277e07;'>{title}</h2>", unsafe_allow_html=True)

# Ensure "page" is defined before using it
if "page" in locals():
    if page == "🏠 Home":
        navigate_to_section("🏠 Home")
        st.write("Welcome to the unversal UnitConverter.st!")

    elif page == "📏 Universal Unit Converter":
        navigate_to_section("📏 Universal Unit Converter")
        st.write("Convert units easily between different measurement systems.")

    elif page == "🧮 BMI Calculator":
        navigate_to_section("🧮 BMI Calculator")




        
        weight = st.number_input("Enter Weight (kg):", min_value=0.0, step=0.1, format="%.1f", key="bmi_weight")
        height = st.number_input("Enter Height (m):", min_value=0.0, step=0.01, format="%.2f", key="bmi_height")
        
        if st.button("Calculate BMI", key="bmi_button"):
            bmi = weight / (height ** 2) if height > 0 else 0
            st.write(f"**Your BMI is:** {bmi:.2f}")

    elif page == "💰 Interest Calculator":
        navigate_to_section("💰 Interest Calculator")
        
        principal = st.number_input("Enter Principal Amount:", min_value=0.0, step=0.1, format="%.2f", key="interest_principal")
        rate = st.number_input("Enter Interest Rate (%):", min_value=0.0, step=0.1, format="%.2f", key="interest_rate")
        time = st.number_input("Enter Time (years):", min_value=0.0, step=1.0, format="%.1f", key="interest_time")

        if st.button("Calculate Interest", key="interest_button"):
            interest = (principal * rate * time) / 100
            st.write(f"**Total Interest:** {interest:.2f}")

    elif page == "📚 Help & FAQs":
        navigate_to_section("📚 Help & FAQs")
        st.write("Need assistance? Here's how you can use the app!")

    elif page == "📐 Common Unit System":
        navigate_to_section("📐 Common Unit System")
        st.write("Learn about common unit systems and conversions.")


# Title and Description

st.write("Convert any unit with ease! Supports length, weight, temperature, volume, time, and more.")
st.write("Use the navigation sidebar to access different features.")



# Unit Categories
categories = {
    "Length": ["meter", "foot", "inch", "kilometer", "mile"],
    "Weight": ["kilogram", "pound", "ounce", "gram"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Volume": ["liter", "gallon", "milliliter", "cubic meter"],
    "Time": ["second", "minute", "hour", "day"],
    "Currency": ["USD", "EUR", "GBP", "INR", "JPY"]  # Add more currencies as needed
}

# Sidebar for Category Selection
category = st.sidebar.selectbox("Select Category", list(categories.keys()))

# Input Fields
col1, col2 = st.columns(2)
with col1:
    value = st.number_input("Enter Value", min_value=0.0, step=0.1)
with col2:
    from_unit = st.selectbox("From Unit", categories[category])
    to_unit = st.selectbox("To Unit", categories[category])

# Conversion Logic
try:
    if category == "Currency":
        # Fetch real-time exchange rates
        api_key = "YOUR_API_KEY"  # Replace with a real API key
        url = f"https://api.exchangerate-api.com/v4/latest/{from_unit}"
        response = requests.get(url)
        data = response.json()

        if to_unit in data["rates"]:
            rate = data["rates"][to_unit]
            converted = value * rate
            st.success(f"**Converted Value:** {converted:.4f} {to_unit}")
        else:
            st.error("Invalid currency conversion.")
    
    else:
        # Use pint for unit conversions
        quantity = value * ureg(from_unit)
        converted = quantity.to(to_unit).magnitude
        st.success(f"**Converted Value:** {converted:.4f} {to_unit}")

except Exception as e:
    st.error(f"**Error:** {e}")

import streamlit as st

# -*- coding: utf-8 -*-
import streamlit as st
from components.header2 import load_header2  # Import the header function

# Load Header
load_header2()

# Load Custom CSS
with open(".streamlit/assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title

st.write("Perform different calculations.")

# =========================
# **BMI Calculator**
# =========================
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# **User Inputs**
age = st.number_input("Enter Age:", min_value=1, step=1, format="%d")
gender = st.selectbox("Select Gender:", ["Male", "Female", "Other"])

# **Unit selection**
weight_unit = st.selectbox("Select Weight Unit:", ["kg", "lbs"])
height_unit = st.selectbox("Select Height Unit:", ["feet & inches"])

# **Weight Input**
if weight_unit == "kg":
    weight = st.number_input("Enter Weight (kg):", min_value=0.0, step=0.1, format="%.1f")
else:
    weight = st.number_input("Enter Weight (lbs):", min_value=0.0, step=0.1, format="%.1f")
    weight = weight * 0.453592  # Convert lbs to kg

# **Height Input**
feet = st.number_input("Feet:", min_value=0, step=1, format="%d")
inches = st.number_input("Inches:", min_value=0, step=1, format="%d")
height = ((feet * 12) + inches) * 0.0254  # Convert ft/in to meters

# **BMI Calculation & Interpretation**
if weight > 0 and height > 0:
    bmi = weight / (height ** 2)
    st.success(f"**Your BMI is:** {bmi:.2f}")

    # BMI Categories
    if bmi < 18.5:
        st.info("🔵 **You are underweight.** Consider a balanced diet to gain weight.")
    elif 18.5 <= bmi < 24.9:
        st.success("✅ **You have a normal weight.** Maintain a healthy lifestyle!")
    elif 25 <= bmi < 29.9:
        st.warning("🟠 **You are overweight.** Consider a balanced diet and exercise.")
    else:
        st.error("🔴 **You are in the obesity range.** Consult a healthcare professional.")

    # **BMI Chart**
    bmi_chart = pd.DataFrame({
        "BMI Category": ["Underweight", "Normal", "Overweight", "Obese"],
        "BMI Range": ["< 18.5", "18.5 - 24.9", "25 - 29.9", "30+"],
        "Color": ["🔵", "✅", "🟠", "🔴"]
    })
    st.table(bmi_chart)

    # **Plot BMI Chart**
    fig, ax = plt.subplots()
    categories = ["Underweight", "Normal", "Overweight", "Obese"]
    bmi_values = [18.4, 24.9, 29.9, 35]
    ax.barh(categories, bmi_values, color=["blue", "green", "orange", "red"])
    ax.axvline(x=bmi, color='black', linestyle='dashed', label=f'Your BMI: {bmi:.2f}')
    ax.set_xlabel("BMI")
    ax.set_title("BMI Classification")
    st.pyplot(fig)

else:
    st.warning("⚠️ Please enter valid weight and height.")

# =========================
# **Interest Calculator**
# =========================
import streamlit as st
from components.header3 import load_interest_header3 # Import the header function

# Load Header
load_interest_header3()
st.write("### Interest Calculator")
principal = st.number_input("Principal Amount", min_value=0.0, step=0.01)
rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, step=0.01)
time = st.number_input("Time (years)", min_value=0.0, step=0.1)

if principal > 0 and rate > 0 and time > 0:
    simple_interest = principal * (1 + (rate / 100) * time)  # Simple Interest
    compound_interest = principal * (1 + rate / 100) ** time  # Compound Interest
    
    st.success(f"**Total (Simple Interest):** {simple_interest:.2f}")
    st.success(f"**Total (Compound Interest):** {compound_interest:.2f}")
elif principal > 0 or rate > 0 or time > 0:
    st.warning("⚠️ Please enter values greater than 0 for all fields.")

# -*- coding: utf-8 -*-
import streamlit as st
from components.header4 import load_help_header4  # Import the header function

# Load Header
load_help_header4()
# Load custom CSS
with open(".streamlit/assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Page Title

st.write("Find answers to your questions.")

# How to Use the Unit Converter
st.write("## How to Use the Unit Converter")
st.markdown("""
1. **Select a category** from the sidebar (Length, Weight, Temperature, etc.).
2. **Enter a value** that you want to convert.
3. **Choose the 'From' and 'To' units** from the dropdown menus.
4. **Click 'Convert'** to get the result instantly.
5. If you encounter any issues, check the **FAQs** below.
""")

# FAQs Section
st.write("## FAQs")
faq_list = [
    ("How do I convert currency?", "Select the 'Currency' category and choose the currencies to convert between."),
    ("Why do I see an error when converting units?", "Ensure you have selected the correct category and units."),
    ("How do I calculate my BMI?", "Go to the 'Calculators' page, enter your weight and height, and view your BMI."),
    ("Does this tool require an internet connection?", "Most conversions work offline, but currency conversion requires an active internet connection."),
    ("Can I report an issue or request a feature?", "Yes! Please contact support via the 'Contact Us' section.")
]

for question, answer in faq_list:
    st.write(f"**Q: {question}**")
    st.write(f"A: {answer}")

# Contact Us Section
st.write("## Contact Us")
st.markdown("""
If you need further assistance, please reach out to us:
- **Email:** support@unitconverter.com
- **GitHub Issues:** [Report a Bug](https://github.com/yourrepo/issues)
- **Live Chat:** Available Mon-Fri (9 AM - 5 PM)
""")


# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
from components.header5 import load_common_unit_header # Import the header function

# Load Header
load_common_unit_header()
def main():
    
    
    st.write("Explore commonly used unit systems.")

    st.markdown("""
    A unit system, or system of measurement, is a system comprised of interrelated units of measurement.
    Various unit systems have existed throughout history, and their importance remains evident today.
    """)
    
    st.header("The Three Common Unit Systems")
    st.markdown("""
    The three common unit systems that are in use today are:
    - **The International System of Units (SI)**
    - **United States customary units (UCS)**
    - **The Imperial system of units**
    """)
    
    st.subheader("International System of Units (SI)")
    st.write("The International System of Units (SI) is the modern form of the metric system and consists of seven base units.")
    
    st.markdown("### SI Base Units:")
    si_base_units = {
        "Unit": ["ampere", "kelvin", "second", "meter", "kilogram", "candela", "mole"],
        "Symbol": ["A", "K", "s", "m", "kg", "cd", "mol"],
        "Measurement": ["Electric current", "Temperature", "Time", "Length", "Mass", "Luminous intensity", "Amount of substance"]
    }
    st.table(pd.DataFrame(si_base_units))
    
    st.markdown("### Metric Prefixes:")
    metric_prefixes = {
        "Prefix": ["exa", "peta", "tera", "giga", "mega", "kilo", "hecto", "deca", "deci", "centi", "milli", "micro", "nano", "pico", "femto", "atto"],
        "Symbol": ["E", "P", "T", "G", "M", "k", "h", "da", "d", "c", "m", "μ", "n", "p", "f", "a"],
        "Factor": ["10^18", "10^15", "10^12", "10^9", "10^6", "10^3", "10^2", "10^1", "10^-1", "10^-2", "10^-3", "10^-6", "10^-9", "10^-12", "10^-15", "10^-18"]
    }
    st.table(pd.DataFrame(metric_prefixes))
    
    st.markdown("### SI-Derived Units:")
    si_derived_units = {
        "Unit": ["radian", "newton", "watt", "volt", "degree Celsius"],
        "Symbol": ["rad", "N", "W", "V", "°C"],
        "Measurement": ["Angle", "Force or weight", "Power", "Voltage", "Temperature"]
    }
    st.table(pd.DataFrame(si_derived_units))
    
    st.markdown("### Non-SI Units Accepted for Use with SI:")
    non_si_units = {
        "Unit": ["minute", "hour", "day", "liter", "bar", "millimeter of mercury"],
        "Symbol": ["min", "h", "d", "L", "bar", "mmHg"],
        "Measurement": ["Time", "Time", "Time", "Volume", "Pressure", "Pressure"]
    }
    st.table(pd.DataFrame(non_si_units))
    
    st.subheader("United States Customary Units (UCS)")
    st.write("United States customary units (UCS) are a system of measurements used in the United States.")
    
    st.subheader("The Imperial System of Units")
    st.write("The imperial system is a system of weights and measures that was officially used in the UK and other countries.")
    
    st.info("More details on UCS and the Imperial system will be provided in future updates.")

if __name__ == "__main__":
    main()



# Footer
st.markdown("---")
st.write("© 2025 Calculators. All rights reserved.")





