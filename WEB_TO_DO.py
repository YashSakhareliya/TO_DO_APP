import streamlit as st
import function


st.set_page_config(layout="wide")
todos = function.get_todos()

def get_todo():
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    function.write_todos(todos)



st.header("My todo App")
st.subheader("This is my todo app")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="",placeholder="Add a todo...",on_change=get_todo,key="new_todo")

