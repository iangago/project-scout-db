import json

DATA_PATH = "clean/clean_data.json"

def load_clean_data():
    try:
        with open(DATA_PATH, "r") as file:
            clean_data = json.load(file)
            return clean_data
        
    except FileNotFoundError:
        return {}

def save_clean_data(clean_data):
    with open(DATA_PATH, "w") as file:
        json.dump(clean_data, file, indent=4)