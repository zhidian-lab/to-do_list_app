import streamlit as st
import functions

def add_action():
    new_todo = st.session_state["new_todo"] + "\n"
    functions.add_action(new_todo)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("Welcome back!", divider='rainbow')

todos = functions.get_action()

for i, todo in enumerate(todos):
    st.checkbox(label=todo, key=todo)
    if st.session_state[todo]:
        todos = functions.get_action()
        todos.pop(i)
        functions.overwrite_action(todos)
        st.session_state.pop(todo)
        st.rerun()

st.text_input(label="to-do: ", placeholder="Please text ...",
              key="new_todo", on_change=add_action)
st.session_state

