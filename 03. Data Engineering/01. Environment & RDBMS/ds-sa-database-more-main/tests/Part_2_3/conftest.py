import os
import sqlite3
import pytest
from string import Template
from src import Part_2


@pytest.fixture(autouse=True, scope="module")
def test_db_session():
    conn = sqlite3.connect(':memory:')
    yield conn
    conn.close()


@pytest.fixture(autouse=True, scope="function")
def cursor(test_db_session):
    pytest.cur = test_db_session.cursor()
    yield pytest.cur
    pytest.cur.close()


@pytest.fixture(autouse=True, scope="module")
def db_setup(test_db_session):
    cur = test_db_session.cursor()
    try:
        cur.execute(Part_2.QUERY_1)
        cur.execute(Part_2.QUERY_2)

    except Exception as e:
        print('Error occurred while executing Part 2 SQL')
        print(e)

@pytest.fixture(autouse=True, scope="module")
def part_2_insert_setup_teacher(test_db_session):
    cur = test_db_session.cursor()
    try:
        cur.execute(Part_2.QUERY_3_1)
        cur.execute(Part_2.QUERY_3_2)
        cur.execute(Part_2.QUERY_3_3)
        cur.execute(Part_2.QUERY_3_4)
        cur.execute(Part_2.QUERY_3_5)
        cur.execute(Part_2.QUERY_3_6)
        cur.execute(Part_2.QUERY_3_7)

    except Exception as e:
        print("INSERT 중 오류가 발생하였습니다")
        print('Error occurred while executing Part 2 INSERT')
        print(e)

@pytest.fixture(autouse=True, scope="module")
def part_2_insert_setup_student(test_db_session):
    cur = test_db_session.cursor()
    try:
        cur.execute(Part_2.QUERY_4_1)
        cur.execute(Part_2.QUERY_4_2)
        cur.execute(Part_2.QUERY_4_3)
        cur.execute(Part_2.QUERY_4_4)
        cur.execute(Part_2.QUERY_4_5)
        cur.execute(Part_2.QUERY_4_6)
        cur.execute(Part_2.QUERY_4_7)

    except Exception as e:
        print("INSERT 중 오류가 발생하였습니다")
        print('Error occurred while executing Part 2 INSERT')
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

