import requests
import pprint

headers = {
    'X-Naver-Client-Id': 'SZEQTRIMTjOniRYdBdpG',
    'X-Naver-Client-Secret': 'ZzQs2QTnbO',
}

payload = {
    'query': '파이썬',
    'display': 100
}

url = 'https://openapi.naver.com/v1/search/blog'

res = requests.get(url, headers=headers, params=payload)
print('request senede..')
#print(res.json())



result = res.json()['items'][2]['title']
print(result)

