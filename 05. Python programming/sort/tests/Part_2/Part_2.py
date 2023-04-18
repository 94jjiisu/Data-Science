import random
import pytest

@pytest.fixture(autouse=True)
def test_part2_import():
    try:
        from src.Part_2 import print_to_zero_pos, print_to_zero_neg
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')

def test_part2_pos():
    from src.Part_2 import print_to_zero_pos

    for i in range(0, 5):
        rd = random.randint(10, 100)
        result_list = []
        print_to_zero_pos(rd, result_list)
        assert result_list == [n for n in range(0, rd + 1)][::-1], "어떤 경우의 수에서도 가능해야합니다. {}에서 오류가 발생했습니다".format(rd)


def test_part2_neg():
    from src.Part_2 import print_to_zero_neg

    for i in range(0, 5):
        rd = random.randint(10, 100) * -1
        result_list = []
        print_to_zero_neg(rd, result_list)
        assert result_list == [n for n in range(rd, 1)], "어떤 경우의 수에서도 가능해야합니다. {}에서 오류가 발생했습니다".format(rd)


def test_part2_is_recursion():
    from src.Part_2 import print_to_zero_pos, print_to_zero_neg

    result_list = []
    print_to_zero_pos(5,result_list)
    assert result_list == [5,4,3,2,1,0], "먼저 문제가 해결되어야합니다."
    assert print_to_zero_pos.cnt >= 50, "재귀로 문제를 해결해야합니다." 

    result_list = []
    print_to_zero_neg(-3,result_list)
    assert result_list == [-3,-2,-1,0], "먼저 문제가 해결되어야합니다."
    assert print_to_zero_neg.cnt >= 50, "재귀로 문제를 해결해야합니다."
    