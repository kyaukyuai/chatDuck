import duckdb
import os
import streamlit as st

DUCKDB_DATABASE = st.secrets["DUCKDB_DATABASE"]


class TableDescriber:
    def __init__(self, conn, output_dir):
        self.conn = conn
        self.output_dir = output_dir

    def create_output_dir(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def get_tables(self):
        return self.conn.execute("SHOW TABLES").fetchall()

    def describe_table(self, table_name):
        describe_table_query = f"DESCRIBE {table_name}"
        return self.conn.execute(describe_table_query).fetchdf()

    @staticmethod
    def create_markdown(table_name, schema_info):
        markdown_text = f"# Table: {table_name}\n\n"
        markdown_text += "| Column Name | Data Type |\n"
        markdown_text += "|-------------|-----------|\n"
        for index, row in schema_info.iterrows():
            markdown_text += f"| {row['column_name']} | {row['column_type']} |\n"
        return markdown_text

    def save_to_file(self, table_name, markdown_text):
        with open(os.path.join(self.output_dir, f"{table_name}.md"), "w") as file:
            file.write(markdown_text)

    def describe_all_tables(self):
        self.create_output_dir()
        tables = self.get_tables()
        for (table_name,) in tables:
            schema_info = self.describe_table(table_name)
            markdown_text = self.create_markdown(table_name, schema_info)
            self.save_to_file(table_name, markdown_text)


describer = TableDescriber(duckdb.connect(DUCKDB_DATABASE), "docs")
describer.describe_all_tables()
