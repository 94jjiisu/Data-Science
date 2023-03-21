
import pickle

from src import Part_2
from src.Part_2 import sqlite3

from tests.conftest import os

DB_FILEPATH = Part_2.DB_FILEPATH

# Part 2 은 리스트, 딕션어리 입력을 예시로 합니다.
# 1. `setup.cfg`와 같은 위치에 'DB_API.db' 파일이 생성되었는지 확인합니다.   
table_exist = os.path.isfile(DB_FILEPATH)
def test_Part_2_exist():
    assert table_exist

conn = None
if table_exist == True:
    conn = sqlite3.connect(DB_FILEPATH)

#2. 여러분의 테이블이 스키마대로 만들어졌는지 확인합니다.
def test_Part_2_schema():
    fields = {
        ('AlbumId','INTEGER', 1, 1),
        ('Title','NVARCHAR(160)', 0, 0),
        ('ArtistId','INTEGER', 0, 0)
    }

    cursor = conn.cursor()
    cursor.execute("SELECT p.name, p.type, p.'notnull', p.pk FROM pragma_table_info('Albums_Part2') p;")
    columns = set(cursor.fetchall())

    assert fields == columns 

#3. 데이터가 10개 들어가 있는지 확인합니다.

def test_Part_2_count():

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Albums_Part2;")
    count = cursor.fetchone()
    assert count[0] == 10

#4. 데이터베이스의 데이터와 resource/DB_API 데이터와 비교합니다.

def test_Part_2_data():

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Albums_Part2;")
    user_data = cursor.fetchall()

    Part_2_resource = None

    with open('resource/DB_API.pickle', 'rb') as file:
        Part_2_resource = pickle.load(file)

    assert user_data == Part_2_resource
