import json

def get_json(filepath='./picture_text/Ruby_Crystal_Ring_Stats.json'):
    with open(filepath) as f:
        data = json.load(f)
    return data


def has_text(source_text, find_text="ATTACHMENT"):    
    for text in source_text:
        if text['DetectedText'] == find_text:
            return True
    else:
        return False

def find_value_by_id(source_text,id=4):
    for text in source_text:
        if text['Id'] == id:
            return text['DetectedText']
    else:
        return 0