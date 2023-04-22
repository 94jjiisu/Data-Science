import os
import sqlite3
from src import Part_2


def test_db_connection():
    path = Part_2.DATABASE_PATH

    conn = sqlite3.connect(path)

    try:
        cursor = conn.cursor()
        assert True
        cursor.close()
    except Exception as e:
        print('DB 와 연결할 수 없습니다')
        print(e)
        assert False
    finally:
        conn.close()


def test_store_by_page_num():
    test_db_path = os.path.join(os.path.dirname(__file__), 'test.db')

    conn = sqlite3.connect(test_db_path)

    test_title = '엔더스 게임'
    test_pg_num = 3

    Part_2.init_db(conn)
    Part_2.store_by_page_num(test_title, test_pg_num, conn)

    select_query = "SELECT COUNT(*) FROM Review;"

    cur = conn.cursor()

    review_count = cur.execute(select_query).fetchone()[0]
    print(review_count)

    assert review_count == test_pg_num * 10
