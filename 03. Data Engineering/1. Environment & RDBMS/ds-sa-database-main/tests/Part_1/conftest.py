import os
import sqlite3
import pytest
from string import Template
from src import Part_1


@pytest.fixture(autouse=True, scope="module")
def test_db_session():
    TEST_FILENAME = 'test.db'
    TEST_FILEPATH = os.path.join(os.path.dirname(__file__), TEST_FILENAME)

    if os.path.isfile(TEST_FILEPATH):
        os.remove(TEST_FILEPATH)

    conn = sqlite3.connect(TEST_FILEPATH)

    yield conn

    conn.close()

    try:
        os.remove(TEST_FILEPATH)
    except FileNotFoundError as e:
        print("File doesn't exist, see error for more detail")
        print(e)
    except Exception as e:
        print("Error occurred while removing test db file")
        print(e)


@pytest.fixture(autouse=True, scope="function")
def cursor(test_db_session):
    pytest.cur = test_db_session.cursor()
    yield pytest.cur
    pytest.cur.close()


@pytest.fixture(autouse=True, scope="module")
def db_setup(test_db_session):
    cur = test_db_session.cursor()
    try:
        cur.execute(Part_1.CUSTOMER_TABLE)
        cur.execute(Part_1.PACKAGE_TABLE)
        cur.execute(Part_1.CUSTOMER_PACKAGE_TABLE)
    except Exception as e:
        print('Error occurred while executing Part 1 SQL')
        print(e)


@pytest.fixture
def table_checker(cursor):
    query_tmpl = Template(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='$tbl';")

    def returner(tablename):
        return cursor.execute(query_tmpl.substitute(tbl=tablename)).fetchall()

    return returner

@pytest.fixture
def field_checker(cursor):
    query_tmpl = Template("SELECT p.name, p.type, p.'notnull', p.pk FROM pragma_table_info('$tbl') p;")

    def returner(tablename):
        return cursor.execute(query_tmpl.substitute(tbl=tablename)).fetchall()

    return returner
