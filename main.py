from extract import extract_data
from transform import transform_data
from load import load_to_csv

def run_etl():
    # Step 1: Extract
    data = extract_data()
    print("✅ Data extracted.")

    # Step 2: Transform
    transformed_data = transform_data(data)
    print("✅ Data transformed.")

    # Step 3: Load
    load_to_csv(transformed_data)
    print("✅ Data loaded into output.csv.")

if __name__ == "__main__":
    run_etl()
