# WeatherFlow ETL

## Project Overview
WeatherFlow ETL is an **end-to-end ETL pipeline** that collects, transforms, stores, and forecasts weather data. The pipeline is automated using **Apache Airflow** and integrates with **PostgreSQL** for structured storage and **AWS S3** for cloud-based processed data storage.

## Key Features
- **Extract**: Fetches real-time weather data from OpenWeatherMap API.
- **Transform**: Cleans and enhances data, including moving averages for trend analysis.
- **Load**: Stores weather data in a PostgreSQL database.
- **Forecast**: Uses Facebook Prophet for weather trend predictions.
- **Automate**: Managed with Apache Airflow for scheduled execution.
- **Cloud Storage**: Uploads processed data to AWS S3 for easy access.

---

## Tech Stack
- **Programming Language**: Python
- **Data Processing**: Pandas, SQLAlchemy
- **Database**: PostgreSQL
- **Forecasting**: Facebook Prophet
- **Cloud Services**: AWS S3, OpenWeatherMap API
- **Automation**: Apache Airflow
- **Other**: Requests, Boto3 (AWS SDK)

---

## Installation & Setup
1️. Clone the Repository
```bash
  git clone https://github.com/yourusername/weatherflow-etl.git
  cd weatherflow-etl
```
2. Set Up a Virtual Environment
```bash
  python3 -m venv venv
  source venv/bin/activate  # On macOS/Linux
  venv\Scripts\activate     # On Windows
```
3. Install Dependencies
```bash
  pip install -r requirements.txt
```
4. Set Up PostgreSQL Database
Install PostgreSQL if not already installed.
Create a new database:
```sql
  CREATE DATABASE weatherflow;
  Update config.py with your PostgreSQL connection details.
```
5. Configure API Keys & AWS Credentials
Edit the config.py file:

```python
  API_KEY = "your_openweathermap_api_key"
  DB_URL = "postgresql://user:password@host:port/weatherflow"
  AWS_ACCESS_KEY = "your_aws_access_key"
  AWS_SECRET_KEY = "your_aws_secret_key"
  BUCKET_NAME = "your_s3_bucket"
```
## Running the Pipeline
- **Option 1**: Manual Execution
Run the entire pipeline sequentially using:

```bash
  python main.py
```  
- **Option 2:** Automated Execution with Airflow
1️. Start the Airflow Scheduler & Web Server
```bash
  airflow db init
  airflow users create --username admin --firstname John --lastname Doe --role Admin --email admin@example.com --password admin
  airflow webserver --port 8080
  airflow scheduler
```
2️. Add DAG to Airflow
Ensure your DAG file ```weather_etl_dag.py``` is inside the Airflow DAGs folder ```(~/airflow/dags/)```. The DAG should now be visible in the Airflow UI at:

```arduino
  http://localhost:8080
```
Activate the WeatherFlow ETL DAG to begin automation.

## Forecasting Output
1. Uses Facebook Prophet to predict weather trends for the next 7 days.
2. Outputs predictions as a CSV file (forecasted_weather.csv).
3. Forecast data is automatically uploaded to AWS S3.

## License
This project is licensed under the MIT [License](LICENSE).

