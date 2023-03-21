import os
import pytest


def test_passenger_table(cursor):
    check_sql = """SELECT EXISTS (
                    SELECT 1
                    FROM information_schema.tables
                    WHERE table_name='passenger');"""

    cursor.execute(check_sql)

    res = cursor.fetchone()

    assert len(res) == 1
    assert res[0] is True


def get_pkl(file_name):
    file_path = os.path.join(pytest.RESOURCE_PATH, file_name)
    return pytest.pkl_opener(file_path)


def comp_q_res(base, comparison):
    for t in comparison:
        if t not in base:
            return False
    return True


def test_titanic_data(cursor):
    select_sql = "SELECT * FROM passenger;"

    cursor.execute(select_sql)
    res = cursor.fetchall()

    test_res = get_pkl('p3data.pkl')

    assert len(res) == 878
    assert comp_q_res(test_res, res) is True