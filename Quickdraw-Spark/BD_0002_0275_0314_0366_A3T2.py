import sys
from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext("local", "task-2")
sql_context = SQLContext(sc)

word, k, df_path_1, df_path_2 = sys.argv[1:]
k = int(k)

df1 = sql_context.read.csv(df_path_1, header=True)
df1 = df1.filter(df1.word == word)

df1 = df1.repartition(df1.key_id)  #Co partition

df2 = sql_context.read.csv(df_path_2, header=True)
df2 = df2.filter((df2.word == word) & (df2.Total_Strokes <= k)
                 & (df2.recognized == "False"))

df2 = df2.repartition(df2.key_id)  #Co partition

joined_df = df1.join(df2, df1.key_id == df2.key_id)
counts_by_rec = joined_df.groupBy(joined_df.countrycode).agg(
    {"countrycode": "count"}).collect()
counts_by_rec = sorted(list(map(lambda x: (x[0], x[1]), counts_by_rec)))


if len(counts_by_rec) == 0:
    print(0)
else:
    for country_code, count in counts_by_rec:
        if count != 0:
            print(f"{country_code},{count}")
