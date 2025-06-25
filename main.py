import requests
import sys

api_key = sys.argv[1]
symbol = 'AAPL'

response = requests.get(url=f'https://api.marketstack.com/v2/eod?access_key={api_key}&symbols={symbol}')

data = response.json()['data']

print('Apple (AAPL): Stock Closing Report')
for a in data:
  print(f'Date: {a["date"]} Close Price: {a["close"]}')