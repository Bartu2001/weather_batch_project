from airflow import DAG
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1)
}

with DAG(
    dag_id='real_airbyte_to_dbt_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    description='Trigger Airbyte then run DBT in container'
) as dag:

    # 1. Airbyte Sync
    airbyte_sync = AirbyteTriggerSyncOperator(
        task_id='airbyte_sync',
        airbyte_conn_id='airbyte_connection',
        connection_id='c9346af9-0bcf-4576-a657-b5e00a3e8b1e',
        asynchronous=False,
        timeout=3600,
        wait_seconds=5,
    )

    # 2. DBT Run inside container
    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='docker exec weather_dbt dbt run --project-dir /usr/app --profiles-dir /root/.dbt'
    )

    airbyte_sync >> dbt_run
