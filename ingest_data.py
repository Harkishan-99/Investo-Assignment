import yaml
import pandas as pd
from sqlalchemy import create_engine

FILENAME = "HINDALCO_1D.csv"
df = pd.read_csv(FILENAME, parse_dates=[0])

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

connect_alchemy = "postgresql+psycopg2://%s:%s@%s/%s" % (
    config['DATABASE']['USERNAME'],
    config['DATABASE']['PASSWORD'],
    config['DATABASE']['HOST'],
    config['DATABASE']['DB']
)
engine = create_engine(connect_alchemy)
df.to_sql('price', engine, if_exists='replace', index=False)
