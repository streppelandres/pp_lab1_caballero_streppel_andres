import os
from utilities.files.json import json_utils


class Helper:
    __JSON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), './_data'))
    __CSV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), './_tmp'))

    elements: list

    def __init__(self) -> None:
        self.elements = json_utils.read_json(self.__JSON_PATH, 'data')
