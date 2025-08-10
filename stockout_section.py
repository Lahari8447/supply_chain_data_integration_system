import streamlit as st

def show_stockout_alerts(run_query):
    st.subheader("⚠️ Stockout Alerts")

    query = """
    SELECT date, product_name, category, inventory_level
    FROM `charged-ground-467919-q0.supply_chain_data.stockout_alerts_view`
    ORDER BY date DESC
    LIMIT 20
    """

    df = run_query(query)

    if df.empty:
        st.success("✅ No stockouts detected. All inventory is healthy.")
    else:
        st.dataframe(df)
