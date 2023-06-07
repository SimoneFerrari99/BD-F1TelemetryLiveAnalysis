# Set up e Avvio del progetto
# Kafka server on Docker Container
-   Installare docker
-   Creare il docker-compose
-   Caricare i volumi: `docker-compose -f ./config/docker-compose.yml up -d`
-   Eseguire Kafka: `docker exec -it kafka /bin/sh`

# Kafka Topic
-   Creare il topic: `kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic input_telemetry`
-   Verificare che il topic esista: `kafka-topics.sh --list --zookeeper zookeeper:2181`

# VENV for Python's Libraries
-   Creare venv python: `python3 -m venv venv`
-   Attivare il venv:
    -   Windows: `env\Scripts\activate`
    -   Linux/MacOS: `source venv/bin/activate`

# Kafka Dependencies
-   Installare libreria Kafka: `pip install kafka-python`

# Jupyter Dependenies e avvio
-   Installare Jupyter Notebook: `pip install jupyter notebook`
-   Avvio di jupyther-lab: `jupyter-lab`

# Avvio del progetto
-   Avviare container docker
-   Creare topic kafka
-   Creare venv
-   Scaricare dipendenze python
-   Attivare venv
-   Avviare su un terminale il procuer: `python3 02Producer_CarSimulation/producer.py`
-   Avviare Jupyther-lab (se serve recupero del file telemetria): `jupyter-lab`
-   Avviare su un secondo terminale il consumer: `spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.2 consumerSpark.py`
-   Avviare su un terzo terminale lo store process: `python3 04Visualization/store.py`
-   Avviare la dashboard grafana e visualizzare i dati
