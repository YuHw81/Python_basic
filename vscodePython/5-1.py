
### for 예제1
def for_ex1():
    test_list = ['one', 'two', 'three']

    for i in test_list:
        print(i)


### for 예제2
def for_ex2():
    a = [(1, 2), (3, 4), (5, 6)]
    for (first, second) in a:
        print(first + second)

    
# for_ex1()
# for_ex2()

### for 응용1
def for_ex3():
    marks = [90, 25, 67, 45, 80]
    number = 0
    sumScore = 0
    for mark in marks:
        sumScore = sumScore + mark
        number = number + 1
        if mark >= 60:
            print('%d번 학생 %d점 합격입니다.' % (number, mark))
        else:
            print('%d번 학생 %d점 불합격입니다.' % (number, mark))

    print(sumScore)

#for_ex3()            
            
### for 응용2
# a = range(10)
# print(a)
def for_ex4():
    add = 0
    for i in range(1, 11):
        print('i=' + str(i))
        add = add + i # add += i
    print(add)

# for_ex4()

def for_ex5():
    marks = [90, 25, 60, 45, 80]
    names = ['홍길동', '김길동', '고길동', '최길동', '이길동']

    for i in range(0, len(marks)):
        if marks[i] >= 60:
            print('%s은 %d점으로 합격입니다.' % (names[i], marks[i]))

# for_ex5()

def for_ex6():
    a = range(1, 101)
    result = 0
    for i in a:
        result = result + i # result += i
    print(result)

# for_ex6()

def for_ex7():
    for i in range(2, 10):
        for j in range(1, 10):
            # print(i * j, end = ' ')
            # print(str(i) + ' * ' + str(j) + ' = ' + str(i * j))
            print('%d * %d = %d' % (i, j, i * j))
        print('')

# for_ex7()

### 리스트 내포 사용
def for_ex8():
    a = [1, 2, 3, 4]
    result = []
    for num in a:
        result.append(num*3)
    print(result)

# for_ex8()    

def for_ex9():
    a = [1, 2, 3, 4]
    # result = [num*3 for num in a]
    result = [num*3 for num in a if num % 2 == 0]
    # for num in a:
    #     if num % 2 == 0:
    #         result.append(num*3)
    print(result)

# for_ex9()    

def for_ex10():
    result = [x*y for x in range(2, 10)
                for y in range(1, 10)]
    print(result)

# for_ex10()    
