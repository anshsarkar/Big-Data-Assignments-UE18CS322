#!/usr/bin/python3
import sys

wordCountRecognized, wordCountNotRecognized = 0, 0

for line in sys.stdin:
    line = line.strip()
    isRecognized, count = line.split("\t")

    try:
        count = int(count.strip())
    except:
        continue
    
    if isRecognized.strip() == "RECOGNIZED":
        wordCountRecognized+= count
    else:
        wordCountNotRecognized+= count

else:
    print(wordCountRecognized)
    print(wordCountNotRecognized)

