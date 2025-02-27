import streamlit as st
import pandas as pd

def length_conversion(value, from_unit, to_unit):
    length_units = {
        'Kilometer': 1000,
        'Meter': 1,
        'Centimeter': 0.01,
        'Millimeter': 0.001,
        'Mile': 1609.34,
        'Yard': 0.9144,
        'Foot': 0.3048,
        'Inch': 0.0254
    }
    return value * length_units[from_unit] / length_units[to_unit]

def weight_conversion(value, from_unit, to_unit):
    weight_units = {
        'Tonne': 1000,
        'Kilogram': 1,
        'Gram': 0.001,
        'Milligram': 0.000001,
        'Pound': 0.453592,
        'Ounce': 0.0283495
    }
    return value * weight_units[from_unit] / weight_units[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        return (value * 9/5) + 32 if to_unit == 'Fahrenheit' else value + 273.15
    elif from_unit == 'Fahrenheit':
        return (value - 32) * 5/9 if to_unit == 'Celsius' else (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        return value - 273.15 if to_unit == 'Celsius' else (value - 273.15) * 9/5 + 32
    return value

def area_conversion(value, from_unit, to_unit):
    area_units = {
        'Square Kilometer': 1000000,
        'Square Meter': 1,
        'Square Mile': 2589988.11,
        'Square Yard': 0.836127,
        'Square Foot': 0.092903,
        'Square Inch': 0.00064516,
        'Hectare': 10000,
        'Acre': 4046.86
    }
    return value * area_units[from_unit] / area_units[to_unit]

def volume_conversion(value, from_unit, to_unit):
    volume_units = {
        'Cubic Meter': 1,
        'Cubic Centimeter': 0.000001,
        'Liter': 0.001,
        'Milliliter': 0.000001,
        'Gallon (US)': 0.00378541,
        'Quart (US)': 0.000946353,
        'Pint (US)': 0.000473176,
        'Cup (US)': 0.000236588
    }
    return value * volume_units[from_unit] / volume_units[to_unit]

def main():
    st.set_page_config(page_title="Universal Unit Converter", page_icon="🔄", layout="centered")
    
    st.markdown("""
        <style>
            .title {text-align: center; font-size: 32px; color: #2E86C1;}
            .footer {text-align: center; margin-top: 20px; color: #555;}
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 class='title'>🔄 Universal Unit Converter</h1>", unsafe_allow_html=True)
    st.write("Easily convert between different units of Length, Weight, Temperature, Area, and Volume.")
    
    conversion_types = {
        'Length': ['Kilometer', 'Meter', 'Centimeter', 'Millimeter', 'Mile', 'Yard', 'Foot', 'Inch'],
        'Weight': ['Tonne', 'Kilogram', 'Gram', 'Milligram', 'Pound', 'Ounce'],
        'Temperature': ['Celsius', 'Fahrenheit', 'Kelvin'],
        'Area': ['Square Kilometer', 'Square Meter', 'Square Mile', 'Square Yard', 'Square Foot', 'Square Inch', 'Hectare', 'Acre'],
        'Volume': ['Cubic Meter', 'Cubic Centimeter', 'Liter', 'Milliliter', 'Gallon (US)', 'Quart (US)', 'Pint (US)', 'Cup (US)']
    }
    
    conversion_type = st.selectbox('Select Conversion Type', list(conversion_types.keys()))
    units = conversion_types[conversion_type]
    
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox('From Unit', units)
    with col2:
        to_unit = st.selectbox('To Unit', units)
        
    value = st.number_input(f'Enter value in {from_unit}', value=1.0)
    
    if conversion_type == 'Length':
        result = length_conversion(value, from_unit, to_unit)
    elif conversion_type == 'Weight':
        result = weight_conversion(value, from_unit, to_unit)
    elif conversion_type == 'Temperature':
        result = temperature_conversion(value, from_unit, to_unit)
    elif conversion_type == 'Area':
        result = area_conversion(value, from_unit, to_unit)
    elif conversion_type == 'Volume':
        result = volume_conversion(value, from_unit, to_unit)
    
    st.success(f'{value} {from_unit} = {result:.6g} {to_unit}')
    
    st.markdown("<div class='footer'> Created by Waqar Ahmed</div>", unsafe_allow_html=True)
    
    with st.expander("ℹ️ About this converter"):
        st.write("""
        This universal unit converter supports various conversion types:
        - **Length** (e.g., meters to feet)
        - **Weight** (e.g., kilograms to pounds)
        - **Temperature** (e.g., Celsius to Fahrenheit)
        - **Area** (e.g., square meters to acres)
        - **Volume** (e.g., liters to gallons)
        
        All conversions are based on standard conversion factors.
        """)

if __name__ == "__main__":
    main()
