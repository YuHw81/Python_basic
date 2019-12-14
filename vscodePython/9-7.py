# 엑셀
import pandas as pd
# a_list = [
#     ['홍길동', 90, 100, 80],
#     ['고길동', 80, 90, 70],
#     ['김길동', 70, 80, 60]
# ]

# df = pd.DataFrame(a_list, columns=['이름', '국어', '영어', '수학'])
# df.to_excel('score.xlsx', encoding='ms949')

# 엑셀 읽어오기
df2 = pd.read_excel('score.xlsx', encoding='ms949', index_col = 0)

print(df2)