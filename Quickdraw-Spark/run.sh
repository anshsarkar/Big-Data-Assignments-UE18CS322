#!/bin/sh

# INSTRUCTIONS TO RUN SHELL SCRIPT AND GENERATE OUTPUT
    # Task 1: bash ./run.sh 1 <word> 
    # Task 2: bash ./run.sh 2 <word> <K>
    # The result is redirected to log(task number).txt

# SETTING UP FILE PATHS

    ## Each tester function has 2 blocks - 
        ### The first block is to generate outputs for the first script
        ### The second block is to generate outputs for the second script

    ## Replace task1.py in the first block to the first Task 1 Python script,
    ## and task1.py in the second block to the second Task 2 Python script.
    ## Additionally, remember to change the HDFS directory paths for the datasets.

TASK=$1
WORD=$2
K=$3

rm output*.txt
rm log*.txt

Task1_Test(){
    spark-submit task1.py \
    $WORD \
    hdfs://localhost:9000/user/hadoop/input/quickdraw-spark/shape.csv \
    hdfs://localhost:9000/user/hadoop/input/quickdraw-spark/shape_stat.csv > output1.txt

    spark-submit task1.py \
    $WORD \
    hdfs://localhost:9000/user/hadoop/input/quickdraw-spark/shape.csv \
    hdfs://localhost:9000/user/hadoop/input/quickdraw-spark/shape_stat.csv > output2.txt

    python3 check_output.py 1 output1.txt output2.txt > log1.txt
}

Task2_Test(){
    spark-submit task2.py \
    $WORD $K \
    hdfs://localhost:9000/user/hadoop/input/quickdraw-spark/shape.csv \
    hdfs://localhost:9000/user/hadoop/input/quickdraw-spark/shape_stat.csv > output1.txt

    spark-submit task2.py \
    $WORD $K \
    hdfs://localhost:9000/user/hadoop/input/quickdraw-spark/shape.csv \
    hdfs://localhost:9000/user/hadoop/input/quickdraw-spark/shape_stat.csv > output2.txt

    python3 check_output.py 2 output1.txt output2.txt > log2.txt
}

if [ $TASK == 1 ]
then
    Task1_Test

elif [ $TASK == 2 ]
then
    Task2_Test

else
    Task1_Test
    Task2_Test
fi