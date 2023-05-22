import csv_utils

__CSV_NAME = '_test_csv'
__CSV_HEAD = ['A1', 'B1', 'C1']
__CSV_DATA = [['A2', 'B2', 'C2'], ['A3', 'B3', 'C3'], ['A4', 'B4', 'C4']]


def test_save_csv():
    assert csv_utils.save_csv(__CSV_NAME, [__CSV_HEAD] + __CSV_DATA)


def test_read_csv():
    assert csv_utils.read_csv(__CSV_NAME) == [__CSV_HEAD] + __CSV_DATA
