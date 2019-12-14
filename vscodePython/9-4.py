# 외부 JSON
import json
import urllib.request

url = 'http://withsky.co.kr/json/test.json'
req = urllib.request.Request(url)
res = urllib.request.urlopen(req)

text = res.read()
# print(text.decode('utf-8'))

data = json.loads(text)

for d in data:
    print(d['title'], d['name'], d['date'], d['readno'])