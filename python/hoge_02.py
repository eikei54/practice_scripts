import requests

url = 'https://www.google.co.jp/search'

params = {'q': '$BF|K\BeI=(B', 'tbm': 'nws'}

r = requests.get(url, params=params)

print(r.url)
# https://www.google.co.jp/search?q=%E6%97%A5%E6%9C%AC%E4%BB%A3%E8%A1%A8&tbm=nws


