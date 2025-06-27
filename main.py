import requests
import sys
import sqlalchemy as db
import pandas as pd

symbol = 'AAPL'

def get_api_key():
    if len(sys.argv) < 2:
        print("Usage: python main.py <API_KEY>")
        sys.exit(1)
    return sys.argv[1]

api_key = get_api_key()

def get_stock_data(symbol, api_key):
    url = f'https://api.marketstack.com/v2/eod?access_key={api_key}&symbols={symbol}'
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        sys.exit(1)
    return response.json()['data']

data = get_stock_data(symbol, api_key)

def print_stock_data(data):
    print(f'Apple (AAPL): Stock Closing Report')
    for entry in data:
        print(f'Date: {entry["date"]} Close Price: {entry["close"]}')

def save_and_print_data_to_db(data):
   dataframe = pd.DataFrame(data)
   engine = db.create_engine('sqlite:///data_base_name.db')
   dataframe.to_sql('table_name', con=engine, if_exists='replace', index=False)
   with engine.connect() as connection:
      query_result = connection.execute(db.text("SELECT * FROM table_name;")).fetchall()
      print(pd.DataFrame(query_result))