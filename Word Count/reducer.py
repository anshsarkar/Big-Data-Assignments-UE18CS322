#!/usr/bin/env python
import sys
wordCount = dict()

for line in sys.stdin:
    word, count = line.split("\t")
    word = word.strip()
    count = count.strip()

    try:
        count = int(count)
    except ValueError:
        continue

    if word not in wordCount.keys():
        wordCount[word] = 0
    wordCount[word]+= count

for word, count in wordCount.items():
    print("{}\t{}".format(word, count))