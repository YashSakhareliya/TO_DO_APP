import streamlit as st
import function


todos = function.get_todos()
def get_todo():
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    function.write_todos(todos)




st.header("My todo App")
st.subheader("This is my todo app")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add a todo...",on_change=get_todo,key="new_todo")
st.session_state
