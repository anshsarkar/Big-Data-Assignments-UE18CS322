#!/usr/bin/python3
import sys
import json
from string import punctuation, digits
from datetime import datetime

punctuation+= "\n\t"

def checkBadRecord(data):
    if len(data["word"]) > 0 and len(set(data["word"]).intersection(set(punctuation + digits))) > 0:
        return True
    if len(data["countrycode"]) != 2 or not data["countrycode"].isupper():
        return True
    if not isinstance(data["recognized"], bool):
        return True
    if len(data["key_id"]) != 16 or not data["key_id"].isnumeric():
        return True
    if len(data["drawing"]) < 1 or not all([len(i) == 2 for i in data["drawing"]]):
        return True
    return False
    
parameter = sys.argv[1].strip()

for line in sys.stdin:
    data = json.loads(line.strip())
    word = data["word"].strip()
    if word != parameter or checkBadRecord(data):
        continue
    if data["recognized"]:
        print("RECOGNIZED\t1")
    elif datetime.strftime(datetime.strptime(data["timestamp"].strip(), r"%Y-%m-%d %H:%M:%S.%f %Z"), r"%A") in ["Saturday", "Sunday"]:
        print("UNRECOGNIZED\t1")
    else:
        pass
