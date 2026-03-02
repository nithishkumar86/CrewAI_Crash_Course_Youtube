import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("🎓 Student Management System")

# ─────────────────────────────────
# 1. GET ALL STUDENTS
# ─────────────────────────────────
st.header("📋 All Students")
if st.button("Get All Students"):
    response = requests.get(f"{BASE_URL}/students")
    students = response.json()
    st.json(students)

# ─────────────────────────────────
# 2. GET SINGLE STUDENT
# ─────────────────────────────────
st.header("🔍 Get Student by ID")
name = st.text_input("Enter you name")
if st.button("Get Student"):
    response = requests.get(f"{BASE_URL}/single_students/{name}")

    st.json(response.json())

# ─────────────────────────────────
# 3. CREATE STUDENT
# ─────────────────────────────────
st.header("➕ Create Student")
new_id = st.number_input("Student ID", min_value=1, step=1, key="create_id")
new_name = st.text_input("Student Name", key="create_name")
if st.button("Create Student"):
    response = requests.post(
        f"{BASE_URL}/students",
        json={"id": new_id, "name": new_name}
    )

    if response.status_code == 200:
        st.success(response.json()["message"])
    else:
        st.error("there is error occured")

# ─────────────────────────────────
# 4. UPDATE STUDENT
# ─────────────────────────────────
st.header("✏️ Update Student")
update_id = st.number_input("Student ID to Update", min_value=1, step=1, key="update_id")
update_name = st.text_input("New Name", key="update_name")
if st.button("Update Student"):
    response = requests.put(
        f"{BASE_URL}/students/{update_id}",
        json={"id": update_id, "name": update_name}
    )
    if response.status_code == 200:
        st.success(response.json())
    else:
        st.error("there is error occured")

# ─────────────────────────────────
# 5. DELETE STUDENT
# ─────────────────────────────────
st.header("🗑️ Delete Student")
delete_id = st.number_input("Student ID to Delete", min_value=1, step=1, key="delete_id")
if st.button("Delete Student"):
    response = requests.delete(f"{BASE_URL}/students/{delete_id}")
    st.warning(response.json()["message"])