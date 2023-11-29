import re
import duckdb
import streamlit as st

from st_components.st_message import append_message

DUCKDB_DATABASE = st.secrets["DUCKDB_DATABASE"]


class SQLChainHandler:
    def __init__(self, chain):
        self.chain = chain

    @staticmethod
    def get_sql(text):
        sql_match = re.search(r"```sql\n(.*)\n```", text, re.DOTALL)
        return sql_match.group(1) if sql_match else None

    @staticmethod
    def create_error_message(query, error):
        return (
            f"You gave me a wrong SQL. FIX the SQL query by searching the schema definition:\n"
            f"```sql\n{query}\n```\nError message:\n\t{error}"
        )

    @staticmethod
    def is_safe_query(query):
        return not re.match(
            r"^\s*(drop|alter|truncate|delete|insert|update)\s", query, re.I
        )

    def handle_sql_exception(self, query, error, retries=2):
        append_message("Uh oh, I made an error, let me try to fix it..")
        error_message = self.create_error_message(query, error)
        new_query = self.chain({"question": error_message, "chat_history": ""})[
            "answer"
        ]
        append_message(new_query)
        if self.get_sql(new_query) and retries > 0:
            return self.execute_sql(self.get_sql(new_query), retries - 1)
        append_message("I'm sorry, I couldn't fix the error. Please try again.")
        return None

    def execute_sql(self, query, retries=2):
        if not self.is_safe_query(query):
            append_message(
                "Sorry, I can't execute queries that can modify the database."
            )
            return None

        try:
            conn = duckdb.connect(DUCKDB_DATABASE)
            return conn.sql(query).df()
        except Exception as e:
            return self.handle_sql_exception(query, e, retries)
