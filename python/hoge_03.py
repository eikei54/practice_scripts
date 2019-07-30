import requests
import pprint
import json

url = 'http://weather.livedoor.com/forecast/webservice/json/v1'

params = {'city': 130010}

r = requests.get(url, params=params)

print(r.headers['Content-Type'])
# application/json; charset=utf-8
