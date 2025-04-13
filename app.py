import streamlit as st

def convert_Length(value:float, from_unit:str, to_unit:str):
    from_unit= from_unit.strip()
    to_unit= to_unit.strip()
    conversion_factors={
        'Meter':1,
        'Centimeter':100,
        'Kilometer':0.001,
        'Inch':39.3701,
        'Foot':3.28084,
        'Yard':1.09361,
        'Mile': 0.00621371
    }
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid unit")
    
    # from m
    if from_unit =="Meter" and to_unit=="Centimeter":
        return value * 100
    elif from_unit =="Meter" and to_unit=="Kilometer":
        return value / 1000
    elif from_unit =="Meter" and to_unit =="Yard":
        return value * 1.09361
    elif from_unit =="Meter" and to_unit =="Foot":
        return value *3.28084
    elif from_unit =="Meter" and to_unit=="Inch":
        return value * 39.3701
    elif from_unit=="Meter" and to_unit =="Mile":
        return value * 0.000621371
    
    # from cm
    elif from_unit=="Centimeter" and to_unit=="Meter":
        return value/ 100
    elif from_unit =="Centimeter" and to_unit =="Kilometer":
        return value/ 100000
    elif from_unit =="Centimeter" and to_unit =="Foot":
        return value/ 30.48
    elif from_unit =="Centimeter" and to_unit =="Yard":
        return value /91.44
    elif from_unit =="Centimeter" and to_unit =="Inch":
        return value / 2.54
    elif from_unit =="Centimeter" and to_unit =="Mile":
        return value * 160900
    
    # from km
    elif from_unit =="Kilometer" and to_unit =="Meter":
        return value * 1000
    elif from_unit =="Kilometer" and to_unit =="Centimeter":
        return value * 100000
    elif from_unit =="Kilometer" and to_unit =="Foot":
        return value *3280.84
    elif from_unit =="Kilometer" and to_unit =="Inch":
        return value *39370.1
    elif from_unit =="Kilometer" and to_unit =="Yard":
        return value *1094
    elif from_unit =="Kilometer" and to_unit=="Mile":
        return value /1.60934
    
    # from inch 
    elif from_unit=="Inch" and to_unit=="Centimeter":
        return value * 2.54
    elif from_unit =="Inch" and to_unit =="Meter":
        return value / 39.3701
    elif from_unit =="Inch" and to_unit =="Kilometer":
        return value /39370.1
    elif from_unit =="Inch" and to_unit=="Foot":
        return value /12
    elif from_unit =="Inch" and to_unit =="Yard":
        return value /36
    elif from_unit =="Inch" and to_unit=="Mile":
        return value /63360

    # from ft
    elif from_unit=="Foot" and to_unit=="Centimeter":
        return value * 30.48
    elif from_unit =="Foot" and to_unit=="Meter":
        return value /3.28084
    elif from_unit =="Foot" and to_unit =="Kilometer":
        return value /328.084
    elif from_unit =="Foot" and to_unit=="Inch":
        return value *12
    elif from_unit =="Foot" and to_unit =="Yard":
        return value /3
    elif from_unit =="Foot" and to_unit =="Mile":
        return value /5280
    
    # from yd
    elif from_unit =="Yard" and to_unit =="Centimeter":
        return value *91.44
    elif from_unit =="Yard" and to_unit =="Meter":
        return value * 1.09361
    elif from_unit =="Yard" and to_unit=="Kilometer":
        return value /1094
    elif from_unit =="Yard" and to_unit =="Inch":
        return value* 36
    elif from_unit =="Yard" and to_unit =="Foot":
        return value *3
    elif from_unit =="Yard" and to_unit =="Mile":
        return value /1760
   
    # from mile
    elif from_unit =="Mile" and to_unit=="Centimeter":
        return value *160900
    elif from_unit =="Mile" and to_unit=="Meter":
        return value *1609.34
    elif from_unit =="Mile" and to_unit =="Kilometer":
        return value *1.60934
    elif from_unit =="Mile" and to_unit=="Inch":
        return value *63360
    elif from_unit =="Mile" and to_unit =="Yard":
        return value *1760
    elif from_unit =="Mile" and to_unit =="Foot":
        return value *5280




def convert_Mass(value:float,from_unit:str, to_unit:str):
    from_unit= from_unit.strip()
    to_unit= to_unit.strip()
  #From Gram
    if from_unit== "Gram" and to_unit=="Kilogram":
        return value/1000
    elif from_unit =="Gram" and to_unit=="Miligram":
        return value*1000
    elif from_unit=="Gram" and to_unit=="Pound":
        return value/453.592
    elif from_unit=="Gram" and to_unit=="Ounce":
        return value/28.3495
     
  # From kilogram
    elif from_unit=="Kilogram" and to_unit=="Gram":
        return value*1000
    elif from_unit=="Kilogram" and to_unit=="Miligram":
        return value*1000000
    elif from_unit =="Kilogram" and to_unit=="Pound":
        return value*2.20462
    elif from_unit=="Kilogram" and to_unit=="Ounce":
        return value*35.274
    
   # From Miligram
    elif from_unit=="Miligram" and to_unit=="Gram":
        return value /1000
    elif from_unit=="Miligram" and to_unit=="Kilogram":
        return value/1000000
    elif from_unit=="Miligram" and to_unit=="Pound":
        return value/453600
    elif from_unit=="Miligram" and to_unit=="Ounce":
        return value/28349.5
    
    # From Pound
    elif from_unit =="Pound" and to_unit=="Gram":
        return value *453.592
    elif from_unit =="Pound" and to_unit=="Kilogram":
        return value /2.20462
    elif from_unit=="Pound" and to_unit=="Miligram":
        return value *453600
    elif from_unit =="Pound" and to_unit =="Ounce":
        return value *16
    
    #From Ounce 
    elif from_unit=="Ounce" and to_unit=="Gram":
        return value*28.3495
    elif from_unit=="Ounce" and to_unit =="Kilogram":
        return value /35.274
    elif from_unit =="Ounce" and to_unit=="Miligram":
        return value *28349.5
    elif from_unit=="Ounce" and to_unit=="Pound":
        return value/16
    
def convert_Time(value:float, from_unit:str, to_unit:str):
    from_unit =from_unit.strip()
    to_unit= to_unit.strip()

# From Second
    if from_unit=="Second" and to_unit=="Minute":
        return value /60
    elif from_unit =="Second" and to_unit =="Hour":
        return value /3600
    elif from_unit =="Second" and to_unit =="Day":
        return value /86400
    elif from_unit =="Second" and to_unit =="Week":
        return value /604800
    
# From Minute
    elif from_unit =="Minute" and to_unit =="Second":
        return value *60
    elif from_unit =="Minute" and to_unit =="Hour":
        return value /60
    elif from_unit =="Minute" and to_unit =="Day":
        return value /1440
    elif from_unit =="Minute" and to_unit=="Week":
        return value /10080
    
# From Hour
    elif from_unit =="Hour" and to_unit =="Second":
        return value *3600
    elif from_unit =="Hour" and to_unit =="Minute":
        return value *60
    elif from_unit =="Hour" and to_unit =="Day":
        return value /24
    elif from_unit =="Hour" and to_unit =="Week":
        return value /168
    

    #From Day
    elif from_unit =="Day" and to_unit == "Second":
        return value *86400
    elif from_unit =="Day" and to_unit =="Minute":
        return value *1440
    elif from_unit =="Day" and to_unit =="Hour":
        return value *24
    elif from_unit == "Day " and to_unit =="Week":
        return value/7
    

    #From Week
    elif from_unit =="Week" and to_unit =="Second":
        return value *604800
    elif from_unit =="Week" and to_unit =="Minute":
        return value *10080
    elif from_unit =="Week" and to_unit =="Hour":
        return value *168
    elif from_unit =="Week" and to_unit=="Day":
        return value *7
    elif from_unit=="Week" and to_unit =="Month":
        return value /4.34524


def convert_temperature(value:float, from_unit:str, to_unit:str):
    from_unit =from_unit.strip()
    to_unit= to_unit.strip()
#from Celsius
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
    elif from_unit=="Celsius" and to_unit == "Kelvin":
            return value + 273.15
# From Fahrenheit
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
    elif from_unit== "Farenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
# From Kelvin
    elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
    elif from_unit=="Kelvin"and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32

def main():
    st.title("Unit Convertor")
    st.header("Welcome to the Unit Convertor!")
    category = st.selectbox("Select Category", ["Length", "Mass", "Time", "Temperature"])

    if category =="Length":
     st.subheader("📏Length Conversion!")
   
     value=st.number_input("Enter a number:",min_value=0.00)
     from_unit=st.selectbox("From Unit",["Meter","Centimeter","Kilometer","Inch","Foot","Yard","Mile"])
     to_unit=st.selectbox("To Unit",["Meter","Centimeter","Kilometer","Inch","Foot","Yard","Mile"])
     if st.button("Convert"):
        result=convert_Length(value,from_unit,to_unit)
        st.success(f"({value} {from_unit}) = ({result}{to_unit})")
        st.write("Your converted value is:", result)
        st.button("Reset")
        result=0.00
     else:
        st.info("Click the button to convert the unit")

    elif category=="Mass":
     st.subheader("⚖️ Mass Conversion!")
    
     value=st.number_input("Enter a number:",min_value=0.00)
     from_unit=st.selectbox("From Unit",["Gram","Kilogram","MiliGram","Pound","Ounce"])
     to_unit=st.selectbox("To Unit",["Gram","Kilogram","MiliGram","Pound","Ounce"])
     if st.button("Convert"):
        result=convert_Mass(value,from_unit,to_unit)
        st.success(f"({value} {from_unit}) = ({result}{to_unit})")
        st.write("Your converted value is:", result)
        st.button("Reset")
        result=0.00
     else:
        st.info("Click the button to convert the unit")

    elif category=="Time":
     st.subheader("⏰Time Conversion!")
     value=st.number_input("Enter a number:",min_value=0.00)
     from_unit=st.selectbox("From Unit",["Second","Minute","Hour","Day","Week"])
     to_unit=st.selectbox("To Unit",["Second","Minute","Hour","Day","Week"])
     if st.button("Convert"):
        result=convert_Time(value,from_unit,to_unit)
        st.success(f"({value} {from_unit}) = ({result}{to_unit})")
        st.write("Your converted value is:", result)
        st.button("Reset")
        result=0.00
     else:
        st.info("Click the button to convert the unit")
    elif category=="Temperature":
     st.subheader(" 🌡️Temperature Conversion!")
     value=st.number_input("Enter a number:",min_value=0.00)
     from_unit=st.selectbox("From Unit",["Celsius","Fahrenheit","Kelvin"])
     to_unit=st.selectbox("To Unit",["Celsius","Fahrenheit","Kelvin"])
     if st.button("Convert"):
        result=convert_temperature(value,from_unit,to_unit)
        st.success(f"({value} {from_unit}) = ({result}{to_unit})")
        st.write("Your converted value is:", result)
        st.button("Reset")
        result=0.00
     else:
        st.info("Click the button to convert the unit")




    
    
if __name__ == "__main__":
    main()
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://i.pinimg.com/736x/ae/0c/60/ae0c604b76f71e7551ad21bea3a8f52e.jpg");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
