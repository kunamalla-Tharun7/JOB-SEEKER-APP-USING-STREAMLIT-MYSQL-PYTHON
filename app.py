import streamlit as st
import mysql.connector

# database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tharun@19",
    database="job_portal"
)

cursor = conn.cursor()

st.title("Job Seeker Portal")

menu = ["Register","Login","View Jobs"]
choice = st.sidebar.selectbox("Menu",menu)

# Register
if choice == "Register":
    st.subheader("Create Account")

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password",type="password")
    skills = st.text_input("Skills")

    if st.button("Register"):
        query = "INSERT INTO users(name,email,password,skills) VALUES(%s,%s,%s,%s)"
        cursor.execute(query,(name,email,password,skills))
        conn.commit()
        st.success("Registration Successful")

# Login
elif choice == "Login":
    st.subheader("Login")

    email = st.text_input("Email")
    password = st.text_input("Password",type="password")

    if st.button("Login"):
        query = "SELECT * FROM users WHERE email=%s AND password=%s"
        cursor.execute(query,(email,password))
        result = cursor.fetchone()

        if result:
            st.success("Login Successful")
        else:
            st.error("Invalid Credentials")

# View Jobs
elif choice == "View Jobs":
    st.subheader("Available Jobs")

    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()

    for job in jobs:
        st.write("Job Title:",job[1])
        st.write("Company:",job[2])
        st.write("Location:",job[3])
        st.write("Skills Required:",job[4])
        st.write("------------------------")