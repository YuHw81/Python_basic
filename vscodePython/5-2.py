def q1():
    a = "Life is too short, you need python"

    if "wife" in a: print("wife")
    elif "python" in a and "you" not in a: print("python")
    elif "shirt" not in a: print("shirt")
    elif "need" in a: print("need")
    else: print("none")

# q1()  # shirt    

def q2():
    result = 0
    i = 1
    while i <= 1000:
        # print(i)
        if i % 3 == 0:
            result += i
        i += 1
    print(result)

# q2()    # 166833

def q3():
    i = 0
    while True:
        i += 1
        if i > 5 : break
        print('*' * i)

# q3()        

def q3_1():
    # a = [1, 2, 3, 4, 5]
    for i in range(1, 6):
        print('*' * i)

# q3_1()        

def q4():
    for i in range(1, 101):
        print(i)

# q4()

def q5():
    A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
    total = 0
    for score in A:
        total += score
    average = total / len(A)
    print(average)

# q5()

def q6():
    numbers = [1, 2, 3, 4, 5]

    result = []
    for n in numbers:
        if n % 2 == 1:
            result.append(n*2)

    print(result)

def q6_1():
    numbers = [1, 2, 3, 4, 5]
    result = [n*2 for n in numbers if n % 2 == 1]

    print(result)

# 1부터 100까지의 홀수의 합 출력
def q7():
    result = 0
    for i in range(1, 101):
        # if i % 2 != 0:
        if i % 2 == 1:
            # print(i)
            result += i
    print(result)
    
# q7()

# 가장 큰 수 찾아 출력
def q8():
    a = [5, 10, 1, 20, 15, 3]
    result = 0
    for i in a:
        if result < i:
            result = i
    print(result)

# q8()

'''
*****
****
***
**
*
'''
def q9():
    # for i in range(1, 6):
    #     print('*' * (6 - i))
    for i in range(5, 0, -1):
        print('*' * i)

# q9()

def q9_1():
    for i in range(3, 101, 3):
        print(i)

'''
    *
   ***
  *****
 *******
*********
'''
def q10():
    for i in range(1, 10, 2):
        print('{:^9}'.format('*' * i))
       
# q10()

def q10_1():
    line = 5
    for i in range(1, line + 1):
        # print(i, line - i, i * 2 - 1)
        print(' ' * (line - i) + '*' * (i * 2 - 1))

# q10_1()

# 주어진 수의 각 자리수의 합계를 구해서 출력
# 예) 12345 -> 15 (1+2+3+4+5)
def q11():
    a = 123456789
    b = ' '.join(str(a)).split()
    result = 0
    for i in b:
        # print(i)
        result += int(i)

    print(result)

# q11()    


# 볼펜 456개, 학생 30명
# 똑같은 갯수로 나눠서 가지려고할 때 학생 한명이 갖게될 볼펜 수와 남은 볼펜 수를 출력
# 학생이 갖는 볼펜 : ?개, 남은 볼펜 ?개
def q12():
    ballpen = 456
    student = 30
    # print(ballpen//student)
    # print(ballpen%student)
    print('학생이 갖는 볼펜 : %d개, 남은 볼펜 %d개' % ( ballpen//student, ballpen%student ))

# q12()


# 금액의 최소 지폐의 수량을 출력 (천단위 미만은 제외)
# 5만원권 0장, 1만원권 0장, 5천원권 0장, 1천원권 0장
# 76,000원 -> 5만원권 1장, 1만원권 2장, 5천원권 1장, 1천원권 1장
def q13():
    money = 76000
    m50000 = money // 50000
    money = money % 50000
    m10000 = money // 10000
    money = money % 10000
    m5000 = money // 5000
    money = money % 5000
    m1000 = money // 1000
    money = money % 1000
    print('5만원권 %d장, 1만원권 %d장, 5천원권 %d장, 1천원권 %d장' % (m50000, m10000, m5000, m1000))

# q13()    

