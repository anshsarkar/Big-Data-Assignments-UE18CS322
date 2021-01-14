#!/bin/sh
CONVERGE=1
ITER=1
rm v v1 log*

$HADOOP_HOME/bin/hadoop dfsadmin -safemode leave
hdfs dfs -rm -r /user/hadoop/output/PageRank/task-* 

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-*streaming*.jar \
-mapper "'/home/hadoop/Desktop/big-data/PageRank/BD_0002_0275_0314_0366_mapper_t1.py'" \
-reducer "'/home/hadoop/Desktop/big-data/PageRank/BD_0002_0275_0314_0366_reducer_t1.py' '/home/hadoop/Desktop/big-data/PageRank/v'"  \
-input /user/hadoop/input/PageRank/web-Google.txt \
-output /user/hadoop/output/PageRank/task-1-output #has adjacency list


while [ "$CONVERGE" -ne 0 ]
do
	echo "############################# ITERATION $ITER #############################"
	$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-*streaming*.jar \
	-mapper "'/home/hadoop/Desktop/big-data/PageRank/BD_0002_0275_0314_0366_mapper_t2.py' '/home/hadoop/Desktop/big-data/PageRank/v'" \
	-reducer "'/home/hadoop/Desktop/big-data/PageRank/BD_0002_0275_0314_0366_reducer_t2.py'" \
	-input /user/hadoop/output/PageRank/task-1-output/part-00000 \
	-output /user/hadoop/output/PageRank/task-2-output
	touch v1
	hadoop fs -cat /user/hadoop/output/PageRank/task-2-output/part-00000 > "/home/hadoop/Desktop/big-data/PageRank/v1"
	CONVERGE=$(python3 check_conv.py $ITER>&1)
	ITER=$((ITER+1))
	hdfs dfs -rm -r /user/hadoop/output/PageRank/task-2-output/
	echo $CONVERGE
done
