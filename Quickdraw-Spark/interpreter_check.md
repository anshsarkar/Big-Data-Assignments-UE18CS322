## TASK 1

```Python
word = "ambulance"
df_path = "Input/shape_stat.csv"

sql_context = SQLContext(sc)
df = sql_context.read.csv(df_path, header=True)
df_name = df.filter(df.word == word)

counts_by_rec = df_name.groupBy(df.recognized).agg({"Total_Strokes":"avg"}).collect()
num_items = len(counts_by_rec)
if num_items > 0:
    counts_by_rec = sorted(list(map(lambda x: (x[0], x[1]), counts_by_rec)))
    output_dict = {"True":0, "False":0}
    for status, avg in counts_by_rec:
        output_dict[status] = avg
    print(round(output_dict["True"], 5))
    print(round(output_dict["False"], 5))
else:
    print("0.00000")
    print("0.00000")
```

## TASK 2:

```Python
word = "ambulance"
k = 5
df_path_1 = "Input/shape.csv"
df_path_2 = "Input/shape_stat.csv"
sql_context = SQLContext(sc)
df1 = sql_context.read.csv(df_path_1, header=True)
df2 = sql_context.read.csv(df_path_2, header=True)
df1 = df1.filter(df1.word == word)
df2 = df2.filter((df2.word == word) & (df2.Total_Strokes < k) & (df2.recognized == "False"))
joined_df = df1.join(df2, df1.key_id == df2.key_id)
counts_by_rec = joined_df.groupBy(joined_df.countrycode).agg({"countrycode":"count"}).collect()
counts_by_rec = sorted(list(map(lambda x: (x[0], x[1]), counts_by_rec)))
for country_code, count in counts_by_rec:
    print(f"{country_code},{count}")
```