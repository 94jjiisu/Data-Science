"""
Part 4
클라우드 데이터베이스에 'passenger' 라는 테이블을 생성하고 titanic.csv 에 있는 데이터를 'passenger' 테이블로 옮깁니다.

1. passenger 테이블의 필드를 알맞게 추가합니다 (필드명은 자유입니다).
아래에는 각 필드에 해당하는 데이터 타입입니다.
- Survived: INT
- Pclass: INT
- Name: VARCHAR(128)
- Sex: VARCHAR(12)
- Age: FLOAT
- Siblings/Spouses Aboard: INT
- Parents/Children Aboard: INT
- Fare: FLOAT

2. psycopg2.connect 를 이용해 connection 변수가 데이터베이스와 연결할 수 있도록 다음 변수들에 알맞은 정보를 담습니다:
- host: 데이터베이스 호스트 주소를 입력합니다.
- user: 데이터베이스 유저 정보를 입력합니다.
- password: 데이터베이스 비밀번호를 입력합니다.
- database: 데이터베이스 이름을 입력합니다.

3. passenger 테이블에 titanic.csv 에 있는 데이터를 옮깁니다.

"""

import csv
import psycopg2

host = 'drona.db.elephantsql.com'
user = 'ergrgcvn'
password = 'y5DUZFSXpR5NvRyQbcPBpcxm6WqBkNL-'
database = 'ergrgcvn'

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)


# 나머지 코드는 titanic.csv 의 데이터를 passenger 테이블로 전달할 수 있도록 자유롭게 작성해주시기 바랍니다.


cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS passenger;")
cursor.execute("""CREATE TABLE IF NOT EXISTS passenger (
                    "Id" INT,
                    "Survived" INT, 
                    "Pclass" INT, 
                    "Name" VARCHAR(128), 
                    "Sex" VARCHAR(12), 
                    "Age" FLOAT, 
                    "Siblings/Spouses Aboard" INT, 
                    "Parents/Children Aboard" INT, 
                    "Fare" FLOAT);
			""")

with open('titanic.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader) # 헤더스킵

    for i, j in enumerate(reader):
        cursor.execute('INSERT INTO passenger VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);',
                        (i, j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7]))

connection.commit()


cursor.execute("SELECT * FROM passenger")
result = cursor.fetchall()

cursor.close()
connection.close()