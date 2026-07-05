import json

def format(data: dict | list)-> str:
    s = json.dumps(data, indent=2, sort_keys=True)
    s = s.replace('{', '')
    s = s.replace('}', '')
    s = s.replace('"', '')
    s = s.replace(',', '')
    return s