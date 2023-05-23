import os
import json


def __build_file_path(file_name: str) -> str:
    return os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '../_tmp')), file_name + '.json')


def save_json(file_name, data) -> bool:
    file_path = __build_file_path(file_name)
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)
        return True


def read_json(file_name) -> list:
    file_path = __build_file_path(file_name)
    with open(file_path, 'r') as json_file:
        return json.load(json_file)