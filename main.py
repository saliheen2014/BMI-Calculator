import streamlit as st
st.write("BMI Calculator")

Height=st.text_input("Enter height in m")
Weight=st.text_input("Enter weight in kg")

if Height and Weight:  # Only calculate when both fields are filled
    try:
        h = float(Weight)
        w = float(Height)
        bmi = h / (w ** 2)
        st.write("BMI:", bmi)
    except ValueError:
        st.error("Please enter valid numbers for height and weight.")
    if bmi<18.5:
        st.write("UNDERWEIGHT")
        st.write("Eat more")
    if bmi>24.9<30:
        st.write("OVERWEIGHT")  
    if bmi>30:
        st.write("OBESITY")
    if bmi>18.5<24.9:
            st.write(name, " you are healthy")
            st.markdown("Continue the good work:joy:")
    bmi=round(bmi)
    slider=st.slider("bmi",min_value=10,max_value=40,value=bmi)

    
