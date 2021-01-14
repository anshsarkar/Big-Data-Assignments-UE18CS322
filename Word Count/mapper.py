#!/usr/bin/env python
import sys
from string import punctuation

for line in sys.stdin:
    line = line.strip().lower()
    preprocessed = "".join(ch for ch in line if ch not in punctuation)
    words = preprocessed.split()
    for word in words:
        print("{}\t1".format(word))