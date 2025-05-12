from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

with DAG(dag_id='mock_airbyte_weather_dag',
         start_date=datetime(2025, 5, 1),
         schedule_interval='@daily',
         catchup=False) as dag:

    start = DummyOperator(task_id='start')
    extract = DummyOperator(task_id='airbyte_sync')
    transform = DummyOperator(task_id='dbt_run')
    end = DummyOperator(task_id='end')

    start >> extract >> transform >> end
