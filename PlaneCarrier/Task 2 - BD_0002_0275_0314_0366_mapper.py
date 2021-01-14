#!/usr/bin/python3
import sys
import json
from string import punctuation, digits
from datetime import datetime

punctuation+= "\n\t"
parameter, K = sys.argv[1].strip(), float(sys.argv[2].strip())

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
    
def checkEuclideanDistance(data):
    x0 = float(data["drawing"][0][0][0])
    y0 = float(data["drawing"][0][1][0])
    distance = (x0**2 + y0**2)**0.5
    return distance > K

for line in sys.stdin:
    data = json.loads(line.strip())
    word = data["word"].strip()
    country = data["countrycode"].strip()
    if word != parameter or checkBadRecord(data):
        continue
    if checkEuclideanDistance(data):
        print(f"{country}\t1")
