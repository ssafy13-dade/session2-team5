from pyspark.sql import SparkSession
from pyspark.sql.types import MapType, StringType
from pyspark.sql.functions import from_json, col

# Spark 세션 생성
spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .getOrCreate()

# Kafka로부터 데이터 읽기
# 스트리밍 데이터라면 spark.readStreaming
df = spark.read \
    .format('kafka') \
    .option('kafka.bootstrap.servers', 'localhost:9092') \
    .option('subscribe', 'bms_data') \
    .option('startingOffsets', 'earliest') \
    .option("endingOffsets", "latest") \
    .load()

# Kafka의 binary 데이터를 문자열로 캐스팅
df_cast = df.selectExpr("CAST(value AS STRING) as json_str")

# 스키마 설정
schema = MapType(StringType(), StringType())

# json 문자열을 구조화
df_parsed = df_cast \
    .withColumn("data", from_json(col("json_str"), schema)) \
    .select("data.*")

# 출력
df_parsed.show()
