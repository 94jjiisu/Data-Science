import os
import sqlite3
from src import Part_1

"""
Part 2

해당 부분은 Advanced 이기 때문에 필수는 아닙니다.

init_db 는 이미 구현되어 있습니다.
"""

DATABASE_PATH = os.path.join(os.getcwd(), 'scrape_data.db')

conn = sqlite3.connect(DATABASE_PATH)


def store_by_page_num(movie_title, page_num=10, conn=conn):
    """
    store_by_page_num 함수는 영화 제목, 페이지 번호, 데이터베이스 커넥션 객체를
    받아 주어진 영화제목의 리뷰를 총 주어진 페이지 개수 만큼 스크레이핑 한 뒤에
    데이터베이스에 저장합니다.

    파라미터:
        - movie_title: 리뷰를 스크레이핑할 영화 제목이 담긴 문자열(str) 입니다.
        - page_num: 첫 번째 페이지에서부터 스크레이핑할 페이지 개수가 담긴
        숫자(int) 입니다.
        - conn: 데이터베이스와 연결되 커넥션 객체

    리턴:
        - 별도로 없습니다.
    """
    #pass

    reviews = Part_1.scrape_by_page_num(movie_title, page_num)

    cur = conn.cursor()
    init_db()

    for r in reviews:
        cur.execute("INSERT INTO Review (review_text, review_star, movie_title) VALUES (?,?,?);",
        (r['review_text'], r['review_star'], movie_title))

    conn.commit()
        

def init_db(conn=conn):
    """
    init_db 함수는 Review 테이블을 초기화해주는 함수입니다.

    실행을 하게 되면 파라미터로 전해지는 conn 객체가 연결된 데이터베이스에서
    Review 테이블이 존재하면 DROP 하고 새로 생성해줍니다.

    기본적으로 Part_2.py 에 있는 conn 객체와 연결을 시도합니다.
    """

    create_table = """CREATE TABLE Review (
                        id INTEGER,
                        review_text TEXT,
                        review_star FLOAT,
                        movie_title VARCHAR(128),
                        PRIMARY KEY (id)
                        );"""

    drop_table_if_exists = "DROP TABLE IF EXISTS Review;"

    cur = conn.cursor()

    cur.execute(drop_table_if_exists)
    cur.execute(create_table)
    cur.close()
