import pandas as pd
from sqlalchemy import create_engine
import yaml

# Load config
with open('config/config.yaml.example', 'r') as f:
    config = yaml.safe_load(f)

# Connect to PostgreSQL
engine = create_engine(
    f"postgresql+psycopg2://{config['postgres']['user']}:{config['postgres']['password']}@"
    f"{config['postgres']['host']}:{config['postgres']['port']}/{config['postgres']['database']}"
)

# Example ETL: Read CSV and load into PostgreSQL
df = pd.read_csv('data/example_data.csv')
df.to_sql('example_table', engine, if_exists='replace', index=False)
print("ETL completed successfully!")