import json

DATA_PATH = "raw/raw_data.json"

def load_raw_data():
    try:
        with open(DATA_PATH, "r") as file:
            raw_data = json.load(file)
            return raw_data
        
    except FileNotFoundError:
        return {}

def save_raw_data(raw_data):
    with open(DATA_PATH, "w") as file:
        json.dump(raw_data, file, indent=4)