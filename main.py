import requests
import sys
import sqlalchemy as db
import pandas as pd

api_key = sys.argv[1]
symbol = 'AAPL'

response = requests.get(url=f'https://api.marketstack.com/v2/eod?access_key={api_key}&symbols={symbol}')

data = response.json()['data']

# print('Apple (AAPL): Stock Closing Report')
# for a in data:
#   print(f'Date: {a["date"]} Close Price: {a["close"]}')

# Day 2
dataframe = pd.DataFrame(data)
engine = db.create_engine('sqlite:///data_base_name.db')
dataframe.to_sql('table_name', con=engine, if_exists='replace', index=False)
with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM table_name;")).fetchall()
   print(pd.DataFrame(query_result))