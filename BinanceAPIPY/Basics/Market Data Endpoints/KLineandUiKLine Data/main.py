import requests
import csv
import os

# url = 'https://api.binance.com/api/v3/klines'
url = 'https://api.binance.com/api/v3/uiKlines' # If you are going to use it for the interface, it is more useful to use it, it is important for optimisation
parameters = {
    'symbol': 'BTCUSDT',  # Pair
    'interval': '1d',     # Timeframe s = second, m = minute, h = hour, d = day, w = week, m = month
    'limit': 25           # Candlestick count, Default is 500
}

response = requests.get(url, params=parameters)
data = response.json()
current_directory = os.getcwd()
csv_file_name = os.path.join(current_directory, 'data.csv')

with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 'Quote Asset Volume', 'Number of Trades', 'Taker Buy Base Asset Volume', 'Taker Buy Quote Asset Volume'])

    for kline in data:
        writer.writerow([
            kline[0],  # Open Time
            kline[1],  # Open
            kline[2],  # High
            kline[3],  # Low
            kline[4],  # Close
            kline[5],  # Volume
            kline[6],  # Close Time
            kline[7],  # Quote Asset Volume
            kline[8],  # Number of Trades
            kline[9],  # Taker Buy Base Asset Volume
            kline[10]  # Taker Buy Quote Asset Volume
        ])

print(f"Data has been written to {csv_file_name}")
