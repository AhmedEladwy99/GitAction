import requests
from transform import transform_data

import logging
logging.basicConfig(level=logging.INFO)
logging.info("Data extracted successfully.")


def test_api_response():
    response = requests.get("https://restcountries.com/v3.1/all")
    assert response.status_code == 200

def test_transformation_structure():
    sample = [{
        "name": {"common": "Egypt"},
        "population": 100000000,
        "region": "Africa"
    }]
    transformed = transform_data(sample)
    assert "name" in transformed[0]
    assert "population" in transformed[0]
    assert "region" in transformed[0]
