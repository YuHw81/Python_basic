# q1
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

# print(is_odd(1))
# print(is_odd(2))
# print(is_odd(101))
# print(is_odd(100))


# q2
def avg_nubmers(*args):
    result = 0
    for i in args:
        result += i
        # print(result)
        # print(len(args))
    return print(result / len(args))

# avg_nubmers(1, 2)
# avg_nubmers(1, 2, 3, 4, 5)


def q3():
    input1 = input('첫번째 숫자를 입력하세요:')
    input2 = input('두번째 숫자를 입력하세요:')

    # total = input1 + input2
    total = int(input1) + int(input2)
    print('두 수의 합은 %s 입니다.' % total)

# q3()


def q4():
    print('you' 'need' 'python')    # youneedpython
    print('you'+'need'+'python')    # youneedpython
    print('you','need','python')    # you need python
    print(''.join(['you','need','python'])) # youneedpython

# q4()    

def q5():
    f1 = open('q5.txt', 'w')
    f1.write('Life is too short')
    f1.close()

    f2 = open('q5.txt', 'r')
    print(f2.read())
    f2.close()

# q5()    


def q6():
    user_input = input('저장할 내용을 입력하세요:')
    f = open('q6.txt', 'a')
    f.write(user_input)
    f.write('\n')
    f.close()

# q6()


def q7():
    f = open('q7.txt', 'r')
    body = f.read()
    f.close()

    body = body.replace('java', 'python')

    f = open('q7.txt', 'w')
    f.write(body)
    f.close()

# q7()    





