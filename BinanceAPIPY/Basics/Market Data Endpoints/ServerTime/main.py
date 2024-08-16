import requests
from datetime import datetime

url = 'https://api.binance.com/api/v3/time'
response = requests.get(url)
data = response.json()
server_time = data['serverTime']
server_time_dt = datetime.fromtimestamp(server_time / 1000.0)

print(f"Server Time (Unix timestamp): {server_time}")
print(f"Server Time (Local time): {server_time_dt.strftime('%Y-%m-%d %H:%M:%S')}")