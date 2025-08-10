import pandas as pd

file_path = 'Global Superstore.xls'  # make sure this matches the actual file name

orders = pd.read_excel("C:\\Users\\Laxmi\\OneDrive\\Desktop\\SSS\\Global Superstore.xls.xlsx", sheet_name='Orders')
returns = pd.read_excel("C:\\Users\\Laxmi\\OneDrive\\Desktop\\SSS\\Global Superstore.xls.xlsx", sheet_name='Returns')

orders['Order Date'] = pd.to_datetime(orders['Order Date'], errors='coerce')
orders['Ship Date'] = pd.to_datetime(orders['Ship Date'], errors='coerce')

orders_clean = orders.dropna(subset=['Order Date', 'Ship Date', 'Order ID', 'Product ID'])

orders_clean['Category'] = orders_clean['Category'].str.strip().str.title()
orders_clean['Region'] = orders_clean['Region'].str.strip().str.title()

orders_clean.reset_index(drop=True, inplace=True)

print(f"✅ Cleaned Orders: {len(orders_clean)}")
print(f"📅 Date Range: {orders_clean['Order Date'].min().date()} to {orders_clean['Order Date'].max().date()}")
print(f"📦 Categories: {orders_clean['Category'].unique()}")
print(f"↩️ Return Rate: {len(returns) / len(orders_clean):.2%}")
