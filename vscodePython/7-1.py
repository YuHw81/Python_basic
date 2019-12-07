'''
파일을 쓰기 모드로 열어 출력값 적기
'''
def ex1():
    f = open('test.txt', 'w', encoding='utf-8')
    # f = open('test.txt', 'a', encoding='utf-8')   w:쓰기, a:추가, r:읽기
    for i in range(1, 11):
        data = '%d번째 줄입니다.\n' % i
        f.write(data)
    f.close()

# ex1()

def ex2():
    f = open('test.txt', 'r', encoding='utf-8')
    line = f.readline()
    print(line)
    f.close()

# ex2()

def ex3():
    f = open('test.txt', 'r', encoding='utf-8')
    while True:
        line = f.readline()
        if not line: break
        print(line)
        # print(line, end='')
    f.close()

# ex3()

def ex4():
    f = open('test.txt', 'r', encoding='utf-8')
    lines = f.readlines()   
    # print(type(lines))    # <class 'list'>
    for line in lines:
        print(line)
    f.close()

# ex4()

def ex5():
    f = open('test.txt', 'r', encoding='utf-8')
    data = f.read()
    # print(type(data))     # <class 'str'>
    for c in data:
        # print(c)
        print(c, end='')

# ex5()


