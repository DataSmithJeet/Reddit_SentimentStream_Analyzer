# Reddit_SentimentStream_Analyzer

# how to see data in the kafka topic

# docker exec -it {kafka container id} /bin/bash
# cd  /bin/
# Run the below script to see the data in the topic
# ./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic reddit-stream --from-beginning


# how to run the spark job
# docker exec -it {spark container id} /bin/bash
# cd /bin/ 
# spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1 KafkaSparkStructuredStreaming.py