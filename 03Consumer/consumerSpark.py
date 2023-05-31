# File che si occupa di leggere i dati dal topic Kafka (topic input_telemetry) in modo continuo e di inviarli in output a Kafka (topic spark_output)

# Import necessari
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Costanti relative a Kafka
KAFKA_TOPIC_NAME = "input_telemetry"
OUTPUT_KAFKA_TOPIC_NAME = "spark_output"
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
CHECKPOINT_LOCATION = "./checkpoint"

if __name__ == "__main__":
    # STEP 1 : Crezione di una sessione Spark
    spark = (
        SparkSession.builder.appName("Kafka Pyspark Streamin Learning")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("OFF")

    # STEP 2 : Letture dei dati da Kafka in formato streaming
    sampleDataframe = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS)
        .option("subscribe", KAFKA_TOPIC_NAME)
        .option("startingOffsets", "latest")
        .load()
    )

    # STEP 3 : Trasformazione dei dati
    # Creazione dello schema dei dati
    # schema = StructType(
    #     [
    #         StructField("Time", StringType()),
    #         StructField("RPM", IntegerType()),
    #         StructField("Speed", IntegerType()),
    #         StructField("nGear", IntegerType()),
    #         StructField("Throttle", IntegerType()),
    #         StructField("Brake", IntegerType()),
    #         StructField("DRS", IntegerType()),
    #         StructField("Distance", FloatType()),
    #     ]
    # )
    # Lo schema viene applicato ai dati letti da Kafka e vengono selezionati solo i campi che ci interessano (tutti)

    # STEP 4 : Scrittura dei dati in output
    sampleDataframe.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
        .writeStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS) \
        .option("topic", OUTPUT_KAFKA_TOPIC_NAME) \
        .option("checkpointLocation", CHECKPOINT_LOCATION) \
        .start() \
        .awaitTermination()
    
    # Questo codice serve per stampare i dati in console (utile per debug), ma non è necessario per il progetto. 
    # Se si vuole utilizzare, basta decommentare le righe sotto e commentare quelle sopra relative allo step 4.
    # sampleDataframe.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
    #     .writeStream \
    #     .format("console") \
    #     .outputMode("append") \
    #     .start() \
    #     .awaitTermination() \