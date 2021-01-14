#!/usr/bin/python3

import sys

rank = lambda x: 0.15 + 0.85 * x

prev_page = None

for line in sys.stdin:
    line = line.strip()
    try:
        from_page, page_contribution = line.split(",")
        from_page = from_page.strip()
        page_contribution = float(page_contribution.strip())
    except:
        continue

    if prev_page is None:
        prev_page = from_page
        prev_pagerank = rank(page_contribution)

    elif prev_page == from_page:
        prev_pagerank += 0.85 * page_contribution

    else:
        print("{}, {:.5f}".format(prev_page, prev_pagerank))
        prev_page = from_page
        prev_pagerank = rank(page_contribution)

print("{}, {:.5f}".format(prev_page, prev_pagerank))
