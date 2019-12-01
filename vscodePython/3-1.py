# 튜플(tuple) 자료형
print('================튜플(tuple) 자료형')

t1 = ()
t2 = (1,)
print(type(t2)) # <class 'tuple'>

t = (1)         # 튜플이 아닌 보통 연산의 ()로 인식
print(type(t))  # <class 'int'>

t4 = 1, 2, 3
print(type(t4)) # <class 'tuple'> : () 없이도 ,로 tuple로 인식

t5 = 1,
print(type(t5)) # <class 'tuple'>

# 나혼자 코딩
print('================나혼자 코딩')
a = (1, 2, 3)
b = (4, )
print(a + b)

# 딕셔너리(dictionary) 자료형
print('================딕셔너리(dictionary) 자료형')

a = {1: 'a'}
a['name'] = 'b'     # a[key] = value    {1: 'a', 'name': 'b'}
print(a)
a['name'] = 'c'     # key는 유일하다    {1: 'a', 'name': 'c'}
print(a)

del a['name']       # dictionary 삭제   {1: 'a', 'name': 'c'}
print(a)

# 딕셔너리(dictionary), 리스트의 사용방법의 차이
print('================딕셔너리(dictionary), 리스트의 사용방법의 차이')

a = { '김연아': '피겨스케이팅', '류현진': '야구', '박지성': '축구', '귀도': '파이썬'}

print(a['김연아'])
print(a['류현진'])

b = ['김연아', '류현진', '박지성', '귀도']
c = ['피겨스케이팅', '야구', '축구', '파이썬']
print(b[0], c[0])
print(b[1], c[1])

a['홍길동'] = '사람'
print(a)

a = {(1,2):'hi'}    # 리스트(list)는 key로 사용불가, 튜플(tuple)은 key로 사용가능
print(a[(1,2)])


# 딕셔너리(dictionary) 관련 함수
print('================딕셔너리(dictionary) 관련 함수')

# a['name']에러
print(a.get('name', '홍길동')) # value가 없으면 두번째 매개변수 리턴



ex = { 'name': '홍길동', 'birth': 1128, 'age': 30}
print(ex)

'''
age1 = 20
age2 = 21
age3 = 22
avg = (age1+age2+age3...age15) / 15
age = [20,21,22....]

kor = [100, 90, ....]
def avgKorScore(kor):
    for
    sum

'''

