import streamlit as st
tab1,tab2=st.tabs(["Bmi Calculator","Calculator"])

with tab1:
 st.title("BMI Calculator")
 col_1,col_2,=st.columns(2)
 with col_1:
    options=st.selectbox("Convert:",
                     {'feet','lbs'})
    number=st.number_input("") 
    number=float(number)
    
 with col_2:
    options_2=st.selectbox('To:',
                           {'meters','kg',})
     

 if options=="feet" and options_2=="meters":
    length=number*0.3048
    answer=st.write("Result",round(length,3))

 if options=="lbs" and options_2=="kg":
    weight=number*0.45359237
    st.write("Result",round(weight,3))  
    


 Height = st.number_input("Enter height in m")
 Weight = st.number_input("Enter weight in kg")
 btn_2=st.button("Calculate") 
 if Height and Weight:
    try:
        h = float(Height)
        w = float(Weight)
        bmi = w / (h ** 2)

        if btn_2==True:
         st.write("BMI:", round(bmi, 2))

        if bmi < 18.5:
            st.write("UNDERWEIGHT")
            st.write("Eat more")

        elif 18.5 <= bmi <= 24.9:
            st.write( "You are healthy")
            st.markdown("Continue the good work 😂")

        elif 25 <= bmi <= 29.9:
            st.write("OVERWEIGHT")

        elif bmi >= 30:
            st.write("OBESITY")

        bmi_rounded = round(bmi)
        st.slider("BMI", min_value=10, max_value=40, value=bmi_rounded)

    except ValueError:
        st.error("Please enter valid numbers for height and weight.")
with tab2:
   st.title("Calculator")
   

   Numbers=st.columns(2)
   with Numbers[0]:
      first_number=st.number_input("First number")
      second_number=st.number_input("Second number")
      
   with Numbers[1]:
      button_addition=st.button("+")
      button_subtraction=st.button("-")
      button_division=st.button("/")
      button_multiplication=st.button("*")
      
   if button_addition==True:
      st.write("Result:",float(first_number)+float(second_number)) 
   if button_subtraction==True:
      st.write("Result:",float(first_number)-float(second_number))
   if button_division==True:
      st.write("Result:",float(first_number)/float(second_number)) 
   if button_multiplication==True:
      st.write("Result:",float(first_number)*float(second_number))
   

