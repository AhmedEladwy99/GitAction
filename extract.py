import requests

import logging
logging.basicConfig(level=logging.INFO)


logging.info("Data extracted successfully.")


def extract_data():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
