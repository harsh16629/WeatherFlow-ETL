import pandas as pd

def transform_weather_data(raw_data):
    df = pd.DataFrame([raw_data])
    df["temperature_moving_avg"] = df["temperature"].rolling(window=3).mean()
    return df.dropna()