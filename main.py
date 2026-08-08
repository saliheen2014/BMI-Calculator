import streamlit as st

side = st.sidebar
with side:
    options = st.radio(" ", ["Bmi", "Calculator","Background Color"])

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

        st.markdown("""
        <style>
        body {
            background-color: #f5f5f5;
        }
        </style>
        """, unsafe_allow_html=True)

        col_1, col_2 = st.columns(2)

        with col_1:
            options = st.selectbox("Convert:",
                                   {'feet', 'lbs'})
            number = st.number_input("")
            number = float(number)

        with col_2:
            options_2 = st.selectbox('To:',
                                     {'meters', 'kg'})

        if options == "feet" and options_2 == "meters":
            length = number * 0.3048
            answer = st.write("Result", round(length, 3))

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
            width = st.number_input("Enter waist measurement.")

        btn_2 = st.button("Calculate")

        if Height and Weight:
            try:
                h = float(Height)
                w = float(Weight)
                bmi = w / (h ** 2)

                if btn_2 == True:
                    st.write("BMI:", round(bmi, 2))

                if bmi < 18.5:
                    st.write("UNDERWEIGHT")
                    st.write("Eat more")

                elif 18.5 <= bmi <= 24.9 and gender == "male" and width < h / 2:
                    st.write("You are healthy")
                    st.markdown("Continue the good work 😂")

                elif 25 <= bmi <= 29.9:
                    st.write("OVERWEIGHT")

                elif bmi >= 30 and gender == "Male" and width > 94:
                    st.write("OBESITY")
                    st.write("Your health is greatly at risk")
                    st.write("Lose a lot of weight, and reduce belly fat.")

                elif bmi >= 30 and gender == "Female" and width > 80:
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

        st.markdown("""
        <style>
        body {
            background-color: #f5f5f5;
        }
        </style>
        """, unsafe_allow_html=True)

        st.title("What’s your Body Mass Index (BMI)?")
        st.header("Are you within a healthy weight range for your height?")

        st.markdown("""
        BMI is calculated using your weight and height (your weight divided by your height squared).
        Along with several other factors, like your blood pressure and cholesterol, BMI can help estimate your risk of a heart attack or stroke.
        """)

        st.subheader("How to Calculate BMI?")
        st.markdown("""
        The Body Mass Index is a quick and simple screening tool that relates your weight to your height. 
        While it has limitations and doesn’t measure body fat directly, it’s often used by healthcare professionals to broadly categorize a person’s weight and potential health risks.
        You can calculate BMI using either the Metric System or the Imperial System (US Units).
        """)

        st.subheader("Metric BMI Formula")
        st.markdown("""
        The metric formula is the standard way to calculate BMI: Weight/height/square. It is the formula that we use.
        """)

        st.header("Waist Measurement")
        st.markdown("""
        Waist measurement (waist circumference) is also important to consider alongside your BMI.
        Waist measurement can help to assess risk by measuring the amount of fat carried around your middle.
        """)

        st.subheader("How to Measure your Waist")
        st.markdown("""
        Find the top of your hip bone and the bottom of your ribs. 
        Breathe out normally.
        Place the tape measure midway between these points, in line with your belly button, and wrap it around your waist loose enough to fit one finger inside the tape.
        Check your measurement.
        """)

        st.markdown("""
        Health Significance  
        Waist circumference reflects abdominal fat, including visceral fat, which surrounds internal organs and is metabolically active. High levels of visceral fat are linked to:

        - Increased risk of type 2 diabetes  
        - High blood pressure  
        - High cholesterol  
        - Heart disease  
        - Fatty liver disease  

        Even individuals with a normal BMI can have elevated health risks if their waist circumference is high.
        """)

        st.markdown("""
        Healthy Waist Guidelines  
        Men: Waist circumference below 40 inches (102 cm)  
        Women: Waist circumference below 35 inches (88 cm)  

        Waist-to-height ratio (WHtR): keeping your waist less than half your height (ratio under 0.50) is associated with lower health risks.
        """)

if options == "Calculator":

    st.set_page_config(page_title="Calculator 📅")
    st.title("Calculator 📅")

    st.subheader("Basic Operations")
    st.write("Type number then press operator.")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        first_number = st.number_input("First number", value=0.0)
        second_number = st.number_input("Second number", value=0.0)
        button_square = st.button("Square (x²)")

    with col2:
        button_addition = st.button("+")
        button_subtraction = st.button("-")
        button_division = st.button("/")
        button_multiplication = st.button("*")

    with col3:
        button_cube = st.button("Cube (x³)")
        button_pi = st.button("x × π")

    if button_addition:
        st.success(f"Result: {first_number + second_number}")

    if button_subtraction:
        st.success(f"Result: {first_number - second_number}")

    if button_division:
        if second_number == 0:
            st.error("Cannot divide by zero.")
        else:
            st.success(f"Result: {first_number / second_number}")

    if button_multiplication:
        st.success(f"Result: {first_number * second_number}")

    if button_square:
        st.success(f"Result: {first_number ** 2}")

    if button_cube:
        st.success(f"Result: {first_number ** 3}")

    if button_pi:
        st.success(f"Result: {first_number * 3.1415926535}")
if options=="Background Color":


# ============================
# 🎨 GLOBAL THEME CONTROLLER
# ============================


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

# Apply theme globally
st.markdown(
    f"""
    <style>
        body {{
            background-color: {bg};
            color: {text};
        }}
    </style>
    """,
    unsafe_allow_html=True
)
