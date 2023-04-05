# Set up

# Kafka server on Docker Container

-   Install docker
-   Create docker-compose
-   Load volumes: `docker-compose -f ./config/docker-compose.yml up -d`
-   Execute Kafka: `docker exec -it kafka /bin/sh`

# Kafka Topic

-   Create topic: `kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic input_telemetry`
-   List all topic: `kafka-topics.sh --list --zookeeper zookeeper:2181`

# VENV for Python's Libraries

-   `cd kafkaInterface`
-   `python3 -m venv venv`
    -   Windows: `env\Scripts\activate`
    -   Linux/MacOS: `source venv/bin/activate`

# Kafka Dependencies

-   Kafka: `pip install kafka-python`

# Jupyter Dependenies

-   Notebook: `pip install jupyter notebook`

# Avvio

-   jupyther-lab: `jupyter-lab`
-   Creazione utenze:

# Avvio del progetto

-   Avviare container docker
-   Creare topic kafka
-   Creare venv
-   Scaricare dipendenze
-   Attivare venv
-   Avviare su un terminale il `python3 02Producer_CarSimulation/producer.py`
-   Avviare Jupyther-lab: `jupyter-lab`
-   Avviare su un secondo terminale il consumer `spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.2 consumerSpark.py`
-   Avviare la dashboard grafana e visualizzare `TBD`
