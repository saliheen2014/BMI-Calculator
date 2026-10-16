import streamlit as st

# ============================
# 📄 PAGE CONFIGURATION (MUST BE FIRST)
# ============================
st.set_page_config(page_title="BMI CALCULATOR 💪🏼", layout="wide")

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

    with tab1:
        st.subheader("Welcome!")
        st.write("Use the next tab to calculate your Body Mass Index (BMI).")

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
            # FIX: Changed variable name from 'options' to 'unit_system' to prevent overriding the sidebar section menu
            unit_system = st.selectbox("Convert:", ["Metric (kg / cm)", "Imperial (lbs / inches)"])

        with col_2:
            if unit_system == "Metric (kg / cm)":
                weight = st.number_input("Weight (kg):",step=1)
                height = st.number_input("Height (m):",step=1)
                bmi = weight / ((height) ** 2) if height > 0 else 0
            else:
                weight = st.number_input("Weight (lbs):", min_value=1.0, value=150.0)
                height = st.number_input("Height (inches):", min_value=1.0, value=67.0)
                bmi = (weight / (height ** 2)) * 703 if height > 0 else 0

        if bmi > 0:
            st.metric(label="Your BMI", value=f"{bmi:.2f}")

# -------------------- CALCULATOR SECTION --------------------
elif options == "Calculator":
    st.header("🧮 Calculator Section")
    x=number_input("Enter number", value=0,step=1)
    if x !=0:
        st.write("Result: ",eval(x))

# -------------------- BACKGROUND COLOR SECTION --------------------
elif options == "Background Color":
    st.header("🎨 Background Color Section")
    st.write(f"The current active background color hex is: `{bg}`")

