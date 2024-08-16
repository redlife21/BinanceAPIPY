import requests
import pandas as pd
import numpy as np

def fetch_klines(symbol, interval, limit):
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}'
    response = requests.get(url)
    data = response.json()
    
    df = pd.DataFrame(data, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'number_of_trades',
        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
    ])
    
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df = df[['timestamp', 'open', 'high', 'low', 'close', 'volume']]
    df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']

    df['Open'] = df['Open'].astype(float)
    df['High'] = df['High'].astype(float)
    df['Low'] = df['Low'].astype(float)
    df['Close'] = df['Close'].astype(float)
    df['Volume'] = df['Volume'].astype(float)

    date_array = df['Date'].values
    open_array = df['Open'].values
    high_array = df['High'].values
    low_array = df['Low'].values
    close_array = df['Close'].values
    volume_array = df['Volume'].values
    
    return date_array, open_array, high_array, low_array, close_array, volume_array

date_array, open_array, high_array, low_array, close_array, volume_array = fetch_klines('BTCUSDT', '1m', 50)