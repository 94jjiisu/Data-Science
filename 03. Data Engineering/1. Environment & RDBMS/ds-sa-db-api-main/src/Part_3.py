"""
Part 3

`DB_API` 이라는 이름의 sqlite 데이터베이스를 과제의 setup.cfg가 있는 위치에 생성합니다.
(앞의 Part 1 또는 Part 2에서 만든 데이터베이스를 이용해도 됩니다.)

1. 데이터베이스에는 `Albums_Part3` 라는 테이블이 생성되어야합니다.
2. Dictionary 와 List 결합된 json_data 안의 10개의 데이터를 입력해야합니다.



"""
import os
import sqlite3

DB_FILENAME = 'DB_API.db'
DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)

json_data = {
"DATA": [
	{
		"AlbumId" : 1,
		"Title" : "For Those About To Rock We Salute You",
		"ArtistId" : 1
	},
	{
		"AlbumId" : 2,
		"Title" : "Balls to the Wall",
		"ArtistId" : 2
	},
	{
		"AlbumId" : 3,
		"Title" : "Restless and Wild",
		"ArtistId" : 2
	},
	{
		"AlbumId" : 4,
		"Title" : "Let There Be Rock",
		"ArtistId" : 1
	},
	{
		"AlbumId" : 5,
		"Title" : "Big Ones",
		"ArtistId" : 3
	},
	{
		"AlbumId" : 6,
		"Title" : "Jagged Little Pill",
		"ArtistId" : 4
	},
	{
		"AlbumId" : 7,
		"Title" : "Facelift",
		"ArtistId" : 5
	},
	{
		"AlbumId" : 8,
		"Title" : "Warner 25 Anos",
		"ArtistId" : 6
	},
	{
		"AlbumId" : 9,
		"Title" : "Plays Metallica By Four Cellos",
		"ArtistId" : 7
	},
	{
		"AlbumId" : 10,
		"Title" : "Audioslave",
		"ArtistId" : 8
	}
]}

# 테이블 실험할 때는 DROP TABLE 구문도 많이 사용됩니다. 참고하세요!
# cursor.execute("DROP TABLE IF EXISTS Albums_Part3;")

"""
해당 과제는 `pytest -m pytest` 로만 진행하기 어렵습니다.
`python src/Part_3.py` 처럼 코드를 실행해서 데이터베이스의 변화를 확인해보시기 바랍니다.

아래 pass 를 지운 후 여러분의 코드를 작성해주시기 바랍니다.
테스트는 tests/Part_3/test_Part_3.py 에서 진행됩니다.

# 이번에 사용할 데이터는 많이 사용되는 json 형태의 데이터와도 유사합니다.

Part 3 은 딕셔너리와 리스트가 결합된 입력을 예시로 합니다. 테스트는 아래의 상황을 확인합니다.
1. `setup.cfg`와 같은 위치에 'DB_API.db' 파일이 생성되었는지 확인합니다.   
2. 여러분의 테이블이 스키마대로 만들어졌는지 확인합니다.
3. 데이터가 10개 들어가 있는지 확인합니다.
4. 데이터베이스의 데이터와 resource/DB_API 데이터와 비교합니다.

"""


conn = sqlite3.connect(DB_FILENAME)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Albums_Part3;")
cur.execute("""CREATE TABLE IF NOT EXISTS Albums_Part3 (
				AlbumId INTEGER NOT NULL PRIMARY KEY,
				Title NVARCHAR(160),
				ArtistId INTEGER);
			""")

for data in json_data['DATA']:
	cur.execute("INSERT INTO Albums_Part3 (AlbumId, Title, ArtistId) VALUES (?, ?, ?);", 
	(data['AlbumId'], data['Title'], data['ArtistId']))

conn.commit()
cur.close()
conn.close()