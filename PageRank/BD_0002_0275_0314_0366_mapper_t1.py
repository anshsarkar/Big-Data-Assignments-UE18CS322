#!/usr/bin/python3

import sys

for line in sys.stdin:
    line = line.strip()
    if line[0] != "#":
        try:
            from_node, to_node = line.split()
            from_node = from_node.strip()
            to_node = to_node.strip()
        except:
            continue
        print(f"{from_node}\t{to_node}")
