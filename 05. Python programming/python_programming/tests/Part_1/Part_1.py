import dis
import pytest

def list_method_calls(fn):
    funcs = []
    bytecode = dis.Bytecode(fn)
    instrs = list(reversed([instr for instr in bytecode]))
    for (ix, instr) in enumerate(instrs):
        if instr.opname=="CALL_METHOD":
            load_func_instr = instrs[ix + instr.arg + 1]
            funcs.append(load_func_instr.argval)
    return funcs


@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from src.Part_1 import part1
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_part1_working_normally():
    from src.Part_1 import part1
    
    assert part1() == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100], "정상적으로 작동해야합니다."
    assert part1() != [1, 4, 9, 16, 25, 36, 49, 64, 81, 10123], "잘못된 값을 반환하면 안됩니다."


def test_part1_use_collection_method():
    from src.Part_1 import part1

    assert len(list_method_calls(part1)) is not 0, "메소드를 하나 이상 사용해야합니다."
    