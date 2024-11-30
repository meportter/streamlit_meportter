import streamlit as st

Youtube_URL = st.text_input("Youtube_URL", 
                        value=st.session_state.get('Youtube_URL',''))

if Youtube_URL:
    st.session_state['Youtube_URL'] = Youtube_URL