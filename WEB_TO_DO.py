import streamlit as st
import function

todos = function.get_todos()

st.header("My todo App")
st.subheader("This is my todo app")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add a todo...")
