import pandas as pd

# ✅ Use full correct path
file_path = 'C:/Users/Laxmi/OneDrive/Desktop/SSS/Global Superstore.xls'

# 1. Load Orders and Returns sheets
orders = pd.read_excel(file_path, sheet_name='Orders')
returns = pd.read_excel(file_path, sheet_name='Returns')

# 2. Convert date columns to datetime
orders['Order Date'] = pd.to_datetime(orders['Order Date'], errors='coerce')
orders['Ship Date'] = pd.to_datetime(orders['Ship Date'], errors='coerce')

# 3. Drop rows with missing essential values
orders_clean = orders.dropna(subset=['Order Date', 'Ship Date', 'Order ID', 'Product ID'])

# 4. Clean text columns
orders_clean['Category'] = orders_clean['Category'].str.strip().str.title()
orders_clean['Region'] = orders_clean['Region'].str.strip().str.title()

# 5. Reset index
orders_clean.reset_index(drop=True, inplace=True)

# 6. Print summary
print(f"✅ Cleaned Orders: {len(orders_clean)}")
print(f"📅 Date Range: {orders_clean['Order Date'].min().date()} to {orders_clean['Order Date'].max().date()}")
print(f"📦 Categories: {orders_clean['Category'].unique()}")
print(f"↩️ Return Rate: {len(returns) / len(orders_clean):.2%}")
orders_clean.to_csv('cleaned_orders.csv', index=False)

