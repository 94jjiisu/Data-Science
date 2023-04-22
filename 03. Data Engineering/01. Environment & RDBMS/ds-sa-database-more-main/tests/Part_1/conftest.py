import os
import sqlite3
import pytest
import shutil

pytest.RESOURCE_PATH = os.path.join(os.getcwd(), 'tests', 'resources')

@pytest.fixture(scope="module")
def test_db_session_Part_1():
    DB_FILENAME = 'chinook.db'
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
def cursor(test_db_session_Part_1):
    pytest.cur = test_db_session_Part_1.cursor()
    yield pytest.cur
    pytest.cur.close()
