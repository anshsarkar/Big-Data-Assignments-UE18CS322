#!/usr/bin/python3

import sys

pagerank = dict()

with open(sys.argv[1].strip()) as v_file:
    lines = v_file.read().strip().split("\n")
    for line in lines:
        try:
            page, rank = line.split(",")
        except:
            continue
        pagerank[page.strip()] = float(rank.strip())


for line in sys.stdin:
    line = line.strip()
    try:
        from_node, to_nodes = line.split("\t")
        from_node = from_node.strip()
        to_nodes = eval(to_nodes.strip())
    except:
        continue

    num_outgoing_links = len(to_nodes)
    from_node_pagerank = pagerank[from_node]
    from_node_contribution = from_node_pagerank * (1 / num_outgoing_links)

    print(f"{from_node},0")

    for node in to_nodes:
        if node in pagerank.keys():
            print(f"{node},{from_node_contribution}")