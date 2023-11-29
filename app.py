import warnings
import streamlit as st

from st_components.st_init import st_init
from st_components.st_sidebar import st_sidebar
from st_components.st_session_states import init_session_states
from st_components.st_main import st_main

warnings.filterwarnings("ignore")

st_init()
st.title("🐤 chatDuck - Text to SQL")
init_session_states()
st_sidebar()
st_main()
