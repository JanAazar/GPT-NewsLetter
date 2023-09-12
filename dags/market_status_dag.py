from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from src.market_status import get_market_status

with DAG('market_status_dag', description='market_status_dag_schedule',
          schedule_interval='1 11 * * 1-5',  # Change to run every minute
          start_date=datetime(2023, 8, 20), catchup=False) as dag:

    @task
    def run_market_status():
        get_market_status()
    
    run_market_status_task = run_market_status()

    run_market_status_task


