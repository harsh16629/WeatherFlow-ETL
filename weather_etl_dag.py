from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from extract_weather_data import extract_weather_data
from transform_weather_data import transform_weather_data
from load_to_postgres import load_to_postgres
from forecast_weather import forecast_weather
from upload_to_cloud import upload_to_s3

# Configuration variables
API_KEY = "your_api_key"
DB_URL = "postgresql://user:password@host:port/dbname"
AWS_ACCESS_KEY = "your_aws_access_key"
AWS_SECRET_KEY = "your_aws_secret_key"
BUCKET_NAME = "your_s3_bucket"
S3_KEY = "processed_weather_data.csv"
CITY = "New York"

# Define default arguments for DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 13),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define DAG
dag = DAG(
    'weather_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline for real-time weather data processing and forecasting',
    schedule_interval=timedelta(days=1),
    catchup=False,
)

# Define Python tasks
def extract_task():
    return extract_weather_data(CITY, API_KEY)

def transform_task(ti):
    raw_data = ti.xcom_pull(task_ids='extract_weather')
    return transform_weather_data(raw_data)

def load_task(ti):
    transformed_data = ti.xcom_pull(task_ids='transform_weather')
    load_to_postgres(transformed_data, DB_URL)

def forecast_task():
    forecast = forecast_weather(DB_URL)
    forecast.to_csv("forecasted_weather.csv", index=False)

def upload_task():
    upload_to_s3("forecasted_weather.csv", BUCKET_NAME, S3_KEY, AWS_ACCESS_KEY, AWS_SECRET_KEY)

# Define DAG tasks
task_extract = PythonOperator(
    task_id='extract_weather',
    python_callable=extract_task,
    dag=dag,
)

task_transform = PythonOperator(
    task_id='transform_weather',
    python_callable=transform_task,
    provide_context=True,
    dag=dag,
)

task_load = PythonOperator(
    task_id='load_to_postgres',
    python_callable=load_task,
    provide_context=True,
    dag=dag,
)

task_forecast = PythonOperator(
    task_id='forecast_weather',
    python_callable=forecast_task,
    dag=dag,
)

task_upload = PythonOperator(
    task_id='upload_to_cloud',
    python_callable=upload_task,
    dag=dag,
)

# Task dependencies
task_extract >> task_transform >> task_load >> task_forecast >> task_upload
