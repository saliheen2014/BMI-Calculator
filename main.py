import streamlit as st

# ============================
# 📄 PAGE CONFIGURATION (MUST BE FIRST)
# ============================
st.set_page_config(page_title="Multi-Tool App 💪🏼", layout="wide")

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
        bg = "#121212"
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

# Inject Custom CSS Theme
st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {bg} !important;
            color: {text} !important;
        }}
        /* Ensures sidebar elements remain readable */
        .css-1d391kg, [data-testid="stSidebar"] {{
            background-color: rgba(0, 0, 0, 0.05);
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# ============================
# NAVIGATION MENU
# ============================
# Changed variable name to 'nav_selection' to prevent overwriting 'options' later
nav_selection = st.sidebar.radio("Choose section:", ["Bmi", "Calculator", "Background Color"])

# -------------------- BMI SECTION --------------------
if nav_selection == "Bmi":
    tab1, tab2 = st.tabs(["Home 🏠", "Calculate Bmi 💪"])

    with tab1:
        st.subheader("Welcome to the Health Portal")
        st.write("Body Mass Index (BMI) is a rough estimate of healthy body weight based on height and weight.")

    with tab2:
        st.markdown("""
            <div style="background-color:#2E8B57;padding:20px;border-radius:10px;margin-bottom:20px;">
                <h1 style="color:white;text-align:center;margin:0;">BMI Calculator</h1>
                <p style="color:white;text-align:center;margin:5px 0 0 0;">
                    Convert units, enter your measurements, and check your BMI instantly
                </p>
            </div>
        """, unsafe_allow_html=True)

        col_1, col_2 = st.columns(2)

        with col_1:
            unit_system = st.selectbox("Choose System:", ["Metric (kg / cm)", "Imperial (lbs / inches)"])

        with col_2:
            if unit_system == "Metric (kg / cm)":
                weight = st.number_input("Weight (kg):", min_value=1.0, value=70.0, step=0.1)
                height = st.number_input("Height (cm):", min_value=1.0, value=170.0, step=1.0)
                
                if height > 0:
                    bmi = weight / ((height / 100) ** 2)
                else:
                    bmi = 0
            else:
                weight = st.number_input("Weight (lbs):", min_value=1.0, value=150.0, step=0.1)
                height = st.number_input("Height (inches):", min_value=1.0, value=67.0, step=1.0)
                
                if height > 0:
                    bmi = (weight / (height ** 2)) * 703
                else:
                    bmi = 0

        if bmi > 0:
            st.metric(label="Your BMI", value=f"{bmi:.2f}")
            
            # BMI Status Breakdown
            if bmi < 18.5:
                st.warning("Category: Underweight")
            elif 18.5 <= bmi < 25.0:
                st.success("Category: Normal weight")
            elif 25.0 <= bmi < 30.0:
                st.warning("Category: Overweight")
            else:
                st.error("Category: Obesity")

# -------------------- CALCULATOR SECTION --------------------
elif nav_selection == "Calculator":
    st.header("🧮 Math Calculator")
    
    calc_col1, calc_col2, calc_col3 = st.columns(3)
    with calc_col1:
        num1 = st.number_input("First Number:", value=0.0)
    with calc_col2:
        operation = st.selectbox("Operation:", ["+", "-", "*", "/"])
    with calc_col3:
        num2 = st.number_input("Second Number:", value=0.0)
        
    if st.button("Calculate"):
        if operation == "+":
            st.success(f"Result: {num1 + num2}")
        elif operation == "-":
            st.success(f"Result: {num1 - num2}")
        elif operation == "*":
            st.success(f"Result: {num1 * num2}")
        elif operation == "/":
            if num2 != 0:
                st.success(f"Result: {num1 / num2}")
            else:
                st.error("Cannot divide by zero!")

# -------------------- BACKGROUND COLOR SECTION --------------------
elif nav_selection == "Background Color":
    st.header("🎨 Active Theme Details")
    st.write(f"The current active background color hex is: `{bg}`")
    st.write(f"The text color context is set to: `{text}`")




       




    



              
                
