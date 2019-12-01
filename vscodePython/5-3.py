import random

def ex1():
    a = random.randrange(1, 11) # 1~10 사이의 랜덤 수
    print(a)


# 두 개의 주사위를 던져서 두 주사위의 눈의 합계가 5가 나올때가지 계속 던지도록
# 출력 (1, 1)
def ex2():
    while True:
        # a = 0
        # b = 0
        a = random.randrange(1, 7)
        b = random.randrange(1, 7)
        if a + b == 5:
            break
    print((a, b))

# ex2()

# 4x + 5y = 60의 모든 해(정수)를 구하시오.
# 4x = 60 - 5y
# x = (60 - 5y) / 4
def ex3():
    # x = 0
    # y = 0
    for i in range(1, 61):
        # print(i)
        y = i
        if (60 - 5 * y) % 4 == 0 and (60 - 5 * y) / 4 >= 0:
            x = (60 - 5 * y) // 4
            print(x, y)
    
# ex3()    


'''
로또번호 변수(리스트)
반복
    1-45의 랜덤값
    변수에 랜덤값이 있는지?
    없으면 리스트에 추가(랜덤값)
    만약 리스트가 길이가 6이되면 중지
'''
def ex4():
    a = []
    print(a.count)
    # while a.count > 6:

# ex4()


'''
숫자 맞히기 게임
컴퓨터가 1~100사이의 랜덤수를 정함
내가 그 숫자를 맞추기(input())
정답이면 '정답입니다. 시도횟수 0회' 출력
오답이면 '큰 숫자를 입력해 주세요.' 또는 '작은 숫자를 입력해 주세요.'
'''
def ex5():
    number = random.randrange(1, 101)
    # print(number)
    print('숫자를 입력해주세요.(1 ~ 100)')
    cnt = 1
    while True:
        answer = int(input())
        if answer == number:
            print('정답입니다. 시도횟수 %d회' % cnt)
            break
        elif answer > number:
            print('작은 숫자를 입력해 주세요.')
        else:
            print('큰 숫자를 입력해 주세요.')
        cnt += 1


ex5()    

