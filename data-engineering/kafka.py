import csv
import json
from kafka import KafkaProducer

# Kafka Producer 생성
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",  # Kafka 브로커 주소 설정
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # 메시지 직렬화 방식 설정
)

file_path = "../raw_data/train/1000_chg.csv"
with open(file_path, newline='', encoding='utf-8') as file:
    data = csv.reader(file)
    headers = next(data)

    for row in data:
        common  = {
            'Date': row[0], 
            'Time': row[1],
            'SerialNumber': row[2]
        }

        BMS = {**common}
        for i in range(3, 23):
            BMS[headers[i]] = row[i]
        producer.send('bms_data', value=BMS)

        BCV = {**common}
        for i in range(23, 199):
            BCV[headers[i]] = row[i]
        producer.send('bcv_data', value=BCV)

        BMT = {**common}
        for i in range(199, 231):
            BMT[headers[i]] = row[i]
        producer.send('bmt_data', value=BMT)
