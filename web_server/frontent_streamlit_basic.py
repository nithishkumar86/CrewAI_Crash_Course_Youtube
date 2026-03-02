import streamlit as st
import time

st.set_page_config(page_title="simple_web_page",layout='centered')
st.title("🎓 Streamlit Quick Intro")

# ─────────────────────────────────
# 1. TEXT INPUT
# ─────────────────────────────────
st.header("1. Text Input")
name = st.text_input("Enter Your Name")
st.write(f"Hello, {name}!")

# ─────────────────────────────────
# 2. NUMBER INPUT
# ─────────────────────────────────
st.header("2. Number Input")
age = st.number_input("Enter Your Age", min_value=1, max_value=100, step=1)
st.write(f"Your Age is {age}")

# ─────────────────────────────────
# 3. SELECTBOX
# ─────────────────────────────────
st.header("3. Select Box")
course = st.selectbox("Select Your Course", ["Python", "Java", "JavaScript", "C++"])
st.write(f"You selected: {course}")

# ─────────────────────────────────
# 4. BUTTON
# ─────────────────────────────────
st.header("4. Button")
if st.button("Click Me"):
    st.success("Button Clicked!")

# ─────────────────────────────────
# 5. RADIO
# ─────────────────────────────────


st.header("1. Radio Button")
gender = st.radio("Select Gender", ["Male", "Female", "Other"])
st.write(f"You selected: {gender}")

# ─────────────────────────────────
# 6.EXPANDER
# ─────────────────────────────────


st.header("2. Expander")
with st.expander("Click to See More Info"):
    st.write("This is hidden content!")
    st.write("Name: John")
    st.write("Age: 25")
    st.write("Course: Python")

# ─────────────────────────────────
# 7.SPINNER
# ─────────────────────────────────


st.header("3. Spinner")
if st.button("Load Data"):
    with st.spinner("Loading... Please wait!"):
        time.sleep(3)   # ← simulates loading
    st.success("Data Loaded!")

# ─────────────────────────────────
# 9. SESSION STATE
# ─────────────────────────────────

# What is Session State?

# Session State is a way to store and remember values in Streamlit even when the page reruns.

st.header("5. Session State")

# Initialize
if "counter" not in st.session_state:
    st.session_state.counter = 0

col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Increment"):
        st.session_state.counter += 1

with col2:
    if st.button("➖ Decrement"):
        st.session_state.counter -= 1

st.write(f"Counter Value: {st.session_state.counter}")