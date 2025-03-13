from extract_weather_data import extract_weather_data
from transform_weather_data import transform_weather_data
from load_to_postgres import load_to_postgres
from forecast_weather import forecast_weather
from upload_to_cloud import upload_to_s3

if __name__ == "__main__":
    API_KEY = "your_api_key"
    DB_URL = "postgresql://user:password@host:port/dbname"
    AWS_ACCESS_KEY = "your_aws_access_key"
    AWS_SECRET_KEY = "your_aws_secret_key"
    BUCKET_NAME = "your_s3_bucket"
    S3_KEY = "processed_weather_data.csv"

    city = "New York"
    
    raw_data = extract_weather_data(city, API_KEY)
    if raw_data:
        transformed_data = transform_weather_data(raw_data)
        load_to_postgres(transformed_data, DB_URL)
        
        forecast = forecast_weather(DB_URL)
        forecast.to_csv("forecasted_weather.csv", index=False)
        
        upload_to_s3("forecasted_weather.csv", BUCKET_NAME, S3_KEY, AWS_ACCESS_KEY, AWS_SECRET_KEY)
    else:
        pass