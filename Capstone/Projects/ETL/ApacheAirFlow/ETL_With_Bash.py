# Import the libraries
from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow.models import DAG
# Operators; you need this to write tasks!
from airflow.operators.python import PythonOperator
from airflow.operators.bash_operator import BashOperator

# This makes scheduling easy
from airflow.utils.dates import days_ago
import requests

# Define DAG arguments
default_args = {
    'owner': 'siri',
    'start_date': days_ago(0),
    'email': ['siri@sirisoftware.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'ETL_toll_data',
    default_args=default_args,
    description='Apache Final Assignment',
    schedule_interval=timedelta(days=1),
)

unzip_data = BashOperator(
   task_id = 'unzip_data',
   bash_command='tar -xzvf /home/project/airflow/dags/finalassignment/tolldata.tar -C /home/project/airflow/dags/finalassignment',
   dag=dag,
)

extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='cut -d":" -f1,2,3,4 /home/project/airflow/dags/finalassignment/vehicle_data.csv > /home/project/airflow/dags/finalassignment/csv_data.csv',
    dag=dag,
)

extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command='cut -d":" -f1,2,3,4 /home/project/airflow/dags/finalassignment/vehicle_data.csv > /home/project/airflow/dags/finalassignment/tsv_data.csv',
    dag=dag,
)

extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command='cut -c1-3,10-12 /home/project/airflow/dags/finalassignment/payment-data.txt | sed "s/\\s\\+/,/g" > /home/project/airflow/dags/finalassignment/fixed_width_data.csv',
    dag=dag,
)

consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command='paste -d"," /home/project/airflow/dags/finalassignment/csv_data.csv /home/project/airflow/dags/finalassignment/tsv_data.csv /home/project/airflow/dags/finalassignment/fixed_width_data.csv > /home/project/airflow/dags/finalassignment/extracted_data.csv',
    dag=dag,
)

transform_and_load = BashOperator(
    task_id='transform_data',
    bash_command='tr ":" "," < /home/project/airflow/dags/finalassignment/extracted-data.csv > /home/project/airflow/dags/finalassignment/transformed-data.csv',
    dag=dag,
)