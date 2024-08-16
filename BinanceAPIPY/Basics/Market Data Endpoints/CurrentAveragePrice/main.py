import requests
import os
import csv

url = 'https://api.binance.com/api/v3/avgPrice'

params = {
    'symbol': 'BTCUSDT'
}

response = requests.get(url, params=params)
data = response.json()
current_directory = os.getcwd()
csv_file = os.path.join(current_directory, 'avg_price.csv')

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(['mins', 'price'])

    writer.writerow([data['mins'], data['price']])

print(f"Data has been written to {csv_file}")