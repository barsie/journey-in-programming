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
import tarfile


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
    'process_web_lg',
    default_args=default_args,
    description='Capston Project Assignment',
    schedule_interval=timedelta(days=1),
)

# Define the path for the input and output files
input_file = 'accesslog.txt'
extracted_data = 'extracted-data.txt'
transformed_data = 'transformed.txt'
output_file = 'weblog.tar'


def download_data():
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/accesslog.txt"
    # Send a GET request to the URL
    with requests.get(url, stream=True) as response:
        # Raise an exception for HTTP errors
        response.raise_for_status()
        # Open a local file in binary write mode
        with open(input_file, 'wb') as file:
            # Write the content to the local file in chunks
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    print(f"File downloaded successfully: {input_file}")

# extract function
def extract_data():
    global input_file, extracted_data
    print("Inside Extract: Extracting IPs")
    # Read the contents of the file into a string
    with open(input_file, 'r') as infile, \
            open(extracted_data, 'w') as outfile:
        for line in infile:
            fields = line.split('#')
            if len(fields) >= 4:
                field_1 = fields[0]
                field_4 = fields[3]
                outfile.write(field_1 + "#" + field_4 + "\n")

# Transform function
def transform_data():
    global extracted_data, transformed_data
    ip_to_filter = "192.168.149.143"
    print("Inside Transform")
    with open(extracted_data, 'r') as infile, open(transformed_data, 'w') as outfile:
        for line in infile:
            if ip_to_filter not in line:
                processed_line = line.upper()
                outfile.write(processed_line)

# Data load
def load_data():
    global transformed_file, output_file
    print("Inside Load")
    with tarfile.open(output_file, "w") as tar:
        tar.add(transformed_file)
    print(f"{transformed_file} archived into {output_file}")

# Define the task named download to call the `download_data` function
download = PythonOperator(
    task_id='download',
    python_callable=download_data,
    dag=dag,
)

# Define the task named execute_extract to call the `extract_data` function
execute_extract = PythonOperator(
    task_id='extract',
    python_callable=extract_data,
    dag=dag,
)

# Define the task named execute_transform to call the `transform_data` function
execute_transform = PythonOperator(
    task_id='transform',
    python_callable=transform_data,
    dag=dag,
)

# Define the task named execute_load to call the `load_data` function
execute_load = PythonOperator(
    task_id='load',
    python_callable=load_data,
    dag=dag,
)

download >> execute_extract >> execute_transform >> execute_load
