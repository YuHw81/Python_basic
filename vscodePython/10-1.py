import pymysql

# DB 연결
conn = pymysql.connect(host='192.168.0.127', port=3307, db='study', user='study', password='study1234', charset='utf8')

# 커서 생성 (sql문을 실행하기 위해)
cur = conn.cursor()

sql = 'select * from student'
cur.execute(sql)

# 실행결과를 가져오기
rows = cur.fetchall()
# print(type(rows))
# print(rows)
for row in rows:
    print(row[0], row[1])

cur.close()
conn.close()

import pandas as pd

df = pd.DataFrame(rows)
print(df)