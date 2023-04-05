# File che simula un consumer che legge da Kafka i dati della telemetria e li stampa a video

from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

consumer = KafkaConsumer(
    'spark_output',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

client = MongoClient('mongodb+srv://simone:simone@progettobigdata.drysbtu.mongodb.net/?retryWrites=true&w=majority')
collection = client.telemetry.telemetry

for message in consumer:
    row = {}
    print("---------------------------------")
    print(message.value)
    print("---------------------------------")
    
    data = message.value
    row['Time'] = data['Time']
    row['RPM'] = data['RPM']
    row['Speed'] = data['Speed']
    row['nGear'] = data['nGear']
    row['Throttle'] = data['Throttle']
    row['Brake'] = data['Brake']
    row['DRS'] = data['DRS']
    row['Distance'] = float(data['Distance'])

    collection.insert_one(row)