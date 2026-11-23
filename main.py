
import streamlit as st

# ============================
# 🎨 GLOBAL THEME CONTROLLER
# ============================

with st.sidebar:
    st.header("🎛 Theme Controller")

    theme = st.selectbox(
        "Choose a theme:",
        ["Default", "Light", "Dark", "Ocean Blue", "Forest Green", "Custom Color"]
    )

    if theme == "Light":
        bg = "#FFFFFF"
        text = "black"

    elif theme == "Dark":
        bg = "#000000"
        text = "white"

    elif theme == "Ocean Blue":
        bg = "#D0E8FF"
        text = "black"

    elif theme == "Forest Green":
        bg = "#DFFFE0"
        text = "black"

    elif theme == "Custom Color":
        bg = st.color_picker("Pick a background color", "#F5F5F5")
        text = "black"

    else:
        bg = "#F5F5F5"
        text = "black"

# ============================
# FIXED CSS — THIS MAKES BACKGROUND CHANGE
# ============================

st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {bg} !important;
            color: {text} !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# ============================
# MAIN APP
# ============================

side = st.sidebar
with side:
    options = st.radio("Choose section:", ["Bmi", "Calculator"])

# -------------------- BMI SECTION --------------------
if options == "Bmi":
    tab1, tab2 = st.tabs(["Home 🏠", "Calculate Bmi 💪"])

    with tab2:

        st.set_page_config(page_title="BMI CALCULATOR 💪🏼")
        st.markdown("""
            <div style="background-color:#2E8B57;padding:20px;border-radius:10px;margin-bottom:20px;">
                <h1 style="color:white;text-align:center;">BMI Calculator</h1>
                <p style="color:white;text-align:center;">
                    Convert units, enter your measurements, and check your BMI instantly
                </p>
            </div>
        """, unsafe_allow_html=True)

        col_1, col_2 = st.columns(2)

        with col_1:
            options = st.selectbox("Convert:", {'feet', 'lbs'})
            number = st.number_input("Enter value:", label_visibility="collapsed")
            number = float(number)

        with col_2:
            options_2 = st.selectbox('To:', {'meters', 'kg'})

        if options == "feet" and options_2 == "meters":
            length = number * 0.3048
            st.write("Result", round(length, 3))

        if options == "lbs" and options_2 == "kg":
            weight = number * 0.45359237
            st.write("Result", round(weight, 3))

        gender = st.radio("Gender:", ["Male", "Female"])

        cols = st.columns(3)
        with cols[0]:
            Height = st.number_input("Enter height in m")
        with cols[1]:
            Weight = st.number_input("Enter weight in kg")
        with cols[2]:
            width = st.number_input(" Optional. Enter waist measurement.")

        btn_2 = st.button("Calculate")

        if Height and Weight :
            try:
                h = float(Height)
                w = float(Weight)
                bmi = w / (h ** 2)

                if btn_2==True:
                    st.write("BMI:", round(bmi, 2))

                    if bmi < 18.5:
                      st.write("UNDERWEIGHT")
                      st.write("Eat more")
                      st.write("Press this to learn more.")
                      st.markdown("https://www.healthline.com/nutrition/18-foods-to-gain-weight")
                
                    elif bmi>18.5 and bmi<24.9 and gender == "Male" and width < h / 2:
                      st.write("You are healthy")
                      st.markdown("Continue the good work 😂")
                    elif bmi>18.5 and bmi<24.9 and gender == "Female" and width < h / 2:   
                     st.write("You are healthy")
                     st.markdown("Continue the good work 😂")

                    elif bmi>24.9 and bmi<30:
                     st.write("OVERWEIGHT")

                    elif bmi >= 30 and gender == "Male" and width > 94:
                     st.write("OBESITY")
                     st.write("Your health is greatly at risk")
                     st.write("Lose a lot of weight, and reduce belly fat.")
                  
                    elif bmi >= 30 and gender=="Female" and width > 80:
                      st.write("Obesity")
                      st.write("Your health is greatly at risk.")
                      st.write("Lose a lot of weight, and reduce belly fat.")
                 
                    elif bmi >= 30:
                      st.write("Obesity")
                      st.write("Lose a lot of weight.")

                    bmi_rounded = round(bmi)
                    st.slider("BMI", min_value=10, max_value=40, value=bmi_rounded)

            except ValueError:
                st.error("Please enter valid numbers for height and weight.")

    with tab1:
      st.title("BMI")


# -------------------- CALCULATOR SECTION --------------------
if options == "Calculator":
    st.title("Calculator")
    try:
     x=eval(st.text_input("Enter numbers"))
     if x:
       st.write(x)
    except Exception as e:
        st.toast(e)
