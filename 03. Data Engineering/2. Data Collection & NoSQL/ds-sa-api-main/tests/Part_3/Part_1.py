import uuid

from src.Part_3 import (
                        os,
                        sqlite3,
                        add_user,
                        add_tweet,
                        delete_user,
                        DB_FILEPATH
                        )

database_exist = os.path.isfile(DB_FILEPATH)

def test_init_database():
    """
    데이터베이스가 생성되어 있는지 확인합니다.
    """
    assert database_exist == True

#sqlite 에서 테이블 리스트를 반환하는 쿼리 입니다.
table_exist_smt = "SELECT name \
                FROM sqlite_master \
                WHERE type IN ('table', 'view') \
                AND name NOT LIKE 'sqlite_%' \
                UNION ALL \
                SELECT name \
                FROM sqlite_temp_master \
                WHERE type IN ('table', 'view') \
                ORDER BY 1;"

def test_tweet_table(test_cursor):
    """
    트윗 테이블이 생성되어 있는지 확인합니다.
    """
    test_cursor.execute(table_exist_smt)
    result = test_cursor.fetchall()
    tables = [table[0] for table in result]

    assert ('tweet' in tables) == True

def test_user_table(test_cursor):
    """
    user라는 테이블이 생성되어 있는지 확인합니다.
    """
    test_cursor.execute(table_exist_smt)
    result = test_cursor.fetchall()
    tables = [table[0] for table in result]

    assert ('user' in tables) == True

def test_user_table_column(test_cursor):
    """
    유저 테이블의 컬럼을 확인합니다.
    """
    fields = {
        ('id','INTEGER', 1, 1),
        ('screen_name','VARCHAR', 0, 0)
    }

    user_column_smt = "SELECT p.name, p.type, p.'notnull', p.pk FROM pragma_table_info('user') p;"
    test_cursor.execute(user_column_smt)
    user_columns = set(test_cursor.fetchall())

    assert fields == user_columns

def test_tweet_table_column(test_cursor):
    """
    트윗 테이블의 컬럼을 확인합니다.
    """
    fields = {
        ('id','INTEGER', 1, 1),
        ('full_text','VARCHAR', 0, 0),
        ('user_id','INTEGER', 0, 0)
    }
    tweet_column_smt = "SELECT p.name, p.type, p.'notnull', p.pk FROM pragma_table_info('tweet') p;"
    test_cursor.execute(tweet_column_smt)
    tweet_columns = set(test_cursor.fetchall())

    assert fields == tweet_columns

def test_add_delete_single_user(test_connection, test_cursor):
    """
    새로운 유저가 추가 및 삭제 되는지 확인합니다.
    - 유저 추가 후 유저의 수를 확인합니다.
    - 유저 삭제 후 유저의 수를 확인합니다. 
    """

    user_count_smt = 'SELECT COUNT(*) FROM user'
    test_cursor.execute(user_count_smt)
    init_count = test_cursor.fetchone()[0]
    
    new_user = uuid.uuid4().hex[0:8]
    add_user(new_user, test_connection, test_cursor)
    add_user(new_user, test_connection, test_cursor)

    test_cursor.execute(user_count_smt)
    add_count = test_cursor.fetchone()[0]

    assert init_count + 1 == add_count

    user_id_smt = f"SELECT id FROM user WHERE screen_name='{new_user}'"
    test_cursor.execute(user_id_smt)
    user_id = test_cursor.fetchone()[0]
    delete_user(user_id, test_connection, test_cursor)

    test_cursor.execute(user_count_smt)
    delete_count = test_cursor.fetchone()[0]

    assert delete_count == init_count
    add_user('patrick', test_connection, test_cursor)

def test_add_tweets_exist_user(test_connection, test_cursor):
    """
    새로운 트윗이 추가 및 삭제 되는지 확인합니다.
    - 연결된 유저가 있는 트윗을 입력합니다.
    """

    # 연결될 유저가 있는 트윗을 입력
    tweet_count_smt = "SELECT COUNT(*) \
                        FROM tweet \
                        JOIN user \
                          ON tweet.user_id = user.id \
                       WHERE user.screen_name = 'patrick'"
    test_cursor.execute(tweet_count_smt)
    init_count = test_cursor.fetchone()[0]
    add_tweet('patrick', 'under the sea', test_connection,test_cursor)

    test_cursor.execute(tweet_count_smt)
    add_count = test_cursor.fetchone()[0]

    assert init_count + 1 == add_count
    
    user_id_smt = f"SELECT id FROM user WHERE screen_name='patrick'"
    test_cursor.execute(user_id_smt)
    user_id = test_cursor.fetchone()[0]

    delete_user(user_id, test_connection,test_cursor)

    test_cursor.execute(tweet_count_smt)
    delete_count = test_cursor.fetchone()[0]

    assert delete_count == init_count

    

def test_add_tweets_non_exist_user(test_connection, test_cursor):
    """
    새로운 트윗이 추가 및 삭제 되는지 확인합니다.
    - 연결된 유저가 없는 트윗을 입력합니다.
    """
    new_user = uuid.uuid4().hex[0:8]
    # 연결될 유저가 없는 트윗을 입력
    tweet_count_smt = f"SELECT COUNT(*) \
                         FROM tweet \
                         JOIN user \
                           ON tweet.user_id = user.id \
                        WHERE user.screen_name = '{new_user}'"
    test_cursor.execute(tweet_count_smt)
    init_count = test_cursor.fetchone()[0]

    # 연결될 유저가 없는 트윗을 입력
    
    add_tweet(new_user, 'under the sea', test_connection,test_cursor)

    test_cursor.execute(tweet_count_smt)
    add_count = test_cursor.fetchone()[0]

    assert init_count + 1 == add_count

    user_id_smt = f"SELECT id FROM user WHERE screen_name='{new_user}'"
    test_cursor.execute(user_id_smt)
    user_id = test_cursor.fetchone()[0]

    delete_user(user_id, test_connection,test_cursor)

    test_cursor.execute(tweet_count_smt)
    delete_count = test_cursor.fetchone()[0]

    assert delete_count == init_count

    

