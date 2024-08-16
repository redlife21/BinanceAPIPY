import requests
import csv
import os

url = 'https://api.binance.com/api/v3/depth'

parameters = {
    'symbol': 'BTCUSDT',  # Pair
    'limit': 25           # Order limit, default is 100. taking 5 sell order and 5 buy order 
}

response = requests.get(url, params=parameters)
data = response.json()
current_directory = os.getcwd()
csv_file_name = os.path.join(current_directory, 'order_book_depth.csv')

with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(['Bids', ''])
    writer.writerow(['Price', 'Quantity'])

    for bid in data['bids']:
        writer.writerow(bid)

    writer.writerow([])

    writer.writerow(['Asks', ''])
    writer.writerow(['Price', 'Quantity'])

    for ask in data['asks']:
        writer.writerow(ask)

print(f"Data has been written to {csv_file_name}")