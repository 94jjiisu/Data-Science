import dis
import pytest

def list_func_calls(fn, s):
    cnt = 0
    bytecode = dis.Bytecode(fn)
    instrs = list(reversed([instr for instr in bytecode]))
    for (ix, instr) in enumerate(instrs):
        if instr.opname==s:
            cnt += 1
    return cnt


@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from src.Part_1 import part1
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_part1_use_statement():
    from src.Part_1 import part1
    
    assert list_func_calls(part1, "GET_ITER") != 0, '연산을 통해 결과값이 나와야합니다.'


def test_part1_working_normally():
    from src.Part_1 import part1
    
    assert part1() == [35, 70], "정상적으로 작동해야합니다."
    assert list_func_calls(part1, "POP_JUMP_IF_FALSE") == 0, '컴프리헨션을 사용하여 문제를 해결해야합니다.'

