from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

KAFKA_TOPIC_NAME = "input_telemetry"
OUTPUT_KAFKA_TOPIC_NAME = "spark_output"
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
CHECKPOINT_LOCATION = "./checkpoint"

if __name__ == "__main__":
    # STEP 1 : creating spark session object
    spark = (
        SparkSession.builder.appName("Kafka Pyspark Streamin Learning")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("OFF")
    # STEP 2 : reading a data stream from a kafka topic
    sampleDataframe = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS)
        .option("subscribe", KAFKA_TOPIC_NAME)
        .option("startingOffsets", "latest")
        .load()
    )

    # sampleDataframe.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
    #     .writeStream \
    #     .format("console") \
    #     .outputMode("append") \
    #     .start() \
    #     .awaitTermination() \

    sampleDataframe.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
        .writeStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS) \
        .option("topic", OUTPUT_KAFKA_TOPIC_NAME) \
        .option("checkpointLocation", CHECKPOINT_LOCATION) \
        .start() \
        .awaitTermination()