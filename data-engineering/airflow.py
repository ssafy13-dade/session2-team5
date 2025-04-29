from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',  # 이 DAG의 소유자 (기록 용도)
    'depends_on_past': False,  # 이전 실행 성공 여부에 따라 실행할지 여부 (False면 상관 없음)
    'start_date': datetime(2025, 4, 24),  # DAG 시작 날짜 (이전 날짜는 실행 안 됨)
    'retries': 1,  # 실패 시 재시도 횟수
    'retry_delay': timedelta(minutes=5),  # 재시도 간격
}

dag = DAG(
    dag_id='kafka_spark_pipeline',
    default_args=default_args,
    schedule_interval=None,  # 수동 실행. 필요 시 '0 * * * *'처럼 설정
    catchup=False,
)

# Kafka Producer 실행 태스크
kafka_producer = BashOperator(
    task_id='kafka_producer',
    bash_command="""
        source /opt/airflow/dags/venv/data-pjt/bin/activate
        /opt/airflow/dags/venv/data-pjt/bin/python /opt/airflow/dags/project/kafka_producer.py
    """
,
    dag=dag,
)

# Spark Consumer 실행 태스크
spark_consumer = BashOperator(
    task_id='spark_consumer',
    bash_command=(
        'spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.4 '
        '/opt/airflow/dags/project/spark_consumer.py'
    ),
    dag=dag,
)

# 의존 관계 설정
kafka_producer >> spark_consumer
