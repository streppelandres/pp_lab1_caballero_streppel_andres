import json_utils

__JSON_NAME = '_test_json'
__DICTIONARY = [{'key': 'value', 'key2': 'value'}, {'key': 'value', 'key2': 'value'}]

def test_save_json():
    assert json_utils.save_json(__JSON_NAME, __DICTIONARY)

def test_read_json():
    assert json_utils.read_json(__JSON_NAME) == __DICTIONARY