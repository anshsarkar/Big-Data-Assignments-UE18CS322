#!/usr/bin/python3
import sys

wordCount = dict()

for line in sys.stdin:
    line = line.strip()
    country, count = line.split("\t")
    country = country.strip()
    
    try:
        count = int(count.strip())
    except:
        continue

    if country not in wordCount.keys():
        wordCount[country] = 0
    wordCount[country]+= count

items = list(wordCount.items())
items.sort(key = lambda x: x[0])
for country, count in items:
    print(f"{country},{count}")
