import streamlit as st
import warnings

warnings.filterwarnings('ignore')

st.title("Autogen Team")
st.write("It takes only 3 steps")

st.page_link( "pages/01_setup.py", icon="🤖", label="Step1: Create a team of agents")

st.page_link( "pages/01_setup_transitions.py", icon="🔄", label="Step2: Define allowed transitions between agents.")

st.page_link( "pages/02_run.py", icon="🏃‍♂️", label="Step3: Run your agentic workflow!")
