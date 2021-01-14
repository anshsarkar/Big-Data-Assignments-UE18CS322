#!/usr/bin/python3

import sys

output_dir = sys.argv[1].strip()

prev_node = None
prev_node_outlink = list()

with open(output_dir, "w") as v_file:
    for line in sys.stdin:
        line = line.strip()
        try:
            from_node, to_node = line.split()
            from_node = from_node.strip()
            to_node = to_node.strip()
        except:
            continue

        if prev_node is None:
            prev_node = from_node
            prev_node_outlink.append(to_node)

        elif prev_node == from_node:
            prev_node_outlink.append(to_node)

        else:
            prev_node_outlink.sort()
            print(f"{prev_node}\t{prev_node_outlink}")
            v_file.write(f"{prev_node}, 1\n")
            prev_node = from_node
            prev_node_outlink.clear()
            prev_node_outlink.append(to_node)

    prev_node_outlink.sort()
    print(f"{prev_node}\t{prev_node_outlink}")
    v_file.write(f"{prev_node}, 1\n")