import sys

vfname1, vfname2 = sys.argv[1:3]
vfile1, vfile2 = dict(), dict()


print("Comparing Page Ranks......")

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

        for i in range(total_pages2):
            try:
                page, rank = content1[i].split(",")
            except:
                print(f"Error in row {i+1}: Could not unpack items in v file 2")
                flag = False
                continue
            vfile2[page.strip()] = rank.strip()

        print(
            f"Pages in v file 1 but not in v file 2: {list(set(list(vfile1.keys())) - set(list(vfile2.keys())))}"
        )
        print(
            f"Pages in v file 2 but not in v file 1: {list(set(list(vfile2.keys())) - set(list(vfile1.keys())))}"
        )

    else:
        print("Equal number of pages in v files: GOOD OUTCOME")
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

            if page1 == page2 and rank1 == rank2:
                continue
            if page1 != page2:
                print(
                    f"Error in row {i+1}: Mismatch in pages - expected {page1}, obtained {page2}"
                )
                flag = False
            if rank1 != rank2:
                print(
                    f"Error in row {i+1}: Mismatch in ranks - expected {rank1}, obtained {rank2}"
                )
                flag = False

        if set(list(vfile1.keys())) != set(list(vfile2.keys())):
            flag = False
            print("Mismatch in pages present:")
            print(
                f"Pages in v file 1 but not in v file 2: {list(set(list(vfile1.keys())) - set(list(vfile2.keys())))}"
            )
            print(
                f"Pages in v file 2 but not in v file 1: {list(set(list(vfile2.keys())) - set(list(vfile1.keys())))}"
            )

        sorted_pages1 = sorted(list(vfile1.keys()))
        sorted_pages2 = sorted(list(vfile2.keys()))

        if list(vfile1.keys()) != sorted_pages1:
            print(f"Error in pages: pages not sorted in v file 1")
            flag = False

        if list(vfile2.keys()) != sorted_pages2:
            print(f"Error in pages: pages not sorted in v file 2")
            flag = False

    if not flag:
        print("One or more issues found in v files: BAD OUTCOME")
    else:
        print("Both v files are the same: NO ISSUES FOUND")
