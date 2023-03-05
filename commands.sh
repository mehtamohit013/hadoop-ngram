#!/usr/bin/env bash
# The following commands evaluate the bigram probablity and what is the most probable word after "united states"

hdfs dfs -rm -r output/unigram;
    mapred streaming \
    -file /home/mm12318_nyu_edu/HW1/unigram_mapper.py -file /home/mm12318_nyu_edu/HW1/unigram_reducer.py \
    -input hw1.2/* -output output/unigram \
    -mapper "python unigram_mapper.py" -reducer "python unigram_reducer.py";

hdfs dfs -rm -r output/bigram;
    mapred streaming \
    -file /home/mm12318_nyu_edu/HW1/bigram_mapper.py -file /home/mm12318_nyu_edu/HW1/unigram_reducer.py \
    -input hw1.2/* -output output/bigram \
    -mapper "python bigram_mapper.py" -reducer "python unigram_reducer.py";

hdfs dfs -rm -r output/uni_wc;
    mapred streaming \
    -file /home/mm12318_nyu_edu/HW1/unigram_wc_mapper.py -file /home/mm12318_nyu_edu/HW1/unigram_wc_reducer.py \
    -input output/unigram/* -output output/uni_wc \
    -mapper "python unigram_wc_mapper.py" -reducer "python unigram_wc_reducer.py";

hdfs dfs -rm -r output/bi_wc ;\
    mapred streaming \
    -file /home/mm12318_nyu_edu/HW1/bigram_wc_mapper.py -file /home/mm12318_nyu_edu/HW1/unigram_wc_reducer.py \
    -input output/bigram/* -output output/bi_wc \
    -mapper "python bigram_wc_mapper.py" -reducer "python unigram_wc_reducer.py";

hdfs dfs -rm -r output/bigram_prob;\
    c1=$(hdfs dfs -cat /output/uni_wc/*);c2=$(hdfs dfs -cat /output/bi_wc/*);\
    mapred streaming \
    -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
    -D stream.num.map.output.key.fields=2 \
    -D mapred.text.key.partitioner.options=-k1 \
    -D mapred.text.key.comparator.options=-k2,2n \
    -file /home/mm12318_nyu_edu/HW1/probablity_mapper.py -file /home/mm12318_nyu_edu/HW1/probablity_reducer.py \
    -input output/unigram/* -input output/bigram/* -output output/conditional_prob \
    -mapper "python probablity_mapper.py" -reducer "python probablity_reducer.py --uni $c1 --bi $c2";

hdfs dfs -rm -r output/bonus;\
mapred streaming \
-file /home/mm12318_nyu_edu/HW1/bonus_mapper.py -file /home/mm12318_nyu_edu/HW1/bonus_reducer.py \
-input hw1.2/* -output output/bonus \
-mapper "python bonus_mapper.py" -reducer "python bonus_reducer.py";