import csv
import json
from kafka import KafkaProducer

# Kafka Producer 생성
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",  # Kafka 브로커 주소 설정
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # 메시지 직렬화 방식 설정
)

file_path = "../../raw_data/train/1000_chg.csv"
with open(file_path, newline='', encoding='utf-8') as file:
    data = csv.DictReader(file)
    for row in data:
        print(row)