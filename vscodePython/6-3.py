f = open('test.txt', 'w')   # r:read, w:write, a:add
f.close()


'''
절대경로 : 절대적인 경로
 - 최상위 경로부터 시작
 - 윈도우 : C:\python\...
 - 리눅스(유닉스, 맥) : /python/...
상대경로 : 상대적인 경로
 - 내가 있는 경로부터 시작
 - 드라이브명 또는 /로 시작하지 않음. /가 없음.
 - 파일명 앞에 아무것도 없으면 현재경로
'''

f = open('../test2.txt', 'w')   # 현재 경로의 한 폴더 위(현재경로 D:\vscodePython -> 한 폴더 위 D:\)
f.close()

f = open('D:/vscodePython/test2.txt', 'w')   # 절대 경로
f.close()


