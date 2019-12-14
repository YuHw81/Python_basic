import time

print(time.time())  # 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초단위로 

print(time.localtime(time.time()))

print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %X', time.localtime(time.time())))

# for i in range(10):
#     print(i)
#     time.sleep(1)


import random
print(random.randint(1, 2))



import webbrowser
webbrowser.open_new('https://www.naver.com')