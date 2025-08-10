import streamlit as st
import pandas as pd
from google.oauth2 import service_account
from google.cloud import bigquery
from stockout_section import show_stockout_alerts

# Streamlit UI setup
st.set_page_config(page_title="Supply Chain Dashboard", layout="wide")

# Authenticate with BigQuery
credentials = service_account.Credentials.from_service_account_file(
    "service_account.json"
)
project_id = "charged-ground-467919-q0"
client = bigquery.Client(credentials=credentials, project=project_id)

@st.cache_data(ttl=3600)
def run_query(query):
    return client.query(query).to_dataframe()

# Sidebar filter
st.sidebar.title("Filters")
selected_category = st.sidebar.selectbox("Select Category", ["All", "men's clothing", "jewelery", "electronics", "women's clothing"])

# Inventory Trend
st.title("📦 Inventory Levels Over Time")

query_inventory = """
SELECT date, category, SUM(inventory_level) AS total_inventory
FROM `charged-ground-467919-q0.supply_chain_data.inventory_fact`
{where_clause}
GROUP BY date, category
ORDER BY date
"""

where = ""
if selected_category != "All":
    where = f"WHERE category = '{selected_category}'"
query_inventory = query_inventory.format(where_clause=where)

df_inventory = run_query(query_inventory)
st.line_chart(df_inventory.pivot(index='date', columns='category', values='total_inventory'))

# Restock Alerts
st.subheader("🚨 Recent Restocks")

query_restock = """
SELECT date, product_name, category, inventory_level
FROM `charged-ground-467919-q0.supply_chain_data.inventory_fact`
WHERE restock_flag = 1
ORDER BY date DESC
LIMIT 10
"""

df_restock = run_query(query_restock)
st.dataframe(df_restock)

# Category Sales
st.subheader("🏆 Top-Selling Categories")

query_sales = """
SELECT Category, ROUND(SUM(Sales), 2) AS total_sales
FROM `charged-ground-467919-q0.supply_chain_data.orders_fact`
GROUP BY Category
ORDER BY total_sales DESC
"""

df_sales = run_query(query_sales)
st.bar_chart(df_sales.set_index("Category"))
show_stockout_alerts(run_query)

# Vendor Section (placeholder)
st.subheader("👨‍💼 Vendor Performance")
st.info("Vendor data not available in Fake Store API. This section can be added later.")
