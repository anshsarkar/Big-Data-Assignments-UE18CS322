import sys

task, file1, file2 = sys.argv[1:]

with open (file1) as f:
    print(f"Reading {file1}")
    content1 = f.read().strip().split("\n")

with open (file2) as f:
    print(f"Reading {file2}")
    content2 = f.read().strip().split("\n")

len1 = len(content1)
len2 = len(content2)

flag = True

print("Initiating checks...")

if len1 != len2:
    flag = False
    print(f"Mismatch in rows: Expected {len1}, obtained {len2}")
    s1 = set(content1)
    s2 = set(content2)
    s1_s2 = s1-s2
    s2_s1 = s2-s1

    if s1_s2:
        print("Items in file 1 not in file 2:")
        for item in s1_s2:
            print(item)
    
    if s2_s1:
        print("Items in file 2 not in file 1:")
        for item in s2_s1:
            print(item)
    
else:
    print("Equal number of items found...")
    if task == '1':
        for i in range(len1):
            avg1 = content1[i]
            avg2 = content2[i]
            if avg1!=avg2:
                print(f"Error: Expected {avg1}, obtained {avg2}")
                flag = False

    if task == '2':
        countries_1 = [i.split(",")[0] for i in content1]
        countries_2 = [i.split(",")[0] for i in content2]

        if countries_1 != sorted(countries_1):
            print("Error: Country Codes in file 1 aren't sorted")
            flag = False

        if countries_2 != sorted(countries_2):
            print("Error: Country Codes in file 2 aren't sorted")
            flag = False

        for i in range(len1):
            country1, count1 = content1[i].split(",")
            country2, count2 = content2[i].split(",")
            if country1 != country2 and count1 != count2:
                print(f"Error: Expected {(country1, count1)}, obtained {(country2, count2)}")
                flag = False

print("Check completed.")

if flag:
    print(f"Result: PASSED")

else:
    print(f"Result: FAILED")

    