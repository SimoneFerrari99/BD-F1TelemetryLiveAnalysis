# File che simula un consumer che legge da Kafka i dati della telemetria e li stampa a video

# Import necessari
from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

# Creazione del consumer di Kafka
consumer = KafkaConsumer(
    'spark_output',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

# Connessione al database MongoDB
client = MongoClient('mongodb+srv://simone:simone@progettobigdata.drysbtu.mongodb.net/?retryWrites=true&w=majority')
collection = client.telemetry.telemetry

# Lettura dei dati da Kafka e inserimento nel database MongoDB
for message in consumer:
    row = {} # Dizionario che contiene i dati da inviare a MongoDB

    # Stampa a video dei dati ricevuti da Kafka (utile per debug)
    print("---------------------------------")
    print(message.value)
    print("---------------------------------")
    
    # Inserimento dei dati nel dizionario
    data = message.value
    row['Time'] = data['Time']
    row['RPM'] = data['RPM']
    row['Speed'] = data['Speed']
    row['nGear'] = data['nGear']
    row['Throttle'] = data['Throttle']
    row['Brake'] = data['Brake']
    row['DRS'] = data['DRS']
    row['Distance'] = float(data['Distance'])

    # Inserimento dei dati nel database MongoDB
    collection.insert_one(row)