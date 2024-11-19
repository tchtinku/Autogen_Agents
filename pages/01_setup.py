import streamlit as st
import random
import string
import json

if 'input_keys' not in st.session_state:
    st.session_state.input_keys = []
if 'saved_agents' not in st.session_state:
    st.session_state.saved_agents = []
    
if 'info' not in st.session_state:
    st.session_state.info = None
    
info_placeholder = st.empty()

if not 