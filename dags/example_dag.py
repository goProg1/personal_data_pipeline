from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from scripts.etl_pipeline import main as etl_main

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2026, 1, 1),
    'retries': 1
}

with DAG('example_etl_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    run_etl = PythonOperator(
        task_id='run_etl_pipeline',
        python_callable=etl_main
    )