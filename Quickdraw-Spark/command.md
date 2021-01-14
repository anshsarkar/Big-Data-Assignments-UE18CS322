## COPYING FILE TO HDFS

```bash
hdfs dfs -put Input/ /user/hadoop/input/quickdraw-spark
```

## STARTING HADOOP & SPARK

```bash
$HADOOP_HOME/sbin/start-all.sh
$SPARK_HOME/sbin/start-all.sh 
```

## SPARK-HDFS

```bash
spark-submit task1.py \
ambulance \
hdfs://localhost:9000/user/hadoop/input/quickdraw-spark/shape.csv \
hdfs://localhost:9000/user/hadoop/input/quickdraw-spark/shape_stat.csv
```

```bash
spark-submit task2.py \
ambulance 7 \
hdfs://localhost:9000/user/hadoop/input/quickdraw-spark/shape.csv \
hdfs://localhost:9000/user/hadoop/input/quickdraw-spark/shape_stat.csv
```

## SPARK

```bash
spark-submit task1.py ambulance Input/shape.csv Input/shape_stat.csv
```

```bash
spark-submit task2.py ambulance 7 Input/shape.csv Input/shape_stat.csv
```