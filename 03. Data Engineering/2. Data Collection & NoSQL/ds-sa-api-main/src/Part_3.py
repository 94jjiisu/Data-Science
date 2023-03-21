
import os
import sqlite3
# DB_FILENAME, DB_FILEPATH 변경하지 마세요
DB_FILENAME = "twitter_db.sqlite3"
DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)


def get_cursor(DB_FILEPATH):
    """
    get_cursor 함수는 데이터베이스와 연결된 커서 객체를 리턴합니다.

    리턴 :
    - connection 인스턴스 : 데이터베이스와 연결된 connection 인스턴스를 리턴합니다.
    - cursor 인스턴스 : 데이터베이스에 sql 쿼리문을 보낼 수 있는 cursor 인스턴스를 러턴합니다.
    """
    conn = sqlite3.connect(DB_FILEPATH) # 라이브러리와 연결
    cur = conn.cursor() # cursor는 핸들러와 같은 역할
    return conn, cur


def init_database():
    """
    데이터베이스를 초기화해주는 함수입니다.
    """

    conn, cur = get_cursor(DB_FILEPATH)
    cur.execute("DROP TABLE IF EXISTS user;")
    cur.execute("DROP TABLE IF EXISTS tweet;")

    cur.execute("""CREATE TABLE user ( 
        id INTEGER NOT NULL PRIMARY KEY,
        screen_name VARCHAR UNIQUE
    );""")

    cur.execute("""CREATE TABLE tweet ( 
        id INTEGER NOT NULL PRIMARY KEY,
        full_text VARCHAR,
        user_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES user(id)
        );
    """)


def add_user(username, connection, cursor):
    """
    add_user 함수는 username 을 기반으로 user 를 새로 추가하고 해당 user 객체를 리턴합니다.
    - username 을 가지고 있는 유저가 기존에 존재한다면 유저를 추가하지 않습니다.
    - id 는 자동으로 생성되어도, 여러분이 생성하셔도 상관없습니다.
    - 해당 함수가 끝나면 데이터베이스에 데이터가 입력되어 있어야합니다.

    파라미터:
        - username: 추가할 유저 이름을 담은 문자열(str) 입니다.
        - connection 인스턴스 : 데이터베이스와 연결된 connection 인스턴스 입니다.
        - cursor 인스턴스 : 데이터베이스에 sql 쿼리문을 보낼 수 있는 cursor 인스턴스 입니다.
    """
    cursor.execute("""
    SELECT * 
    FROM user
    WHERE screen_name = ?
    ;""",
    (username,))

    data = cursor.fetchone()

    if data is None:
        cursor.execute("""
        INSERT INTO user (screen_name)
        VALUES (?);""",
        (username,))
        connection.commit()
    

def add_tweet(username, tweet_text, connection, cursor):
    """
    add_tweet 함수는 tweet_text 와 username 이 주어지면 해당 유저와 연결된
    새로운 트윗을 추가합니다.
    - username 에 해당하는 유저가 user 테이블에 없다면, user 테이블에 username 에 해당하는 user를 추가해야합니다.

    파라미터:
        - username: 추가할 유저 이름을 담은 문자열(str) 입니다.
        - tweet_text: 추가할 트윗을 담은 문자열(str) 입니다.
        - connection 인스턴스 : 데이터베이스와 연결된 connection 인스턴스 입니다.
        - cursor 인스턴스 : 데이터베이스에 sql 쿼리문을 보낼 수 있는 cursor 인스턴스 입니다.
    """

    cursor.execute("""
    SELECT *
    FROM user
    WHERE screen_name = (?)
    ;""",
    (username,))

    data = cursor.fetchone()
    if data is None:
        cursor.execute("INSERT INTO user (screen_name) VALUES (?);", (username,))
        connection.commit()

        cursor.execute("""SELECT id 
        FROM user
        WHERE screen_name = (?);""", 
        (username,))
        data = cursor.fetchone()
    
    cursor.execute("INSERT INTO tweet (full_text, user_id) VALUES (?,?);", (tweet_text, data[0]))
    connection.commit()



def delete_user(user_id, connection, cursor):
    """
    delete_user 함수는 user_id 가 주어지면 데이터베이스에서 해당 user 를 삭제합니다.
    - user 와 연관된 연관된 tweet 테이블의 tweet 들도 같이 삭제해야 합니다.

    파라미터:
        - user_id: 데이터베이스에서 삭제할 트윗 레코드 고유번호(int) 입니다.
        - connection 인스턴스 : 데이터베이스와 연결된 connection 인스턴스 입니다.
        - cursor 인스턴스 : 데이터베이스에 sql 쿼리문을 보낼 수 있는 cursor 인스턴스 입니다.
    """
    cursor.execute("DELETE FROM user WHERE id = (?);", (user_id,))
    cursor.execute("DELETE FROM tweet WHERE user_id = (?);", (user_id,))
    connection.commit()


def delete_tweet(tweet_id, connection, cursor):
    """
    tweetid 가 주어지면 해당 트윗이 데이터베이스에 존재할 경우 삭제하는 함수입니다.
    """
    cursor.execute("DELETE FROM tweet WHERE id = (?);", (tweet_id,))
    connection.commit()

conn, cur = get_cursor(DB_FILEPATH)
init_database()

jisu = "Hello World"
add_user(jisu, conn, cur)

add_tweet(jisu, '바라쿠다', conn, cur)
add_tweet(jisu, '투나', conn, cur)

kim = "showmethemoney"
add_tweet(kim, "show me the money", conn, cur)
add_tweet(kim, "power overwhelming", conn, cur)