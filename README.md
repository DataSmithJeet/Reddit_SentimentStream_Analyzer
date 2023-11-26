# Reddit_SentimentStream_Analyzer

# how to see data in the kafka topic

# docker exec -it kafka /bin/bash
# cd  /bin/
# Run the below script to see the data in the topic
# ./kafka-console-consumer --bootstrap-server localhost:9092 --topic reddit_data_topic --from-beginning


# how to run the spark job
# docker cp KafkaSparkStructuredStreaming.py spark_master:/opt/bitnami/spark/
# docker exec -it spark_master /bin/bash
# spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1 KafkaSparkStructuredStreaming.py
