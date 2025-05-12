from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.utils.dates import days_ago
import json

default_args = {
    'start_date': days_ago(1),
}

with DAG(
    dag_id='real_airbyte_dbt_weather_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    description='Runs Airbyte sync and DBT transformation for weather data'
) as dag:

    trigger_airbyte_sync = SimpleHttpOperator(
        task_id='trigger_airbyte_sync',
        method='POST',
        http_conn_id='airbyte_api',
        endpoint='api/v1/connections/sync',
        headers={"Content-Type": "application/json"},
        data=json.dumps({"connectionId": "c9346af9-0bcf-4576-a657-b5e00a3e8b1e"})
    )

    run_dbt_models = BashOperator(
        task_id='run_dbt_models',
        bash_command="""
        cd /usr/app && dbt run --profiles-dir /root/.dbt
        """,
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge"
    )

    trigger_airbyte_sync >> run_dbt_models
