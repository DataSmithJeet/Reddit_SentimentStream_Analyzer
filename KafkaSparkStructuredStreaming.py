from pyspark import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import from_json, col

schema = StructType([
    StructField("title", StringType(), True),
    StructField("score", StringType(), True),
    StructField("id", StringType(), True),
    StructField("url", StringType(), True),
    StructField("comms_num", StringType(), True),
    StructField("created", StringType(), True)
])

# Create a SparkSession
spark = SparkSession \
    .builder \
    .appName("KafkaRedditStream") \
    .config("spark.driver.host", "localhost") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Create a DataFrame representing the stream of input lines from connection to kafka:19092
reddit_raw_df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:19092") \
    .option("subscribe", "reddit_data_topic") \
    .option("startingOffsets", "earliest") \
    .option("maxOffsetsPerTrigger", "100") \
    .load()

reddit_raw_df.printSchema()

# Cast the value column in the streaming DataFrame as a STRING
reddit_string_df = reddit_raw_df.selectExpr("CAST(value AS STRING)").select(from_json(col("value"), schema).alias("reddit_data")).select("reddit_data.*")

# write the stream to console
query = reddit_string_df.writeStream.outputMode("append").format("console").start()

# wait for the stream to finish
query.awaitTermination()