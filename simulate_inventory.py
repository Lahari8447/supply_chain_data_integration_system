import requests
import pandas as pd
import random
from datetime import datetime, timedelta

# ----------------------------
# STEP 1: Fetch products from Fake Store API
# ----------------------------

def get_products():
    url = 'https://fakestoreapi.com/products'
    response = requests.get(url)
    if response.status_code == 200:
        print("✅ Product data fetched successfully!")
        return response.json()
    else:
        raise Exception("❌ Failed to fetch product data.")

# ----------------------------
# STEP 2: Simulate 30-day inventory history
# ----------------------------

def simulate_inventory(products, days=30):
    inventory_history = []
    start_date = datetime.now() - timedelta(days=days)

    for product in products:
        base_inventory = random.randint(20, 200)  # initial stock
        daily_demand = random.randint(2, 10)      # expected demand

        for day in range(days):
            current_date = start_date + timedelta(days=day)

            # Simulate sales
            sales = min(random.randint(0, daily_demand), base_inventory)
            base_inventory -= sales

            # Simulate restock every 7 days
            restock_flag = 0
            if day % 7 == 0:
                restock_qty = random.randint(30, 100)
                base_inventory += restock_qty
                restock_flag = 1

            inventory_history.append({
                'product_id': product['id'],
                'product_name': product['title'],
                'date': current_date.strftime('%Y-%m-%d'),
                'inventory_level': base_inventory,
                'category': product['category'],
                'price': product['price'],
                'restock_flag': restock_flag
            })

    return pd.DataFrame(inventory_history)

# ----------------------------
# STEP 3: Run it
# ----------------------------

if __name__ == '__main__':
    products = get_products()
    inventory_df = simulate_inventory(products, days=30)

    # Output sample and summary
    print(inventory_df.head())
    print(f"\n✅ Inventory simulation completed for {inventory_df['product_id'].nunique()} products over {inventory_df['date'].nunique()} days.")

    # Optional: Save to CSV
    inventory_df.to_csv("simulated_inventory.csv", index=False)
    print("📁 Saved to simulated_inventory.csv")
