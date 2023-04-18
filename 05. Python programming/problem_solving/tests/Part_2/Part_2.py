import dis
import pytest
from random import *


@pytest.fixture(autouse=True)
def test_part2_import():
    try:
        from src.Part_2 import part2
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def list_method_calls(fn, not_in_use):

    bytecode = dis.Bytecode(fn)
    instrs = list(reversed([instr for instr in bytecode]))
    num = 0
    for (ix, instr) in enumerate(instrs):
        if instr.opname=="CALL_METHOD" or instr.opname=="CALL_FUNCTION" or instr.opname=="LOAD_GLOBAL":
            if not_in_use in str(instr):
                num += 1
    return num


def test_part2_working_normally():
    from src.Part_2 import part2

    for _ in range(0, 10):
        li_len = randint(5, 10)
        li = []
        for n in range(0, li_len):
            li.append(randint(1, 100))
        res = part2(li)
        assert sorted(li)[-1] == res, "리스트의 최댓값을 반환해야합니다."


def test_part2_dont_use_max():
    from src.Part_2 import part2
    
    test_list1 = [4, 8, 5, 11, 7, 2]
    assert part2(test_list1) == 11, "먼저 정확한 값을 반환해야합니다."
    assert list_method_calls(part2, "max") == 0, "max 함수를 사용하면 안됩니다"


def test_part2_dont_use_sort():
    from src.Part_2 import part2

    test_list1 = [4, 8, 5, 11, 7, 2]
    assert part2(test_list1) == 11, "먼저 정확한 값을 반환해야합니다."
    assert list_method_calls(part2, "sort") == 0, "sort 함수를 사용하면 안됩니다"


def test_part2_dont_use_sorted():
    from src.Part_2 import part2
    
    test_list1 = [4, 8, 5, 11, 7, 2]
    assert part2(test_list1) == 11, "먼저 정확한 값을 반환해야합니다."
    assert list_method_calls(part2, "sorted") == 0, "sorted 함수를 사용하면 안됩니다"
    