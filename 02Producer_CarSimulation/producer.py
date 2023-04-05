# File che si occupa di leggere i dati dalla telemetria dal .csv e di inviarli a Kafka (topic input_telemetry)

from time import sleep
from json import dumps
from kafka import KafkaProducer
from datetime import datetime
import csv

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'], 
    value_serializer=lambda x: dumps(x).encode('utf-8'),
    key_serializer=lambda x: dumps(x).encode('utf-8'))

with open('../01GetTelemetry/telemetry.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        
        else:
            rowData = {}
           
            rowData['Time'] = row[1].split(" ")[2]
            rowData['Time'] = datetime.strptime(rowData['Time'], '%H:%M:%S.%f') if "." in rowData['Time'] else datetime.strptime(rowData['Time'], '%H:%M:%S')
            rowData['Time'] = rowData['Time'].strftime('%H:%M:%S.%f')
           
            rowData['RPM'] = int(row[2])
            rowData['Speed'] = int(row[3])
            rowData['nGear'] = int(row[4])
            rowData['Throttle'] = int(row[5])
            rowData['Brake'] = 1 if (row[6] == "True") else 0
            rowData['DRS'] = 1 if (int(row[7]) == 12) else 0
            rowData['Distance'] = float(row[8])
            
            producer.send('input_telemetry', value=rowData)
            
            line_count += 1
            print(rowData)
            sleep(0.15) #0.15