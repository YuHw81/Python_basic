# CSV (, 기준으로 구분)
# 파이썬에서 CSV를 다룰 때 (pandas)
import pandas as pd
# 리스트 생성 (학생들의 국어, 영어, 수학점수)
# a_list = [
#     ['홍길동', 90, 100, 80],
#     ['고길동', 80, 90, 70],
#     ['김길동', 70, 80, 60]
# ]
# print(a_list[0][0]) # 홍길동
# df = pd.DataFrame(a_list, columns=['이름', '국어', '영어', '수학'])
# print(df)

# csv 저장
# df.to_csv('score.csv', encoding='ms949')    # 엑셀프로그램에서 한글 인식

# csv 읽어오기
df2 = pd.read_csv('score.csv', encoding='ms949', index_col=0)

print(df2)
print(df2['국어'])  # 열
print(df2.iloc[3:]) # 인덱스로 행을 가져오는 방법

# 평균열 추가
# 없는 열을 지정하면 추가
df2['평균'] = 0
print(df2.iloc[:, 1:4].sum(axis=1))
# print(df2)

df2['평균'] = df2.iloc[:, 1:4].mean(axis=1)
print(df2)
