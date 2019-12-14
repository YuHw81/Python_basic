'''
JSON
JavaScript Object Notation  자바스크립트 객체 표기법
자바스크립트 문법을 활용한 경량 데이터 표현 방식
[ ] : 배열(리스트)
{ } : 객체(딕셔너리)
key : value 쌍(pair)으로 구성
프로그래밍 언어로부터 독립적
'''
import json

f = open('test.json', encoding='utf-8')
text = f.read()
# print(text)

data = json.loads(text) # loads 문자열
# print(type(data))   # <class 'list'>

for d in data:
    # print(type(d))  # <class 'dict'>
    print(d)
    print(d['name'], d['age'], d['gender'])

with open('test.json', encoding='utf-8') as f:
    data = json.load(f) # load 객체
    for d in data:
        print(d['name'], d['age'], d['gender'])


