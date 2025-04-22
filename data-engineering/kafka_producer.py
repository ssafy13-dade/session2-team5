import csv
import json
from kafka import KafkaConsumer, KafkaProducer

# Kafka Producer 생성
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",  # Kafka 브로커 주소 설정
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # 메시지 직렬화 방식 설정
)

# 파일은 처리하지 않은 파일을 순서대로 처리할 수 있게 선택하는 방법을 강구할 것
file_path = "../raw_data/train/1000_chg.csv"

# Kafka로 send
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

# # Test Kafka Consumer 생성
# consumer = KafkaConsumer(
# 	'bms_data',   # 구독할 토픽 설정 
#     'bcv_data',
#     'bmt_data',
#     bootstrap_servers="localhost:9092",   # Kafka 브로커 주소 설정
#     auto_offset_reset="earliest",   # 오프셋 초기화 방식 설정
#     enable_auto_commit=True,   # 자동 오프셋 커밋 여부 설정
# )

# # json.loads 쓰면 decode한 내용을 바로 key: value로 접근 가능(안하면 문자열 형태)
# for message in consumer:
#     print(f"[{message.topic}] {message.value.decode('utf-8')}")
