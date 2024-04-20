import streamlit as st
import functions

st.title("My Todo App")
st.subheader("Welcome back!", divider='rainbow')

todos = functions.get_action()

for todo in todos:
    st.checkbox(todo.strip("\n"))

st.text_input(label="to-do: ", placeholder="Please text ...")
