import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    df = df[['timestamp', 'close']]
    df.columns = ['Date', 'Close']
    df['Close'] = df['Close'].astype(float)
    
    return df

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def plot_line_chart_with_sma(df, sma):
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['Close'], label='Close Price')
    plt.plot(df['Date'], sma, label=f'SMA {period} Period', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('BTC/USDT Close Price with SMA Line Chart')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

df = fetch_klines('BTCUSDT', '1m', 500)
period = 10 
sma = calculate_sma(df['Close'], period)
plot_line_chart_with_sma(df, sma)