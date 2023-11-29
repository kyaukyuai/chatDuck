import duckdb
import streamlit as st

conn = duckdb.connect(st.secrets["DUCKDB_DATABASE"])

tables = [
    "olist_customers_dataset",
    "olist_geolocation_dataset",
    "olist_order_items_dataset",
    "olist_order_payments_dataset",
    "olist_order_reviews_dataset",
    "olist_orders_dataset",
    "olist_products_dataset",
    "olist_sellers_dataset",
    "product_category_name_translation",
]

for table in tables:
    conn.sql(
        f"""
        CREATE TABLE IF NOT EXISTS {table}
        AS SELECT * FROM read_csv_auto('./seed/data/e-commerce/{table}.csv', header = True)
        """
    )

print(conn.sql("SHOW TABLES"))
conn.close()
