import os
import pytest
from src import Part_2

TEST_PARAMS = [
    ('p2q1.pkl', Part_2.QUERY_1),
    ('p2q2.pkl', Part_2.QUERY_2),
    ('p2q3.pkl', Part_2.QUERY_3),
    ('p2q4.pkl', Part_2.QUERY_4),
    ('p2q5.pkl', Part_2.QUERY_5),
    ('p2q6.pkl', Part_2.QUERY_6),
    ('p2q7.pkl', Part_2.QUERY_7),
    ('p2q8.pkl', Part_2.QUERY_8),
    ('p2q9.pkl', Part_2.QUERY_9),
    ('p2q10.pkl', Part_2.QUERY_10)
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


def test_question_1():
    query_tester(TEST_PARAMS[0][0], TEST_PARAMS[0][1])


def test_question_2():
    query_tester(TEST_PARAMS[1][0], TEST_PARAMS[1][1])


def test_question_3():
    query_tester(TEST_PARAMS[2][0], TEST_PARAMS[2][1])


def test_question_4():
    query_tester(TEST_PARAMS[3][0], TEST_PARAMS[3][1])


def test_question_5():
    query_tester(TEST_PARAMS[4][0], TEST_PARAMS[4][1])


def test_question_6():
    query_tester(TEST_PARAMS[5][0], TEST_PARAMS[5][1])


def test_question_7():
    query_tester(TEST_PARAMS[6][0], TEST_PARAMS[6][1])


def test_question_8():
    query_tester(TEST_PARAMS[7][0], TEST_PARAMS[7][1])


def test_question_9():
    query_tester(TEST_PARAMS[8][0], TEST_PARAMS[8][1])


def test_question_10():
    query_tester(TEST_PARAMS[9][0], TEST_PARAMS[9][1])
