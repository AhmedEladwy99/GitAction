import csv
import logging
logging.basicConfig(level=logging.INFO)

logging.info("Data extracted successfully.")

def load_to_csv(data, file_name="output.csv"):
    keys = data[0].keys()
    with open(file_name, 'w', newline='', encoding='utf-8') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

