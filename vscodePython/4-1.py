money = True

if money:
    if True:
        print('버스를 타고 가라')
    print('택시를 타고 가라')
else:
    print('걸어가라')


print('시작')
print('중국집을 간다')
money = True
if money:
    print('탕수육을 시킨다.')
    print('울면')
print('짜장면을 시킨다')
print('군만두를 시킨다')
print('끝')


t = 10
m = 11
# 출석체크
if t >= 10 and m >= 11 :
    print('지각')


pocket = ['paper', 'cellphone', 'money']
if 'card' in pocket:
    print('걸어가라')
else:
    print('버스 타고 가라')


pocket = ['paper', 'cellphone']
card = False
if 'money' in pocket:
    print('택시 타고 가라')
else:
    if card:
        print('택시를 타고 가라')
    else:
        print('걸어 가라')



pocket = ['money']
card = True
if 'money' in pocket:
    if card:
        print('모범택시 타라')
    else:
        print('택시 타라')


card = False
if 'money' in pocket and card:
    print('모범택시 타라')
elif 'money' in pocket:
    print('택시 타라')
else:
    print('걸어가라')
print('집에 왔다')



score = 59
if score >= 60:
    message = 'success'
else:
    message = 'fail'
print(message)



message = 'success' if score >= 59 else 'fail'
print(message)


treeHit = 1 # 나무 찍은 횟수
maxHit = 10
while True: # 횟수가 10미만인 동안 반복
    print('나무를 %d번 찍었습니다' % treeHit)
    if treeHit == maxHit : # 10번 찍으면
        print('나무 넘어갑니다')
        break
    treeHit = treeHit + 1 # 횟수 1 증가 treeHit += 1

print('나무 베기 끝')
print('저는 나무를 ' + str(treeHit) + '번 찍었습니다')



a = 0
num = 1
while num <= 10:
    a += num
    num += 1
print(a)



prompt = """
1. Add
2. Del
3. List
4. Quit
Enter number:"""
number = 0
while number != 4:
    print(prompt)
    # number = int(input())
    break



coffe = 10
money = 300
while money:
    print('커피를 줍니다')
    coffe = coffe - 1 
    print('남은 커피의 양은 %d개입니다' % coffe)
    if coffe == 0:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다.')
        break



