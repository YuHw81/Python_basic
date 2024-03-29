# 데이터베이스
'''
데이터를 수집해야하는 경우
- 소량의 데이터는 CSV, Excel
- 대량의 데이터는 데이터베이스

데이터베이스를 사용하는 이유(목적)
- 대량의 데이터를 처리하기 위해
- 데이터를 공유(사용자, 어플리케이션)
- 동시접속
- 제약조건(중복데이터 제한)
- 데이터의 정합성 확보
- 데이터간의 속성(key) 연결(relation)
- 검색, 정렬 용이
- 보안
- 안정성

데이터베이스의 종류
- Oracle
- MySQL / MariaDB
- MS-SQL
- SQLite

데이터베이스의 구조
- SQL (Structured Query Language) : 구조적인 질의 언어
- 데이터베이스(스키마) > 테이블 > 데이터
- 엑셀 비유 : 파일 > 시트 > 셀
- 행 : 레코드, 로우
- 열 : 필드, 컬럼

엑셀과의 가장 큰 차이점 : 다른 테이블 간의 연동(relation)

root / root1234
port : 3306 -> 3307

host (주소, ip)
DB명 (스키마)
계정명
비밀번호
포트번호

127.0.0.1 = localhost

host : 192.168.0.127
port : 3307
id / pw : study / study1234
db : study

'''


import pymysql

db = pymysql.connect(host='192.168.0.127', port=3307, user='study', password='study1234', db='study')

try:
    cursor = db.cursor()
    sql = 'select * from student'
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        # print(type(data))       
        print(data)     # <class 'tuple'>
finally:
    db.close()        

