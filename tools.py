import json
import csv

from states import STATES

def format(data: dict | list)-> str:
    '''Formats json for readability'''
    s = json.dumps(data, indent=2, sort_keys=True)
    s = s.replace('{', '')
    s = s.replace('}', '')
    s = s.replace('"', '')
    s = s.replace(',', '')
    return s

def schools () -> list[str]:
    '''Parses csv file and returns data'''
    # read file with correct encoding
    stream = open('./school_data.csv', encoding='cp1252', newline='')
    reader = csv.reader(stream, delimiter=',')
    return list(reader)[1:]

def state_name(abbreviation: str) -> str:
    '''Retrieves the state name by the abbreviation'''
    return STATES.get(abbreviation, '')