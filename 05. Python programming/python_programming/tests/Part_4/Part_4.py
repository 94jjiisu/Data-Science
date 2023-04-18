import dis
import pytest

def cnt_func_calls(fn, s=''):
    cnt = 0
    bytecode = dis.Bytecode(fn)
    instrs = list(reversed([instr for instr in bytecode]))
    for (ix, instr) in enumerate(instrs):
        if instr.opname==s:
            cnt+=1
    return cnt


@pytest.fixture(autouse=True)
def test_part4_import():
    try:
        from src.Part_4 import part4
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_part4_is_sort1(capfd):
    from src.Part_4 import part4

    assert part4('c t A') == 'a C T', '정렬 후, 대소문자를 변경해주세요.'


def test_part4_is_sort2(capfd):
    from src.Part_4 import part4

    assert part4('a b c d E F G') == 'e f g A B C D', '정렬 후, 대소문자를 변경해주세요.'

def test_part4_is_sort3(capfd):
    from src.Part_4 import part4

    assert part4('z X y W v U t S') == 's u w x T V Y Z', '정렬 후, 대소문자를 변경해주세요.'

def test_part4_is_sort4(capfd):
    from src.Part_4 import part4

    assert part4('C c O o d D E e S T a t e s') == 'c d e o s t A C D E O S T', '중복을 제거하고, 정렬 후, 대소문자를 변경해주세요.'

def test_part4_validation():
    from src.Part_4 import part4

    assert cnt_func_calls(part4, 'POP_JUMP_IF_FALSE') < 4, 'if문을 많이 사용하지 않고 문제를 해결할 수 있습니다.'
    assert cnt_func_calls(part4, 'CALL_FUNCTION') + cnt_func_calls(part4, 'CALL_METHOD') > 2, '내장함수, 메소드를 하나 이상 사용해야 합니다.'
