import json
import csv

def format(data: dict | list)-> str:
    s = json.dumps(data, indent=2, sort_keys=True)
    s = s.replace('{', '')
    s = s.replace('}', '')
    s = s.replace('"', '')
    s = s.replace(',', '')
    return s

def schools () -> list[str]:
    # read file with correct encoding
    stream = open('./school_data.csv', encoding='cp1252', newline='')
    reader = csv.reader(stream, delimiter=',')
    return list(reader)
