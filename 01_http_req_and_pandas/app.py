# modules
import requests
import json
from pandas.io.json import json_normalize

url = 'https://finance.naver.com/api/realtime.nhn?query=SERVICE_INDEX:KOSPI'
json_data = json.loads(requests.get(url).text)
df = json_normalize(json_data['result']['etfItemList'])

print(df)
