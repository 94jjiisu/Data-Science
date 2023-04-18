from random import *
import pytest

@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from src.Part_1 import memo_fib, tabul_fib

    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')

def fib(input_value):
    if input_value == 1:
        return 1

    elif input_value == 2:
        return 1

    else:
        return fib(input_value - 1) + fib(input_value - 2)


def test_memo_fib_is_fib():
    from src.Part_1 import memo_fib

    for _ in range(0, 10):
        num = randint(1, 35)
        save_memo = {}
        assert memo_fib(num, save_memo) == fib(num), \
            "memo_fib 함수는 피보나치 수열에 맞추어 값을 반환해야합니다."


def test_memo_fib_memoization():
    from src.Part_1 import memo_fib
    for _ in range(0, 10):
        num = randint(2, 35)
        save_memo = {}
        memo_fib(num, save_memo)
        for k in range(2, num):
            print(save_memo)
            assert save_memo[k] == fib(k), \
                "memo_fib 함수는 메모이제이션을 통해 save_memo에 결과값을 저장해야합니다."
    

def test_tabul_fib_is_fib():
    from src.Part_1 import tabul_fib

    for _ in range(0, 10):
        num = randint(1, 35)
        assert tabul_fib(num) == fib(num), \
            "tabul_fib 함수는 피보나치 수열에 맞추어 값을 반환해야합니다."


def test_memo_fib_is_recursion():
    from src.Part_1 import memo_fib
    assert memo_fib.cnt >= 50, 'memo_fib함수는 재귀로 구현해야합니다.'



def test_tabul_fib_is_recursion():
    from src.Part_1 import tabul_fib
    assert tabul_fib.cnt == 10, 'tabul_fib함수는 재귀로 구현하면 안됩니다.'