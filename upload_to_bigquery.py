import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

# 🔐 Path to your service account key
key_path = "C:/Users/Laxmi/OneDrive/Desktop/project_2/service_account.json"  # ← update if named differently
project_id = "your-gcp-project-id"  # ← replace with your real GCP project ID
dataset_id = "supply_chain_data"    # You can change or keep this

# Setup BigQuery client
credentials = service_account.Credentials.from_service_account_file(key_path)
client = bigquery.Client(credentials=credentials, project=project_id)

def upload_csv_to_bigquery(csv_file, table_name):
    df = pd.read_csv(csv_file)
    table_ref = f"{project_id}.{dataset_id}.{table_name}"

    # Create dataset if not exists
    try:
        client.get_dataset(dataset_id)
    except Exception:
        dataset = bigquery.Dataset(f"{project_id}.{dataset_id}")
        client.create_dataset(dataset)
        print(f"✅ Created dataset: {dataset_id}")

    # Upload data
    job = client.load_table_from_dataframe(df, table_ref)
    job.result()  # Wait for job to finish
    print(f"✅ Uploaded {csv_file} to {table_ref} ({len(df)} rows)")

# Upload both datasets
upload_csv_to_bigquery("cleaned_orders.csv", "orders_fact")
upload_csv_to_bigquery("simulated_inventory.csv", "inventory_fact")
