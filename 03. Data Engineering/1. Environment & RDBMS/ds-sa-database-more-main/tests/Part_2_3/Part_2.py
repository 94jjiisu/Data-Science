import os
import pytest
from src import Part_2

TEST_PARAMS = [
    ('p2q4.pkl', Part_2.QUERY_4)
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


class TestTeachearTable:
    """
    Teachear 테이블에 대해서 테스트합니다.
    - 아래의 레퍼런스를 추가합니다.
    - http://webkebi.zany.kr:9003/board/bView.asp?bCode=19&aCode=2538
    """
    __tablename__='Teacher'

    __fields__ = [
        ('id', 'INTEGER', 0, 1),
        ('name', 'VARCHAR(30)',0,0),
        ('subject', 'VARCHAR(10)',1,0),
        ('salary','INTEGER',0,0)
    ]

    def test_teacher_table_exists(self, table_checker):
        # Teachear 테이블이 존재하는지 확인합니다.
        assert len(table_checker(self.__tablename__)) == 1
    def test_fields(self, field_checker):
        # Teachear 테이블 구조를 확인합니다.
        assert len(field_checker(self.__tablename__)) == 4
        assert comp_q_res(self.__fields__, field_checker(
            self.__tablename__)) is True

class TestStudentTable:
    """
    Student 테이블에 대해서 테스트합니다.
    - 아래의 레퍼런스를 추가합니다.
    - http://webkebi.zany.kr:9003/board/bView.asp?bCode=19&aCode=2538
    """
    __tablename__='Student'

    __fields__ = [
        ('teacher_id', 'INTEGER', 1, 1),
        ('student_id', 'CHAR(4)',1,2),
        ('age', 'INTEGER',1,0)
    ]

    def test_Student_table_exists(self, table_checker):
        # Student 테이블이 존재하는지 확인합니다.
        assert len(table_checker(self.__tablename__)) == 1
    def test_Student_fields(self, field_checker):
        # Student 테이블 구조를 확인합니다.
        assert len(field_checker(self.__tablename__)) == 3
        assert comp_q_res(self.__fields__, field_checker(
            self.__tablename__)) is True

def test_part_2_question_query_4():
    """
    src/Part_2 의 QUERY_4 가 문제의 요구사항에 맞게 실행되는지 확인합니다.
    """
    query_tester(TEST_PARAMS[0][0], TEST_PARAMS[0][1])
