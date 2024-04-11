## Kafka Topic Data Viewer

To view data in the Kafka topic `reddit_data_stream`, follow these steps:

1. Access the Kafka container:
    ```bash
    docker exec -it kafka /bin/bash
    ```

2. Navigate to the Kafka binary directory:
    ```bash
    cd /bin/
    ```

3. Run the following script to consume data from the topic:
    ```bash
    ./kafka-console-consumer --bootstrap-server localhost:9092 --topic reddit_data_stream --from-beginning
    ```

## Running the Spark Job

To run the Spark job `KafkaSparkStructuredStreaming.py`, use the following instructions:

1. Copy the Python script to the Spark master container:
    ```bash
    docker cp KafkaSparkStructuredStreaming.py spark_master:/opt/bitnami/spark/
    ```

2. Access the Spark master container:
    ```bash
    docker exec -it spark_master /bin/bash
    ```

3. Submit the Spark job using `spark-submit`, including the necessary packages:
    ```bash
    spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1 KafkaSparkStructuredStreaming.py
    ```
