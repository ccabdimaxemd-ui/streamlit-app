import streamlit as st
st.title('my first streamlit app')
st.write('this is working')
name = st.text_input('Enter your Name')

if st.button('submit'):
  st.success(f'Hello{name}')
