import streamlit as st

from src.chain import load_chain
from src.callback_handler import CallbackHandler
from src.sql_chain_handler import SQLChainHandler
from st_components.st_message import display_message, append_message


def st_main():
    _display_welcome_message()
    _handle_chat()


def _handle_chat():
    prompt = st.chat_input()
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})

    callback_handler = CallbackHandler()
    chain = load_chain(callback_handler)

    for message in st.session_state.messages:
        is_user = message["role"] == "user"
        is_data = message["role"] == "data"
        display_message(message["content"], is_user, is_data)

    _process_last_message(chain, callback_handler)


def _display_welcome_message():
    st.info("👋 Hey, we're very happy to see you here.")


def _process_last_message(chain, callback_handler):
    last_message = st.session_state.messages[-1]
    if last_message["role"] != "assistant":
        content = last_message["content"]
        if isinstance(content, str):
            answer = chain(
                {"question": content, "chat_history": st.session_state.history}
            )["answer"]
            append_message(answer)
            _handle_sql_content(chain, callback_handler, answer)


def _handle_sql_content(chain, callback_handler, content):
    handler = SQLChainHandler(chain)
    sql_query = handler.get_sql(content)
    if sql_query:
        df = handler.execute_sql(sql_query)
        if df is not None:
            callback_handler.display_dataframe(df)
            append_message(df, "data")
