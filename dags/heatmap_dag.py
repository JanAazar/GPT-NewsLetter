from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from src.heatmap_downloader import download_image
from src.logger import logging

with DAG('heatmap_dag', description='data_finder_dag_schedule',
          schedule_interval='59 18 * * 1-5',  # runs at 11:00 AM every day
          start_date=datetime(2023, 9, 7), catchup=False) as dag:

    @task
    def run_download_image():
        with open(f"dags//src//market_status.txt", "r") as file:
            market_status = file.read()
        if market_status == "open":
            download_image()
        else:
            logging.info("Market is closed")

    run_download_image_task = run_download_image()

    run_download_image_task


