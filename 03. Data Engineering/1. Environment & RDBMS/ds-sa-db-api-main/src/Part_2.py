"""
Part 2

`DB_API` 이라는 이름의 sqlite 데이터베이스를 과제의 setup.cfg가 있는 위치에 생성합니다.
(앞의 Part 1에서 만든 데이터베이스를 이용해도 됩니다.)

1. 데이터베이스에는 `Albums_Part2` 라는 테이블이 생성되어야합니다.
2. Dictionary 와 List가 결합된 dictionary_data 안의 10개의 데이터를 입력해야합니다. 첫번째 줄은 컬럼명입니다.

"""
import os
import sqlite3

DB_FILENAME = 'DB_API.db'
DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)

dictionary_data = {
		"Columns":["AlbumId", "Title", "ArtistId"],
		"1" : ["For Those About To Rock We Salute You",1],
    	"2" : ["Balls to the Wall",2],
    	"3" : ["Restless and Wild",2],
    	"4" : ["Let There Be Rock",1],
    	"5" : ["Big Ones",3],
    	"6" : ["Jagged Little Pill",4],
    	"7" : ["Facelift",5],
    	"8" : ["Warner 25 Anos",6],
    	"9" : ["Plays Metallica By Four Cellos",7],
    	"10" : ["Audioslave",8]
		}

# 테이블 실험할 때는 DROP TABLE 구문도 많이 사용됩니다. 참고하세요!
# cursor.execute("DROP TABLE IF EXISTS Albums;")

"""
해당 과제는 `pytest -m pytest` 로만 진행하기 어렵습니다.
`python src/Part_2.py` 처럼 코드를 실행해서 데이터베이스의 변화를 확인해보시기 바랍니다.

아래 pass 를 지운 후 여러분의 코드를 작성해주시기 바랍니다.
테스트는 tests/Part_2/test_Part_2.py 에서 진행됩니다.

# 이번에 사용할 데이터는 많이 사용되는 json 형태의 데이터와도 유사합니다.

Part 2 은 딕셔너리와 리스트가 결합된 입력을 예시로 합니다. 테스트는 아래의 상황을 확인합니다.
1. `setup.cfg`와 같은 위치에 'DB_API.db' 파일이 생성되었는지 확인합니다.   
2. 여러분의 테이블이 스키마대로 만들어졌는지 확인합니다.
3. 데이터가 10개 들어가 있는지 확인합니다.
4. 데이터베이스의 데이터와 resource/DB_API 데이터와 비교합니다.

"""

conn = sqlite3.connect(DB_FILENAME)

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Albums_Part2;")
cur.execute("""CREATE TABLE IF NOT EXISTS Albums_Part2 (
				AlbumId INTEGER NOT NULL PRIMARY KEY,
				Title NVARCHAR(160),
				ArtistId INTEGER);
			""")

for i in dictionary_data.items():
	if i[0] != 'Columns':
		cur.execute("INSERT INTO Albums_Part2 (AlbumId, Title, ArtistId) VALUES (?, ?, ?);", (i[0], i[1][0], i[1][1]))

conn.commit()
