from requests import Request
from requests import Session

s = Session()


headers = {
    'X-Naver-Client-Id': 'SZEQTRIMTjOniRYdBdpG',
    'X-Naver-Client-Secret': 'ZzQs2QTnbO',
}

text = 'Yesterday all my troubles seemed so far away.'

payload = {
    'source': 'en',
    'target': 'ko',
    'text': text,
}

url = 'https://openapi.naver.com/v1/papago/n2mt'

req = Request('POST', url, data=payload, headers=headers)
prepped = req.prepare()     # 미리 컴파일

res = s.send(prepped)

#print(res)
print(res.json()['message']['result']['translatedText'])
print('')



# payload = {
#     'source': 'en',
#     'target': 'ko',
#     'text': res.json()['message']['result']['translatedText'],
# }
#
#
# req = Request('POST', url, data=payload, headers=headers)
# prepped = req.prepare()     # 미리 컴파일
#
# res = s.send(prepped)
#
# print(res.json()['message']['result']['translatedText'])
# print('')

