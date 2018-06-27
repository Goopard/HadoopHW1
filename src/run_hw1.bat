ssh root@localhost -p 2222 command mkdir /usr/jobs/auto_test/
ssh root@localhost -p 2222 command mkdir /usr/jobs/auto_test/input/

scp -P 2222 largest_words_job.py root@localhost:/usr/jobs/auto_test/test.py
scp -P 2222 ..\input\input0.txt root@localhost:/usr/jobs/auto_test/input/test0.txt
scp -P 2222 ..\input\input1.txt root@localhost:/usr/jobs/auto_test/input/test1.txt
scp -P 2222 ..\input\input2.txt root@localhost:/usr/jobs/auto_test/input/test2.txt

ssh root@localhost -p 2222 command hadoop fs -copyFromLocal /usr/jobs/auto_test/input/* /user/raj_ops/

ssh root@localhost -p 2222 command "python3 /usr/jobs/auto_test/test.py -r hadoop hdfs:///user/raj_ops/ --hadoop-streaming-jar=/usr/hdp/2.6.4.0-91/hadoop-mapreduce/hadoop-streaming.jar --number=5 > /usr/jobs/auto_test/output.txt"

scp -P 2222 root@localhost:/usr/jobs/auto_test/output.txt ..\output\output.txt

ssh root@localhost -p 2222 command rm -r /usr/jobs/auto_test
ssh root@localhost -p 2222 command hadoop fs -rm -skipTrash /user/raj_ops/*
