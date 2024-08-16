import requests
import csv
import os

url = 'https://api.binance.com/api/v3/trades'

parameters = {
    'symbol': 'BTCUSDT',  # Pair
    'limit': 25           # Order limit, default is 100
}

response = requests.get(url, params=parameters)
data = response.json()
current_directory = os.getcwd()
csv_file_name = os.path.join(current_directory, 'Recent_Trades.csv')

with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(['Trade ID', 'Price', 'Quantity', 'Quote Quantity', 'Timestamp', 'Is Buyer Maker', 'Is Best Match'])

    for trade in data:
        writer.writerow([
            trade['id'],
            trade['price'],
            trade['qty'],
            trade['quoteQty'],
            trade['time'],
            trade['isBuyerMaker'],
            trade['isBestMatch']
        ])

print(f"Data has been written to {csv_file_name}")