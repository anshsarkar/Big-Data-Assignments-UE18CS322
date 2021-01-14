import sys

vfname1, vfname2, outfname1, outfname2 = sys.argv[1:5]

vfile1, vfile2 = dict(), dict()

print("Comparing v files...\n")

with open(vfname1) as v1, open(vfname2) as v2:
    content1 = v1.read().strip().split("\n")
    content2 = v2.read().strip().split("\n")
    total_pages1, total_pages2 = len(content1), len(content2)
    flag = True
    if total_pages1 != total_pages2:
        print(
            f"Mismatched number of pages present in v files: exepected {total_pages1}, obtained {total_pages2}"
        )
        flag = False
        for i in range(total_pages1):
            try:
                page, rank = content1[i].split(",")
            except:
                print(f"Error in row {i+1}: Could not unpack items in v file 1")
                flag = False
                continue

            vfile1[page.strip()] = rank.strip()
            if rank != "1":
                print(f"Error in row {i+1}: Rank in v file 1 is not 1 in v file 1")
                flag = False

        for i in range(total_pages2):
            try:
                page, rank = content1[i].split(",")
            except:
                print(f"Error in row {i+1}: Could not unpack items in v file 2")
                flag = False
                continue
            vfile2[page.strip()] = rank.strip()
            if rank != "1":
                print(
                    f"Error in row {i+1} v file 2: Rank in v file 2 is not 1 in v file 2"
                )
                flag = False

        print(
            f"Pages in v file 1 but not in v file 2: {list(set(list(vfile1.keys())) - set(list(vfile2.keys())))}"
        )
        print(
            f"Pages in v file 2 but not in v file 1: {list(set(list(vfile2.keys())) - set(list(vfile1.keys())))}"
        )

    else:
        print("Equal number of pages in v files: GOOD SO FAR")
        for i in range(total_pages1):
            try:
                page1, rank1 = content1[i].split(",")
            except:
                print(f"Error in row {i+1}: Could not unpack items in v file 1")
                flag = False
                continue
            page1 = page1.strip()
            rank1 = rank1.strip()
            vfile1[page1] = rank1

            try:
                page2, rank2 = content2[i].split(",")
            except:
                print(f"Error in row {i+1}: Could not unpack items in v file 2")
                flag = False
                continue
            page2 = page2.strip()
            rank2 = rank2.strip()
            vfile2[page2] = rank2

            if rank1 == "1" and rank2 == "1":
                continue
            if rank1 != 1:
                print(f"Error in row {i+1}: Rank in v file 1 is not 1")
                flag = False
            if rank2 != 1:
                print(f"Error in row {i+1}: Rank in v file 2 is not 1")
                flag = False

        if set(list(vfile1.keys())) != set(list(vfile2.keys())):
            print("Mismatch in pages present:")
            print(
                f"Pages in v file 1 but not in v file 2: {list(set(list(vfile1.keys())) - set(list(vfile2.keys())))}"
            )
            print(
                f"Pages in v file 2 but not in v file 1: {list(set(list(vfile2.keys())) - set(list(vfile1.keys())))}"
            )

    if not flag:
        print("One or more issues found in v files: BAD OUTCOME\n")
    else:
        print("Both v files are the same: NO ISSUES\n")

outfile1, outfile2 = dict(), dict()

print("Comparing adj_list files...\n")

with open(outfname1) as o1, open(outfname2) as o2:
    content1 = o1.read().strip().split("\n")
    content2 = o2.read().strip().split("\n")
    total_pages1, total_pages2 = len(content1), len(content2)
    flag = True
    if total_pages1 != total_pages2:
        print(
            f"Mismatched number of pages present in adj_list files: exepected {total_pages1}, obtained {total_pages2}"
        )
        flag = False
        for i in range(total_pages1):
            try:
                page, links = content1[i].split("\t")
            except:
                print(f"Error in row {i+1}: Could not unpack items in adj_list file 1")
                flag = False
                continue

            try:
                outfile1[page.strip()] = eval(links.strip())
            except:
                print(
                    f"Error in row {i+1}: Non-list type outgoing links element found in in adj_list file 1"
                )
                flag = False
                continue

            if sorted(eval(links.strip())) != eval(links.strip()):
                print(
                    f"Error in row {i+1}: Outgoing links not sorted in adj_list file 1"
                )
                flag = False

        for i in range(total_pages2):
            try:
                page, links = content1[i].split("\t")
            except:
                print(f"Error in row {i+1}: Could not unpack items in adj_list file 2")
                flag = False
                continue

            try:
                outfile2[page.strip()] = eval(links.strip())
            except:
                print(
                    f"Error in row {i+1}: Non-list type outgoing links element found in in adj_list file 2"
                )
                flag = False
                continue

            if sorted(eval(links.strip())) != eval(links.strip()):
                print(
                    f"Error in row {i+1}: Outgoing links not sorted in adj_list file 2"
                )
                flag = False

        print(
            f"Pages in adj_list file 1 but not in adj_list file 2: {list(set(list(outfile1.keys())) - set(list(outfile2.keys())))}"
        )
        print(
            f"Pages in adj_list file 2 but not in adj_list file 1: {list(set(list(outfile2.keys())) - set(list(outfile1.keys())))}"
        )

    else:
        print("Equal number of pages in adj_list files: GOOD SO FAR")
        for i in range(total_pages1):
            try:
                page1, links1 = content1[i].split("\t")
            except:
                print(f"Error in row {i+1}: Could not unpack items in adj_list file 1")
                flag = False
                continue
            page1 = page1.strip()
            try:
                links1 = eval(links1.strip())
            except:
                print(
                    f"Error in row {i+1}: Non-list type outgoing links element found in in adj_list file 1"
                )
                flag = False
                continue
            if sorted(links1) != links1:
                print(
                    f"Error in row {i+1}: Outgoing links not sorted in adj_list file 1"
                )
                flag = False

            try:
                page2, links2 = content2[i].split("\t")
            except:
                print(f"Error in row {i+1}: Could not unpack items in adj_list file 2")
                flag = False
                continue
            page2 = page2.strip()
            try:
                links2 = eval(links2.strip())
            except:
                print(
                    f"Error in row {i+1}: Non-list type outgoing links element found in in adj_list file 2"
                )
                flag = False
                continue
            if sorted(links2) != links2:
                print(
                    f"Error in row {i+1}: Outgoing links not sorted in adj_list file 2"
                )
                flag = False

            if page1 == page2 and links1 == links2:
                continue
            if page1 != page2:
                print(
                    f"Error in row {i+1}: Mismatch in pages - expected {page1}, obtained {page2}"
                )
                flag = False
            if links1 != links2:
                print(
                    f"Error in row {i+1}: Mismatch in links - expected {links1}, obtained {links2}"
                )
                flag = False

        if set(list(outfile1.keys())) != set(list(outfile2.keys())):
            flag = False
            print("Mismatch in pages present:")
            print(
                f"Pages in v file 1 but not in v file 2: {list(set(list(outfile1.keys())) - set(list(outfile2.keys())))}"
            )
            print(
                f"Pages in v file 2 but not in v file 1: {list(set(list(outfile2.keys())) - set(list(outfile1.keys())))}"
            )

        sorted_pages1 = sorted(list(outfile1.keys()))
        sorted_pages2 = sorted(list(outfile2.keys()))

        if list(outfile1.keys()) != sorted_pages1:
            print(f"Error in pages: pages not sorted in adj_list file 1")
            flag = False

        if list(outfile2.keys()) != sorted_pages2:
            print(f"Error in pages: pages not sorted in adj_list file 2")
            flag = False

    if not flag:
        print("One or more issues found in adj_list files: BAD OUTCOME")
    else:
        print("Both adj_list files are the same: NO ISSUES FOUND")
