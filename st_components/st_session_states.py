import streamlit as st

INITIAL_MESSAGE = [
    {"role": "user", "content": "Hi!"},
    dict(
        role="assistant",
        content="""Hey there, I'm chatDuck,
your SQL-speaking sidekick,
ready to chat up DuckDB and fetch answers! 🔍
""",
    ),
]


def init_session_states():
    if "messages" not in st.session_state:
        st.session_state.messages = INITIAL_MESSAGE

    if "history" not in st.session_state:
        st.session_state.history = []
