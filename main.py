
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
    options = st.radio("Choose section:", ["Bmi", "Calculator", "Background Color"])

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
    st.markdown("""
        <div style="background-color:#4CAF50;padding:20px;border-radius:10px;">
            <h1 style="color:white;text-align:center;">BMI & Health Checker</h1>
            <p style="color:white;text-align:center;">Track your BMI, waist measurement, and overall health</p>
        </div>
    """, unsafe_allow_html=True)

    st.title("What’s your Body Mass Index (BMI)?")
    st.header("Are you within a healthy weight range for your height?")

    st.markdown("""
    BMI is calculated using your weight and height (your weight divided by your height squared).
    Along with other factors like blood pressure and cholesterol, BMI helps estimate your risk of heart disease, stroke, and diabetes.
    """)

    st.subheader("How to Calculate BMI")
    st.markdown("""
    The Body Mass Index is a quick screening tool that relates your weight to your height.
    While it doesn’t measure body fat directly, it’s widely used by healthcare professionals. 
    To calculate BMI, this is the formula that we use, Weight/height**2 
    """)

    st.subheader("Waist Measurement")
    st.markdown("""
    Waist measurement is also important. It helps assess how much fat is carried around your abdomen — a major risk factor for heart disease.
    """)

    st.subheader("How to Measure Your Waist")
    st.markdown("""
    • Find the top of your hip bone and the bottom of your ribs  
    • Breathe out normally  
    • Place the tape measure midway between these points  
    • Wrap it around your waist (loose enough for one finger)  
    • Read your measurement  
    """)

    st.markdown("""
    Health Significance
    Waist circumference reflects abdominal fat, including visceral fat, which surrounds internal organs and is metabolically active. High levels of visceral fat are linked to:

    -Increased risk of type 2 diabetes  
    -High blood pressure  
    -High cholesterol  
    -Heart disease  
    -Fatty liver disease  
   

    Even individuals with a normal BMI can have elevated health risks if their waist circumference is high. 
    """)

    st.markdown("""
    Healthy Waist Guidelines
    While exact healthy waist sizes vary by sex, height, and ethnicity, general guidelines include:

    Men: Waist circumference below 40 inches (102 cm) is considered lower risk  
    Women: Waist circumference below 35 inches (88 cm) is considered lower risk  

    Another useful metric is the waist-to-height ratio (WHtR): keeping your waist less than half your height (ratio under 0.50) is associated with lower health risks.
    """)


# -------------------- CALCULATOR SECTION --------------------
if options == "Calculator":

    x=eval(st.text_input("Enter numbers"))
    if x:
       st.write(x)
