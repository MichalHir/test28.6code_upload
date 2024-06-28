import json

file_path = "cars.json"


def read_json():
    with open(file_path, "r") as file:
        data = json.load(file)
        return data


def save_json(cars_array):
    with open(file_path, "w") as file:
        json.dump(cars_array, file)
