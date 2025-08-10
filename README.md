# supply_chain_data_integration_system
# 📦 Supply Chain Data Integration System

## 📋 Overview
The **Supply Chain Data Integration System** is an end-to-end data pipeline and dashboard solution that integrates supply chain data from multiple sources, processes it, and visualizes it for actionable insights.  
It helps businesses monitor **inventory**, **sales**, **stockouts**, and **restock patterns** in real-time using **BigQuery** and **Streamlit**.

---

## 🎯 Project Objectives
- Integrate sales and inventory data from multiple sources.
- Clean, process, and store data in a cloud data warehouse (Google BigQuery).
- Build advanced **Data Marts** (views) for analytics.
- Create an **interactive dashboard** to monitor supply chain KPIs.

---

## 🛠️ Technologies Used
- **Python** – Data cleaning, ETL pipeline
- **Pandas** – Data manipulation
- **Google BigQuery** – Cloud data warehouse
- **Google Cloud IAM** – Secure service account authentication
- **Streamlit** – Interactive dashboard
- **Fake Store API** – Simulated inventory data
- **Global Superstore Dataset** – Sales and returns data

---

## 📁 Data Sources
1. **Global Superstore Dataset** – Historical sales & returns.
2. **Fake Store API** – Simulated inventory data for 30 days.

---

## 🔄 Data Processing Steps
1. **Data Cleaning** – Removed invalid records, parsed dates, merged datasets.
2. **Inventory Simulation** – Simulated daily inventory changes for 30 days with restock flags.
3. **Uploading to BigQuery** – Securely uploaded `orders_fact` and `inventory_fact` tables.
4. **Created Data Marts**:
   - `stockout_alerts_view`
   - `category_performance_view`
   - `inventory_turnover_view`
   - `vendor_performance_view` (planned for future)

---

## 📊 Dashboard Features
Built in **Streamlit**, connected live to BigQuery.

- 📦 **Inventory Levels Over Time** – Trend visualization of stock levels.
- 🚨 **Recent Restocks** – Table of latest restock events.
- 🏆 **Top-Selling Categories** – Bar chart of sales performance.
- ⚠️ **Stockout Alerts** – Notifications for low or zero stock products.
- 👨‍💼 **Vendor Performance** – Placeholder for future vendor analytics.

---

## ✅ Results
- 51,290 cleaned orders uploaded to BigQuery.
- 600 simulated inventory records uploaded.
- Fully functional BigQuery views for analytics.
- Interactive Streamlit dashboard connected to live data.

---

## 🌟 Benefits
- Real-time monitoring of inventory and sales trends.
- Early detection of stockouts.
- Cloud-based data storage for scalability.
- Modular design for easy future feature expansion.

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Lahari8447/supply_chain_data_integration_system.git
cd supply_chain_data_integration_system
