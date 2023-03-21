import os
import pytest
from src import Part_3

TEST_PARAMS = [
    ('p3q1.pkl', Part_3.QUERY_1),
    ('p3q2.pkl', Part_3.QUERY_2),
    ('p3q3.pkl', Part_3.QUERY_3)
]


def get_pkl(file_name):
    file_path = os.path.join(pytest.RESOURCE_PATH, file_name)
    return pytest.pkl_opener(file_path)


def comp_q_res(base, comparison):
    for t in comparison:
        if t not in base:
            return False
    return True

def query_tester(file_name, q):
    test_res = get_pkl(file_name)
    res = pytest.cur.execute(q).fetchall()

    assert len(res) == len(test_res)
    assert comp_q_res(test_res, res) is True


def test_part_3_question_1():
    query_tester(TEST_PARAMS[0][0], TEST_PARAMS[0][1])

def test_part_3_question_2():
    query_tester(TEST_PARAMS[1][0], TEST_PARAMS[1][1])

def test_part_3_question_3():
    query_tester(TEST_PARAMS[2][0], TEST_PARAMS[2][1])
