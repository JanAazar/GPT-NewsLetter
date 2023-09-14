from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from src.letter_creation import create_letter
from src.logger import logging

with DAG('letter_creation_dag', description='data_finder_dag_schedule',
          schedule_interval='50 14 * * 1-5',  # runs at 11:00 AM every day
          start_date=datetime(2023, 9, 7), catchup=False) as dag:

    @task
    def run_letter_creation():
        with open(f"dags//src//market_status.txt", "r") as file:
            market_status = file.read()
        if market_status == "open":        
            create_letter()
        else:
            logging.info("Market is closed")
    
    run_letter_creation_task = run_letter_creation()

    run_letter_creation_task


