class FourCal:
    def __init__(self, a, b):
        self.first = a
        self.second = b
        # print('여기는 생성자!')
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result                

'''
a = FourCal()
# print(type(a))
a.setdata(4, 2)
# print(a.first)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())


b = FourCal()
b.setdata(3, 8)
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())

# print(a.first)
# print(b.first)


c = FourCal(10, 5)
print(c.add())

FourCal(10, 5)  # 생성자 메서드 실행

'''

# 상속
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result


# a = MoreFourCal(4, 2)
# print(a.add())
# print(a.pow())

# c = FourCal(10, 5)
# print(c.pow())    # AttributeError: 'FourCal' object has no attribute 'pow'

# a = FourCal(4, 0)
# a.div() # ZeroDivisionError: division by zero


class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

# a = SafeFourCal(4, 0)
# print(a.div())


class FailFourCal(FourCal):
    def mul(self):
        if self.first == 0 or self.second == 0:
            return 'Fail'
        else:
            return self.first * self.second

# a = FailFourCal(0, 4)
# print(a.mul())


# 사람 객체
# 속성 : 이름, 나이 (필드field, 프로퍼티property)
# 기능 : 걷다, 뛰다, 자다 (메서드method)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walk(self, target):
        print('%s(으)로 걷다' % target)
    def run(self, speed):
        print('%s 속도로 뛰다' % speed)
    def sleep(self):
        print('잠을 자다')

kim = Person('김민지', 20)
lee = Person('이수진', 20)
print(kim.name)
print(lee.name)

kim.walk('학원')

class Student(Person):  # Inheritance 상속
    def study(self):
        print('%s가 공부합니다.' % self.name)
    def walk(self, target):     # Overriding 덮어쓰기
        print('%s가 %s(으)로 걸어갑니다.' % (self.name, target))

kim = Student('김민지', 20)
kim.study()         # 자식클래스에서 확장(추가)한 메서드
kim.walk('학원')    # Overriding 재정의
kim.run('400km/h')  # 부모클래스(상속)의 메서드
kim.sleep()


