### 연습문제
# Q1
a = { '국어': 80, '영어': 75, '수학': 55 }
b = 0
c = 0

for i in a.values():
    print(i)
    b = b + i
    c = c + 1

print(b / c)


# Q2
a = 13 % 2  # 나머지의 몫

print(a)    # 1이면 홀수, 2면 짝수


# Q3
pin = '881120-1068234'

yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)


# Q4
pin = '881120-1068234'

print(pin[7])


# Q5
a = 'a:b:c:d'
b = a.replace(':','#')
print(b)


# Q6
a = [1, 3, 5, 4, 2]
a.sort()
# print(a)
a.reverse()
print(a)


# Q7
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)


# Q8
a = (1, 2, 3)
a = a + (4, )
print(a)


# Q9
a = dict()
a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python'   # 리스트는 딕셔너리 키가 될 수 없다.
a[250] = 'python'
print(a)


# Q10 
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)


# Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
# print(aSet)
b = list(aSet)
print(b)


# Q12
a = b = [1, 2, 3]
a[1] = 4
print(b)

print(id(a))    # 같은 메모리 상에 존재
print(id(b))



