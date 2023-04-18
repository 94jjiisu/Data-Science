import pytest

@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from src.Part_1 import part1_q1_answer, part1_q2_answer, part1_q3_answer
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_part1_q1_answer_test():
    from src.Part_1 import part1_q1_answer

    t_ord = 0
    (time_complexity, reason) = part1_q1_answer()
    for i in time_complexity:
        t_ord += ord(i)
    assert t_ord == 209, "정확한 시간복잡도를 반환해야합니다."
    assert reason != "이유를 작성해주세요" or len(reason) <= 1,\
        "시간복잡도의 이유를 작성해주세요"


def test_part1_q2_answer_test():
    from src.Part_1 import part1_q2_answer

    t_ord = 0
    (time_complexity, reason) = part1_q2_answer()
    for i in time_complexity:
        t_ord += ord(i)
    assert t_ord == 270, "정확한 시간복잡도를 반환해야합니다."
    assert reason != "이유를 작성해주세요" or len(reason) <= 1,\
        "시간복잡도의 이유를 작성해주세요"


def test_part1_q3_answer_test():
    from src.Part_1 import part1_q3_answer

    t_ord = 0
    (time_complexity, reason) = part1_q3_answer()
    for i in time_complexity:
        t_ord += ord(i)
    assert t_ord == 414, "정확한 시간복잡도를 반환해야합니다."
    assert reason != "이유를 작성해주세요" or len(reason) <= 1,\
        "시간복잡도의 이유를 작성해주세요"