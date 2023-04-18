import pytest
from random import *

@pytest.fixture(autouse=True)
def test_part3_import():
    try:
        from src.Part_3 import hashing_sum
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_part3_12():
    from src.Part_3 import hashing_sum

    num_arr = [7, 2, 4 ,5]
    pair_sum = 12
    result1 = hashing_sum(num_arr, pair_sum)
    assert  len(result1) == 1, "[7,2,4,5], 12가 입력되었을 때 결과값은 1개입니다."
    assert  result1[0][0] + result1[0][1] == pair_sum , "정확한 값을 반환해야합니다."

    num_arr = [12, 3, 9, 0]
    pair_sum = 12
    result2 = hashing_sum(num_arr, pair_sum)
    assert  len(result2) == 2, "[12, 3, 9, 0], 12가 입력되었을 때 결과값은 2개입니다."
    assert  result2[0][0] + result2[0][1] == pair_sum, "정확한 값을 반환해야합니다."
    assert  result2[1][0] + result2[1][1] == pair_sum, "정확한 값을 반환해야합니다."


def test_part3_random():
    from src.Part_3 import hashing_sum
    
    li = [n for n in range(0, 31)]
    num_arr = []

    while(len(li) != 0):
        idx = randint(0, len(li) - 1)
        num_arr.append(li[idx])
        del li[idx]

    pair_sum = 31
    result_arr = hashing_sum(num_arr, pair_sum)

    for a,b in result_arr:
        assert a + b == pair_sum, f"어떤 값에서든 정상적으로 작동해야합니다. {a} + {b} = {pair_sum}"
    

