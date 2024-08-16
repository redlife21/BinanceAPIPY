import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

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

def plot_line_chart(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['Close'], label='Close Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('BTC/USDT Close Price Line Chart')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

df = fetch_klines('BTCUSDT', '1m', 50)
plot_line_chart(df)