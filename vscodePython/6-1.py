### 함수
'''
return의 용도
1. 그냥 돌아가
2. 값을 가지고 돌아가
'''
def add(a, b):
    c = a + b
    return c

a = add(1, 2)
print(a)

a = add(2, 3)
print(a)

a = add('a', 'b')
print(a)


def test():
    print(1)
    print(2)
    # return 'test'
    return (1, 2)

test()
a = test()
print(a)


def test1():
    print(1)
    print(2)
    # return 'test'
    return (1, 2)

test()    

# 여러 개의 입력값을 받는 함수
print('================여러 개의 입력값을 받는 함수')
def add_many(*args):    # *tuple, **dictionary
    print(type(args))
    print(args)
    result = 0
    for i in args:
        result = result + i
    return result

print(add_many(1,2,3,4,5,6,7,8,9,10))

print('================여러 개의 입력값을 받는 함수2')
def add_mul(choice, *args):
    result = 0
    if choice == 'add':
        result = 0
        for i in args:
            # result = result + i
            result += i
    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
    return result

print(add_mul('add', 1, 2, 3, 4, 5))
print(add_mul('mul', 1, 2, 3, 4, 5))
print(add_mul('xxx', 1, 2, 3, 4, 5))


print('================매개변수에 초깃값 미리 설정하기')
def say_myself(name, old, man=True):
    print('이름은', name)
    print('나이는',old)
    if man:
        print('남자')
    else:
        print('여자')

say_myself('홍길동', 50, True)
say_myself('홍길동', 50)

print('================매개변수에 초깃값 미리 설정하기2')
# def say_myself(name, city='서울', old, man=True):
def say_myself2(name, old, city='서울', man=True):
    print('이름은', name)
    print('나이는',old)
    if man:
        print('남자')
    else:
        print('여자')
    print('도시는', city)

say_myself2('홍길동', 50, '인천', True)
say_myself2('홍길동', 50, True)
say_myself2('홍길동', 50)

print('================')
a = 1
print(id(a))
def vartest(a):
    print(id(a))
    a = a + 1
    print(id(a))
vartest(a)
print(id(a))
print(a)

print('================')
a = [1, 2, 3, 4, 5]
print(id(a))
def vartest2(a):
    print(id(a))
    a[0] = 6
    print(id(a))
vartest2(a)
print(id(a))
print(a[0])

print('================')
def test3():
    for i in range(1, 11):
        result += i
    print(result)

test3()




