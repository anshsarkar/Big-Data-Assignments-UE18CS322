import sys
from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext("local", "task-1")
sql_context = SQLContext(sc)

word, _, df_path = sys.argv[1:]
df = sql_context.read.csv(df_path, header=True)
df = df.filter(df.word == word) # transformation

counts_by_rec = df.groupBy(df.recognized).agg(
    {"Total_Strokes": "avg"}).collect()

num_items = len(counts_by_rec)
if num_items > 0:
    counts_by_rec = sorted(list(map(lambda x: (x[0], x[1]), counts_by_rec)))
    output_dict = {"True": 0, "False": 0}

    for status, avg in counts_by_rec:
        output_dict[status] = avg

    print(round(output_dict["True"], 5))
    print(round(output_dict["False"], 5))
else:
    print("0.00000")
    print("0.00000")