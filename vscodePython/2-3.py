# 리스트

ex = [1, 2, ['Life', 'is']]
# print(len(ex)) >> result : 3
print(ex[2])    # ex의 세번째 요소 ['Life', 'is']
print(ex[2][0]) # ex의 세번째 요소 ['Life', 'is'] 중 첫번째 요소 'Life'

ex = [1, 2, ['Life', ['too', 'short']]]
'''
ex = [
        1, 
        2, 
        [
            'Life', 
            [
                'too', 
                'short'
            ]
        ]
    ]
'''
print(ex[2][1][1]) # ex의 세번째 요소 ['Life', ['too', 'short']] 중 두번째 요소 중 ['too', 'short'] 중 두번째 요소 'short'


# 리스트 연산하기
print('================리스트 연산하기')
a = [1, 2, 3]
b = [4, 5, 6]
p = a + b
print(p) # [1, 2, 3, 4, 5, 6]
p = a * 3
print(p) # [1, 2, 3, 1, 2, 3, 1, 2, 3]


# 연산 오류
print('================연산 오류')
# a = 3 + 'hi' # TypeError: unsupported operand type(s) for +: 'int' and 'str'
a = str(3) + 'hi'
print(a)
print(type(int('4')))

print('====================')
a = '1'
print(type(list(a)))

def sum(a, b):
    return print(a + b)

sum(2, 3)


# 리스트 수정 삭제 추가
print('================리스트 수정 삭제 추가')

a = [1, 2, 3]
a[2] = 4    # 리스트 세번째 인덱스 수정
print(a)
del a[1]    # 리스트 두번째 인덱스 삭제 # del : 객체 삭제(객체:모든 자료형)
print(a)

a = [1, 2, 3]
a.append(4) # 리스트 요소 추가
a.append([5, 6]) # 리스트 요소 추가
print(a)    # [1, 2, 3, 4, [5, 6]]
print(a[4]) # [5, 6]
print(a[4][1])  # 6

b = a[4]    # [5, 6]
print(b[1]) # 6


# 리스트 정렬
print('================리스트 정렬')

a = [1, 4, 3, 2]
a.sort()    # 리스트 정렬
print(a)

a = ['a', 'c', 'b']
a.reverse() # 리스트 뒤집기
print(a)

a = [1, 2, 3]
print(type(a))
# a.index[4]  # TypeError: '
a.insert(0, 4)  # list 0 위치에 4 입력
print(a)

a = [1, 2, 3, 1, 2, 3]
a.remove(3) # list 중 첫번째 3을 삭제
print(a)
a.remove(3) # 두번 실행하여 3을 삭제
print(a)

a.clear()   # 리스트 전체 삭제
print(a)


# 리스트 pop
print('================리스트 pop')
a = [1, 2, 3, 4]
b = a.pop()     # 빈값은 리스트의 마지막. str.pop(index) 
print(b)
print(a)

a = [1, 2, 3, 4]
b = a.pop(1)    # 1 = index
print(b)
print(a)


def x():
    y()
    print('x')

def y():
    z()
    print('y')    

def z():
    print('z')

x()

