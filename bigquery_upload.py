import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

# ✅ Set your actual service account file, project ID, and dataset ID
key_path = "C:/Users/Laxmi/OneDrive/Desktop/project_2/service_account.json"
project_id = "charged-ground-467919-q0"
dataset_id = "supply_chain_data"

# 🔐 Authenticate and connect to BigQuery
credentials = service_account.Credentials.from_service_account_file(key_path)
client = bigquery.Client(credentials=credentials, project=project_id)

# 📤 Function to upload a CSV file to BigQuery
def upload_csv_to_bigquery(csv_file, table_name):
    df = pd.read_csv(csv_file)
    table_ref = f"{project_id}.{dataset_id}.{table_name}"

    # Create dataset if it doesn't exist
    try:
        client.get_dataset(dataset_id)
    except Exception:
        dataset = bigquery.Dataset(f"{project_id}.{dataset_id}")
        client.create_dataset(dataset)
        print(f"✅ Created dataset: {dataset_id}")

    # Load data to table
    job = client.load_table_from_dataframe(df, table_ref)
    job.result()  # Wait for job to complete
    print(f"✅ Uploaded {csv_file} to {table_ref} ({len(df)} rows)")

# 🚀 Upload both files
upload_csv_to_bigquery("cleaned_orders.csv", "orders_fact")
upload_csv_to_bigquery("simulated_inventory.csv", "inventory_fact")
