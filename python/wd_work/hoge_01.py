import requests

url = 'https://example.com/'

response = requests.get(url)

print(response)
# <Response [200]>

print(type(response))
# <class 'requests.models.Response'>

print(type(response.headers))
# <class 'requests.structures.CaseInsensitiveDict'>

print(response.headers['content-type'])
# text/html

#print(response.text)




