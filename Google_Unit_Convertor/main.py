import streamlit as st


st.set_page_config(page_title="Unit Convertor" , layout="wide")


# conversion dictionary
conversion_dict = {
    "Length" : {
        "meter" : 1,
        "kilometer" : 0.001,
        "centimeter" : 100,
        "millimeter" : 1000,
        "inch" : 39.37,
        "yard" : 1.0936,
        "foot" : 3.2808,
        "mile" : 0.00062137,
    },
    "Weight" : {
        "kilogram" : 1,
        "gram" : 0.001,
        "milligram" : 1000,
        "ounce" : 0.035274,

    },

    "Volume" : {
        "liter" : 1,
        "milliliter" : 0.001,
        "gallon" : 0.264172,
        "quart" : 0.00946353,
        "pint" : 0.00473176,
        "cup" : 0.00236588,
        "teaspoon" : 0.0000558139,
        "tablespoon" : 0.0000191304,
    },
    "Time": {
        "second": 1, 
        "minute": 1/60, 
        "hour": 1/3600, 
        "day": 1/86400
    },
    "Speed":{
        "meter/second": 1, 
        "kilometer/hour": 3.6,
        "mile/hour": 2.23694, 
        "foot/second": 3.28084,
    },
}


    



# Function to convert units based on the given category  and conversion dictionary
def convert_unit(value , from_unit , to_unit):
    return value * conversion_dict[category][to_unit] / conversion_dict[category][from_unit]

# Main App
st.title("🔄Unit Convertor")
st.write('''Esily convert between different units 
          Just inpit the values and get the result instantly!''')


category = st.selectbox("Category", conversion_dict.keys())



col1 , col2 = st.columns(2)


with col1:

    from_unit = st.selectbox("🔄Convert From", conversion_dict[category].keys() )


    
with col2:

    to_unit = st.selectbox("➡Convert To", conversion_dict[category].keys())

value = st.number_input("Enter value to Convert" , value = 1 )

if st.button("Convert "):

    result = st.number_input("Converted Value" , value = convert_unit(value , from_unit , to_unit))

    st.success(f"{value} {from_unit} is equal to {result} {to_unit}")




