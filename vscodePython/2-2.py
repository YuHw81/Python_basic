# 문자열 관련 함수
## 문자열 중 문자 개수 count
print('================문자열 중 문자 개수 count')

a = "hobby"
p = a.count('b')
print(p)

b = 'bye'
p = b.count('b')
print(p)

a = "hobby"
b = a.count('b') ** 2 / 5
print(b)

## 문자열 중 문자 위치1 find
print('================문자열 중 문자 위치1 find')

a = 'Python is the best choice'
#####0         1         2
#####0123456789012345678901234
b = a.find('b')
print(b)
b = a.find('k') # 없으면 -1 출력
print(b)

b = a.find('i') # 먼저나오는 i 를 출력
print(b)

a = 'hi, hello'
# a = 'hi, xxx'
print(a.find('xxx')) # 해당 문자열이 포함되어 있드마녀 무조건 0 이상
if (a.find('xxx') >= 0):
    print('욕이 포함되어 있습니다.')
else:   # if (a.find('xxx') = -1
    print('욕이 없습니다.')


## 문자열 중 문자 위치2 index
print('================문자열 중 문자 위치2 index')
a = 'Life is too short'
p = a.index('t')
print(p)

### p = a.index('k') # 없으면 error

a_index = -1 # 변수 미리 선언(생성)
if (a.count('k') > 0):
    a_index = a.index('k')
print(a_index)    


## 문자열을 삽입 join : 앞의 문자열을 뒤에 문자열 사이사이에 삽입 => 문자열보다는 리스트와 튜플에서 사용
print('================문자열을 삽입 join : 앞의 문자열을 뒤에 문자열 사이사이에 삽입')
a = ','.join('abcd')
print(a)


## 문자열바꾸기 replace
print('================문자열바꾸기 replace')
a = 'Life is too short.'
p = a.replace('Life', 'Your leg')
print(p)

a = '           Li        fe is to   o s     hort.         '
p = a.strip()
print(p)
p = a.replace(' ', '')
print(p)


## 문자열 쪼개기 split 
print('================문자열 쪼개기 split')
a = 'Life is too short.'
p = a.split() # 공백기준 # 결과값은 list
print(p)

# dictionary { key1 : value1, key2 : value2, key3 : value3, ... }
# list [ value1, value2, value3, ... ]

print(p[0])