# 네이버 API
import os
import sys
import urllib.request
import json

client_id = "szfQ0Y2iwgVceFTniZf9"
client_secret = "7nGbtHmA08"
encText = urllib.parse.quote("겨울왕국")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
url = "https://openapi.naver.com/v1/search/movie?query=" + encText
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))
    text = response_body.decode('utf-8')
    data = json.loads(text)
    items = data['items']   # list
    for item in items:
        print(item['title'], item['link'])
else:
    print("Error Code:" + rescode)