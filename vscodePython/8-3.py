
def ex1():
    try:
        print('1')
        4/0
        print('2')
    except ZeroDivisionError as e:
        print('예외발생')
        print(e)
    finally:
        print('여기는 finally')     # 예외가 발생하든 안 하든 무조건 실행

# ex1()

# 오류 회피하기
def ex2():
    try:
        f = open('asdfasdf.txt', 'r')
    except FileNotFoundError:
        pass

    print(1)

# ex2()

def ex2_1():
    for i in range(1, 11):
        try:
            print(i)
            f = open('aa.txt', 'r')
        except:
            # pass
            print('error')

# ex2_1()

# 오류 일부러 발생시키기
'''
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass
    # def fly(self):
    #     print('fly 재정의')

eagle = Eagle()
eagle.fly()
'''

