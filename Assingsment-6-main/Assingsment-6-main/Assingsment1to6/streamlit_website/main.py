import streamlit as st
st.set_page_config(page_title="My firs website", page_icon="🌍",layout="centered")
st.title('welcome to my first pythonn website')

page = st.sidebar.radio('go to',['home','about','contact'])

if page == 'home':
     st.header('home page')
     st.write('this is a simple homepage built with python as streamlit ')
     name = st.text_input('whatis your name?')
     if name:
          st.success(f'hello {name} thank for visting')
elif page == 'about':
     st.header('about')
     st.write('this website is built entrierly using pythonng and streamlit ')
elif page == 'contact':
     st.header('contact us')
     email = st.text_input('your email')
     message = st.text_input('your massege')
     if st.button('submit'):
          st.success('thank you we have received your massege')
