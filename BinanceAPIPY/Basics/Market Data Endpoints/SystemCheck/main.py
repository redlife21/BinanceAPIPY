import requests

url = 'https://api.binance.com//sapi/v1/system/status'
response = requests.get(url)
data = response.json()

print(data)

#status = 0 is normal, 1 is maintenance     