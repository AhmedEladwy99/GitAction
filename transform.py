import logging
logging.basicConfig(level=logging.INFO)
logging.info("Data extracted successfully.")


def transform_data(data):
    transformed = []
    for country in data:
        transformed.append({
            "name": country.get("name", {}).get("common"),
            "population": country.get("population"),
            "region": country.get("region")
        })
    return transformed
