import pandas as pd
from sqlalchemy import create_engine
from fbprophet import Prophet


def forecast_weather(db_url):
    engine = create_engine(db_url)
    df = pd.read_sql("SELECT timestamp, temperature FROM weather_data", engine)
    df.rename(columns={"timestamp": "ds", "temperature": "y"}, inplace=True)
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)
    return forecast[["ds", "yhat"]]