import os
import pytest
from src import Part_1

TEST_PARAMS = [
    ('p1q1.pkl', Part_1.QUERY_1),
    ('p1q2.pkl', Part_1.QUERY_2),
    ('p1q3.pkl', Part_1.QUERY_3),
    ('p1q4.pkl', Part_1.QUERY_4),
    ('p1q5.pkl', Part_1.QUERY_5)
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


def test_part_1_question_1():
    """
    입력한 쿼리에 맞는 결과와 비교하는 테스트케이스 입니다.
    """
    query_tester(TEST_PARAMS[0][0], TEST_PARAMS[0][1])


def test_part_1_question_2():
    """
    입력한 쿼리에 맞는 결과와 비교하는 테스트케이스 입니다.
    """    
    query_tester(TEST_PARAMS[1][0], TEST_PARAMS[1][1])


def test_part_1_question_3():
    """
    입력한 쿼리에 맞는 결과와 비교하는 테스트케이스 입니다.
    """
    query_tester(TEST_PARAMS[2][0], TEST_PARAMS[2][1])


def test_part_1_question_4():
    """
    입력한 쿼리에 맞는 결과와 비교하는 테스트케이스 입니다.
    """
    query_tester(TEST_PARAMS[3][0], TEST_PARAMS[3][1])


def test_part_1_question_5():
    """
    입력한 쿼리에 맞는 결과와 비교하는 테스트케이스 입니다.
    """
    query_tester(TEST_PARAMS[4][0], TEST_PARAMS[4][1])
