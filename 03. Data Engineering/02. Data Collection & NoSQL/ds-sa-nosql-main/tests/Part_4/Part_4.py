import os
from src.Part_4 import  (sqlite3,
                        dont_touch,
                        DB_FILEPATH)

def test_mongodb_table_collection_id(collection):
    """
    몽고디비 콜렉션에 Github issue 리스트의 내용이 들어있는지 확인합니다.
    -  몽고디비 문서에 들어있는 Github issue 리스트 값 확인
    """
    for item in dont_touch:
        assert collection.count_documents({"id":item['id']}) >= 1
        assert collection.count_documents({"node_id":item['node_id']}) >= 1
        assert collection.count_documents({"body":item['body']}) >= 1


conn = None
table_exist = os.path.isfile(DB_FILEPATH)
if table_exist == True:
    conn = sqlite3.connect(DB_FILEPATH)

def test_sqlite_exist():
    """
    SQLite 데이터베이스가 존재하는지 확인합니다.
    """
    assert table_exist

def test_sqlite_user_table_schema():
    """
    User 테이블의 스키마가 정확한지 확인합니다.
    """
    fields = {
        ('id','INTEGER', 1, 1),
        ('login','VARCHAR(10)', 0, 0),
        ('node_id','VARCHAR(20)', 0, 0)
    }
    cursor = conn.cursor()
    cursor.execute("SELECT p.name, p.type, p.'notnull', p.pk FROM pragma_table_info('User') p;")
    columns = set(cursor.fetchall())

    assert fields == columns

def test_sqlite_label_table_schema():
    """
    Label 테이블의 스키마가 정확한지 확인합니다.
    """
    fields = {
        ('id','INTEGER', 1, 1),
        ('name','VARCHAR(20)', 0, 0),
        ('node_id','VARCHAR(20)', 0, 0),
        ('color','VARCHAR(10)', 0, 0)
    }
    cursor = conn.cursor()
    cursor.execute("SELECT p.name, p.type, p.'notnull', p.pk FROM pragma_table_info('Label') p;")
    columns = set(cursor.fetchall())

    assert fields == columns

def test_sqlite_prlist_table_schema():
    """
    PRlist 테이블의 스키마가 정확한지 확인합니다.
    """
    fields = {
        ('id','INTEGER', 1, 1),
        ('node_id','VARCHAR(20)', 0, 0),
        ('title','VARCHAR(100)', 0, 0),
        ('body','VARCHAR(100)', 0, 0),
        ('created_at','VARCHAR(20)', 0, 0),
        ('comments','INTEGER', 0, 0),
        ('userId','INTEGER', 0, 0),
        ('labelId','INTEGER', 0, 0)
    }
    cursor = conn.cursor()
    cursor.execute("SELECT p.name, p.type, p.'notnull', p.pk FROM pragma_table_info('PRList') p;")
    columns = set(cursor.fetchall())

    assert fields == columns

def test_sqlite_user_data():
    """
    SQLite 데이터베이스의 User 테이블 데이터를 검사합니다.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM User;")
    your_users = cursor.fetchall()

    users = {issue['user']['id'] for issue in dont_touch}
    
    assert {your_user[0] for your_user in your_users} == users

def test_sqlite_label_data():
    """
    SQLite 데이터베이스의 Label 테이블 데이터를 검사합니다.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM Label;")
    your_labels = cursor.fetchall()

    labels = {issue['labels'][0]['id'] for issue in dont_touch}
    
    assert {your_label[0] for your_label in your_labels} == labels

def test_sqlite_prlist_data():
    """
    SQLite 데이터베이스의 issue 테이블 데이터를 검사합니다.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM PRList;")
    your_prlists = cursor.fetchall()

    prlist = {issue['id'] for issue in dont_touch}
    
    assert {your_prlist[0] for your_prlist in your_prlists} == prlist