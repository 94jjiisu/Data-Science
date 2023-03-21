import os
import pytest
import sqlite3

@pytest.fixture
def create_tmp_db(tmpdir):
    filename = tmpdir.join('test.sqlite3')
    conn = sqlite3.connect(filename)
    yield conn
    conn.close()

@pytest.fixture
def test_cursor(create_tmp_db):
    cursor = create_tmp_db.cursor()
    yield cursor
    cursor.close()

@pytest.fixture
def northwind_conn():
    NW_DB_FILEPATH = os.path.join(os.getcwd(), 'data', 'northwind_small.sqlite3')
    conn = sqlite3.connect(NW_DB_FILEPATH)
    yield conn
    conn.close()

@pytest.fixture
def nw_cur(northwind_conn):
    cursor = northwind_conn.cursor()
    yield cursor
    cursor.close()

@pytest.fixture
def get_answer(nw_cur):
    def return_func(query):
        return nw_cur.execute(query).fetchall()
    return return_func
