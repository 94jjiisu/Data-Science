import os
import pytest
import shutil
import sqlite3

@pytest.fixture(scope="module")
def test_db_session():
    DB_FILENAME = 'STORE.db'
    DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)
    TESTDB_FILEPATH = os.path.join(os.path.dirname(__file__), 'test.db')

    shutil.copy(DB_FILEPATH, TESTDB_FILEPATH, follow_symlinks=True)

    if not os.path.isfile(DB_FILEPATH):
        print(f'{DB_FILENAME} not found')
        return

    conn = sqlite3.connect(TESTDB_FILEPATH)
    yield conn
    conn.close()
    os.remove(TESTDB_FILEPATH)

@pytest.fixture(autouse=True, scope="function")
def cursor(test_db_session):
    pytest.cur = test_db_session.cursor()
    yield
    pytest.cur.close()
