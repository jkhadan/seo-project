import requests
api_key = 'd067498f6406a5a7298364140f4c8801'
symbol = 'AAPL'

response = requests.get(url=f'https://api.marketstack.com/v2/eod?access_key={api_key}&symbols={symbol}')

print(response.json())