import os
import csv


def __build_file_path(file_path, file_name: str) -> str:
    return os.path.join(file_path, file_name + '.csv')


def save_csv(file_path, file_name: str, rows: list) -> bool:
    '''
    Save rows to a CSV file
        file_name: Name of the file, concats to the defined '../tmp' folder
        rows: Row list of elements to save, example: [['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3']]
        return: True if all went well or false if something goes wrong
    '''
    file_path = __build_file_path(file_path, file_name)
    try:
        with open(file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(rows)
            print(f'\n✅ File saved at [{file_path}]\n')
            return True
    except Exception as exception:
        print(f'\n⛔ Error saving file at [{file_path}]:')
        print(exception)
        return False


def read_csv(file_path, file_name: str) -> list:
    '''
    Read's entire CSV file
        file_name: Name of the file, concats to the defined '../tmp' folder
        return: List fo readed elements or false if something goes wrong
    '''
    file_path = __build_file_path(file_path, file_name)
    try:
        csv_rows = []
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                csv_rows.append(row)
            print(f'\n✅ File readed at [{file_path}]\n')
            return csv_rows
    except Exception as exception:
        print(f'\n⛔ Error reading file at [{file_path}]:')
        print(exception)
        return False
