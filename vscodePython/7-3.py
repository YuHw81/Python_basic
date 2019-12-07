result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))

# =======================class
print('=======================class')
class Cookie():
    pass

a = Cookie()
b = Cookie()

print(a == b)
print(type(a))
print(type(b))
print(id(a))
print(id(b))

print('Cookie는 클래서, a는 객체, a는 Cookie의 인스턴스')

