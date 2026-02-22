
import json
import os


def save_data(data, filename):
    
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print("Error saving file:", e)


def load_data(filename):
    
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r") as file:
            return json.load(file)
    except Exception as e:
        print("Error loading file:", e)
        return []