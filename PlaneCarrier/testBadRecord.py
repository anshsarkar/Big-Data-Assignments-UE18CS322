#!/usr/bin/python3
import sys
import json
from string import punctuation, digits

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

with open("Input/badrecord.ndjson") as f:
    for line in f:
        #print(line)
        data = json.loads(line.strip())
        if checkBadRecord(data):
            print("BAD RECORD -- CORRECT")
        else:
            print("CORRECT RECORD -- INCORRECT")