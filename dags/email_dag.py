from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from src.email_creation import send_email
from src.auth import gmail_pass as password
from src.utils import get_date
from src.logger import logging



with DAG('email_dag', description='creating_email_dag_schedule',
          schedule_interval='1 19 * * 1-5',  # Change to run every minute
          start_date=datetime(2023, 8, 20), catchup=False) as dag:

    @task
    def run_email_creation():
        with open(f"dags//src//market_status.txt", "r") as file:    
            market_status = file.read()
        if market_status == "open":
            sender_email = "aazarjan15003@gmail.com"  # Replace with the sender's email address 

            subject = f"GPT-News Letter for {get_date()}"

            # Send the email
            send_email(sender_email, password, subject)
        else:
            logging.info("Market is closed")
        
    
    run_email_creation_task = run_email_creation()

    run_email_creation_task


