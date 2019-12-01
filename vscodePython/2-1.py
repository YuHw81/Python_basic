
print('===================')
c = 'I eat {0} apples'.format(3)
print(c)

print('===================')
c = 'I eat {0} apples. So I was sick for {1} days.'
print(c.format(3, 'three'))

print('===================')
# 문자열 포맷팅
c = 'I eat {number} apples. So I was sick for {day} days.'.format(number=3, day='three')
print(c)

print('===================')
# f문자열 포매팅 python v3.6
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age+1}입니다.')

d = {'name':'홍길동', 'age':30} #딕셔너리
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')


print(f'{"python":!^12}')

a = "{0:!^12}".format('python')
print(a)