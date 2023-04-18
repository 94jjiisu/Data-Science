import pytest

@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from src.Part_1 import oneto100, factor
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')

def test_oneto100_return_correct_answer():
    from src.Part_1 import oneto100

    assert oneto100(10) == 55, "어떤 수를 넣어도 정확한 값을 반환해야합니다."
    assert oneto100(20) == 210, "어떤 수를 넣어도 정확한 값을 반환해야합니다."
    assert oneto100(30) == 465, "어떤 수를 넣어도 정확한 값을 반환해야합니다."
    assert oneto100(50) == 1275, "어떤 수를 넣어도 정확한 값을 반환해야합니다."
    assert oneto100(100) == 5050, "어떤 수를 넣어도 정확한 값을 반환해야합니다."


def test_oneto100_is_recursion():
    from src.Part_1 import oneto100

    assert oneto100.cnt > 200, "재귀함수로 문제를 해결해주세요!"

def test_factor_return_correct_answer():
    from src.Part_1 import factor

    assert factor(7, 19) == 1, "어떤 수를 넣어도 정확한 값을 반환해야합니다."
    assert factor(10, 40) == 10, "어떤 수를 넣어도 정확한 값을 반환해야합니다."
    assert factor(1071, 1029) == 21, "어떤 수를 넣어도 정확한 값을 반환해야합니다."
    assert factor(78696, 19332) == 36, "어떤 수를 넣어도 정확한 값을 반환해야합니다."
    assert factor(969280, 83729) == 1, "어떤 수를 넣어도 정확한 값을 반환해야합니다."
    assert factor(610411, 470636) == 1, "어떤 수를 넣어도 정확한 값을 반환해야합니다."
    assert factor(516880, 34632) == 104, "어떤 수를 넣어도 정확한 값을 반환해야합니다."

def test_factor_is_recursion():
    from src.Part_1 import factor

    assert factor.cnt > 30, "재귀함수로 문제를 해결해주세요!"
