from sqlalchemy import create_engine

def load_to_postgres(df, db_url):
    engine = create_engine(db_url)
    df.to_sql("weather_data", engine, if_exists="append", index=False)
    print("Data loaded to PostgreSQL successfully!")