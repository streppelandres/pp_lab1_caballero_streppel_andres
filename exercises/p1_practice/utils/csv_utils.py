import os
import csv

CSV_OUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tmp'))

def save_csv(file_name, elements):
    file_path = os.path.join(CSV_OUT_PATH, file_name + '.csv')

    try:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(elements)
            print(f'\n✅ File saved at [{file_path}]\n')
            return True
    except Exception as exception:
        print(f'\n⛔ Error saving file at [{file_path}]:')
        print(exception)
        return False