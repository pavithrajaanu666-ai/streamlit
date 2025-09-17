import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("🎓 Student Management System")

menu = ["Add Student", "Update Name", "Delete Student"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Student":
    st.subheader("➕ Add New Student")
    s_no = st.text_input("S No")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=150)
    department = st.text_input("Department")
    cutoff = st.number_input("Cutoff", min_value=0.0, max_value=100.0)

    if st.button("Add Student"):
        data = {
            "s_no": s_no,
            "name": name,
            "age": age,
            "department": department,
            "cutoff": cutoff
        }
        response = requests.post(f"{API_URL}/std/", json=data)
        if response.status_code == 200:
            st.success("✅ Student added successfully!")
            st.json(response.json())
        else:
            st.error(f"❌ Failed! Status code: {response.status_code}")

elif choice == "Update Name":
    st.subheader("✏️ Update Student Name")
    s_no = st.text_input("S No")
    name = st.text_input("New Name")

    if st.button("Update Name"):
        data = {"s_no": s_no, "name": name}
        response = requests.post(f"{API_URL}/update/", json=data)
        if response.status_code == 200:
            st.success("✅ Name updated successfully!")
            st.json(response.json())
        else:
            st.error(f"❌ Failed! Status code: {response.status_code}")

elif choice == "Delete Student":
    st.subheader("🗑️ Delete Student")
    s_no = st.text_input("S No to Delete")

    if st.button("Delete Student"):
        data = {"s_no": s_no}
        response = requests.post(f"{API_URL}/delete/", json=data)
        if response.status_code == 200:
            st.success("✅ Student deleted successfully!")
            st.json(response.json())
        else:
            st.error(f"❌ Failed! Status code: {response.status_code}")
