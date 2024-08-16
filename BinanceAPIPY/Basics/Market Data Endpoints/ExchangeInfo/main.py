import requests
import csv
import os

url = 'https://api.binance.com/api/v3/exchangeInfo'
response = requests.get(url)
data = response.json()
current_directory = os.getcwd()
csv_file_name = os.path.join('exchange_info.csv')

with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file) #create a writer

    #here is titles
    writer.writerow([
        'symbol', 'status', 'baseAsset', 'baseAssetPrecision',
        'quoteAsset', 'quotePrecision', 'quoteAssetPrecision',
        'icebergAllowed', 'ocoAllowed', 'isSpotTradingAllowed', 'isMarginTradingAllowed'
    ])

    #loop for all symbols
    for symbol_info in data['symbols']:
        writer.writerow([
            symbol_info['symbol'],
            symbol_info['status'], #Trading mean is avaible for trade, break is not avaible for trade
            symbol_info['baseAsset'], 
            symbol_info['baseAssetPrecision'],
            symbol_info['quoteAsset'],
            symbol_info['quotePrecision'],
            symbol_info['quoteAssetPrecision'],
            symbol_info['icebergAllowed'],
            symbol_info['ocoAllowed'],
            symbol_info['isSpotTradingAllowed'],
            symbol_info['isMarginTradingAllowed']
        ])

print(f"Data has been written to {csv_file_name}")