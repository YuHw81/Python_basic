def add_total(start, end):
    result = 0 
    for i in range(start, end + 1):
        result += i
    return result

t = add_total(1, 100)
print(t)
t = add_total(100, 1000)
print(t)


def china_restaurent(money):
    print('시작')
    print('중국집을 간다')
    if money:
        print('탕수육을 시킨다.')
        print('울면')
    print('자장면을 시킨다.')
    print('군만두를 시킨다.')
    print('끝')

china_restaurent(1000)