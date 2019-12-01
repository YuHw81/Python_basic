# 집합 자료형
print('================집합 자료형')

s2 = set('Hello')   # 순서, 중복 없다
print(s2)

print(list(s2))
print(tuple(s2))


s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print('================교집합')
print(s1 & s2)
print(s1.intersection(s2))

print('================합집합')
print(s1 | s2)
print(s1.union(s2))

print('================차집합')
print(s1 - s2)
print(s2 - s1)
print(s1.difference(s2))
print(s2.difference(s1))

a = True
# b = false     # name 'false' is not defined
b = False

print(a)
print(b)
print(type(a))  # <class 'bool'>

# 특정 자료형으로 True / False => 값이 있다 / 없다
print(id(a))
print(id(b))

# 기본자료형 / 참조자료형(사용자 정의 자료형) 차이
a = [1,2,3]
b = a[:]
print(a)
print(id(a))
print(id(b))

a, b = ('python', 'life')
print(a, b)
a, b = 'python', 'life'
print(a, b)

a = 3
b = 5
a, b = b, a
# tmp = a
# a = b
# b = tmp
print(a, b)

