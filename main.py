import streamlit as st
import random
import time
import pandas as pd
import math
from streamlit_drawable_canvas import st_canvas



tab1, tab2, tab3, tab4 = st.tabs(["Math Quiz",  "More", "Slope", "Draw"])

# TAB 1 — MATH QUIZ
# ---------------------------------------------------------
with tab1:
    st.title("Math Quiz 📅")
    st.subheader("Challenge yourself and improve ⬆️.")
    




    # ---------------- TIMER ----------------
    

    # ---------------- QUIZ SETUP ----------------
    if "questions" not in st.session_state:
        st.session_state.questions = []
        st.session_state.correct = {}

    difficulty = st.slider("Difficulty", 10, 100, 1000, step=100)
    length = st.slider("Number of Questions", 5, 15, 5)
    operation = st.radio("Operation", ("Addition", "Subtraction", "Multiplication", "Division"))

    # Reset questions if settings change
    if (
        "old_diff" not in st.session_state
        or st.session_state.old_diff != difficulty
        or st.session_state.old_len != length
        or st.session_state.old_op != operation
    ):
        st.session_state.questions = []
        st.session_state.correct = {}

    st.session_state.old_diff = difficulty
    st.session_state.old_len = length
    st.session_state.old_op = operation

    # Generate questions
    if len(st.session_state.questions) == 0:
        for _ in range(length):
            num1 = random.randint(1, difficulty)
            num2 = random.randint(1, difficulty)
            st.session_state.questions.append((num1, num2))

    # ---------------- DISPLAY QUESTIONS ----------------
    st.subheader("Questions")

    for i, (num1, num2) in enumerate(st.session_state.questions):

        if operation == "Addition":
            answer = num1 + num2
            text = f"{num1} + {num2}"
        elif operation == "Subtraction":
            answer = num1 - num2
            text = f"{num1} - {num2}"
        elif operation == "Multiplication":
            answer = num1 * num2
            text = f"{num1} × {num2}"
        else:
            answer = num1 / num2
            text = f"{num1} ÷ {num2}"

        user_answer = st.number_input(f"Q{i+1}: {text}", key=f"ans{i}")

        if st.button(f"Submit q{i+1}", key=f"sub{i}"):
            st.session_state.correct[i] = (user_answer == answer)

        if i in st.session_state.correct:
            if st.session_state.correct[i]:
                st.success("Correct!")
            else:
                st.error("Wrong")

    # ---------------- FINAL RESULT ----------------
    if st.button("See Result"):
        if len(st.session_state.correct) < length:
            st.warning("You must answer all questions!")
        else:
            score = sum(st.session_state.correct.values())
            with st.spinner("Calculating..."):
                time.sleep(5)
            
                st.write(f"Your score: {score}/{length}")

                if score == length:
                 with st.spinner("Calculating..."):
                    time.sleep(5)

                    st.balloons()
                    st.success("Great Job! You scored 100%")
                else:
                 st.error("Try again!")

    # ---------------- RESTART QUIZ ----------------
    
    if st.button("🔄 Restart Quiz"):
        st.session_state.questions = []
        st.session_state.correct = {}
       
        st.session_state.old_diff = None
        st.session_state.old_len = None
        st.session_state.old_op = None

        for key in list(st.session_state.keys()):
            if key.startswith("ans") or key.startswith("sub"):
                del st.session_state[key]

        st.success("Quiz restarted!")
        st.rerun()

# ---------------------------------------------------------
# TAB 2 — GRAPHS
# ---------------------------------------------------------
with tab2:
    st.title("Graphs")

    picture = st.radio("Choose a graph:", ["Make a graph", "Canada Population"])

    if picture == "Canada Population":
        if st.button("Start"):
            placeholder = st.empty()
            placeholder.progress(0)
            time.sleep(1)
            placeholder.progress(50)
            time.sleep(1)
            placeholder.progress(100)
            time.sleep(1)

            st.header("Population of Canada from 2016")
            st.bar_chart([36110000, 36550000, 37070000, 37620000, 38030000, 38240000, 38950000, 40050000, 41260000, 41650000])
            table = {
                "Population": [36110000, 36550000, 37070000, 37620000, 38030000, 38240000, 38950000, 40050000, 41260000, 41650000],
                "Year": [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
            }
            
            st.dataframe(table)
            
    elif picture == "Make a graph":
        if st.button("Start"):
            placeholder = st.empty()
            placeholder.progress(0)
            time.sleep(1)
            placeholder.progress(50)
            time.sleep(1)
            placeholder.progress(100)
            time.sleep(1)

        plot1 = st.slider("Plot1", 50, 1000, 0)
        plot2 = st.slider("plot2", 50, 1000, 0)
        plot3 = st.slider("PLot3", 50, 1000, 0)
        plot4 = st.slider("PlOt4", 50, 1000, 0)

        st.line_chart({"data": [plot1, plot2, plot3, plot4]})
        st.bar_chart({"data": [plot1, plot2, plot3, plot4]})
        tables = {
            "1": [plot1],
            "2": [plot2],
            "3": [plot3],
            "4": [plot4]
        }
        st.dataframe(tables)
side=st.sidebar
with side:
          st.sidebar.subheader("Timer")
        
          start_time=st.sidebar.text_input("Enter time")
          placeholder = st.sidebar.empty() 
          if st.sidebar.button("Start"):
    
              for x in range(int(start_time)):
                placeholder.write(f"{x} seconds has passed")
                time.sleep(1)
               
                placeholder.empty()
                
              
              st.balloons()
with tab3:
    st.title("Slope Quiz")
    if "Questions" not in st.session_state:
        st.session_state.Questions=[]
        st.session_state.Correct={}
    if len(st.session_state.Questions)==0:
        for m in range(5):
         y1=random.randint(-10,100)
         y2=random.randint(-10, 100)
         x1=random.randint(-10, 100)
         x2=random.randint(-10, 100)
         while x1==x2:
             x1=random.randint(-10, 100)
         st.session_state.Questions.append((y1,y2,x1,x2))
        
    for b,(y1,y2,x1,x2) in enumerate(st.session_state.Questions):
        def plot_slope_line(x1, y1, x2, y2):
            # Create a DataFrame for the line
            df = pd.DataFrame({
                "x": [x1, x2],
                "y": [y1, y2]
            })
            # Set x as index so Streamlit uses it as the horizontal axis
            df = df.set_index("x")
            st.line_chart(df)
        
        plot_slope_line(x1, y1, x2, y2)
        User_answer=st.number_input(f"What is the slope of the line connecting ({x1}, {y1}) and ({x2}, {y2})?")
        User_answer=(User_answer)
        slope = (y2 - y1) / (x2 - x1)

        if User_answer:
         st.session_state.Correct[b]=(User_answer==slope)
         if b in st.session_state.Correct:
            st.session_state.Correct[b]
            if st.session_state.Correct[b]:
                st.success("Correct")
            elif st.session_state.Correct[b]=="0.00":
                st.write(" ")
            else:
                st.error("Wrong")
                st.warning(f"The answer is {slope}")
    if  st.session_state.Correct:
        if st.button("Result"):
         with st.spinner("Calculating...."):
             
          score=sum(st.session_state.Correct.values())
          st.write(score/5)
          if score==5:
              st.success("You scored 100%")
              st.balloons()
              st.snow()
          elif score==4:
              st.write_stream("Almost there ")
              st.error("Try again")
          else:
              st.error("YOu lost")
    sid=st.sidebar
    with sid:
     try:
       sid.title("Math Evalutor")
       x=st.text_input("Enter a number")
       if st.button("Submit1",key="submit2"):
           result=eval(x)
           st.write("Result"+result)
           
     except Exception as e:
       st.error(f"Error: {e}")
with tab4:
       st.header("Draw")
       stroke=st.slider("Stroke Width", min_value=1, max_value=50,value=10)
       stroke_color=st.color_picker("#000000")
       background=st.color_picker("#F8F6F6")
       height=st.slider("Height", min_value=100, max_value=1000, value=400)
       width=st.slider("Width", min_value=100, max_value=1000, value=600)
       drawing_mode = st.selectbox(
    "Tool",
    ["freedraw", "line", "rect", "circle", "transform"]
)

       canvas=st_canvas(
           stroke_width=stroke,
           stroke_color=stroke_color,
           background_color=background,
           height=height,
           width=width,
           drawing_mode=drawing_mode,
           display_toolbar=True,
           update_streamlit=False,
           key="canvas",
                       )



       




    



              
                    
