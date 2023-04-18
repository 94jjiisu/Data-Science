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
def test_part3_import():
    try:
        from src.Part_3 import part3
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_part3_is_sort():
    from src.Part_3 import part3

    output = part3('a T C')
    assert output == 'C T a', '문자열 정렬이 이루어져야합니다.'

    output = part3('a b c d e f g')
    assert output == 'a b c d e f g', '문자열 정렬이 이루어져야합니다.'

    output = part3('z x y w v u t s')
    assert output == 's t u v w x y z', '문자열 정렬이 이루어져야합니다.'

    output = part3('z X y D c A b U')
    assert output == 'A D U X b c y z', '문자열 정렬이 이루어져야합니다.'

    output = part3('a a a C C b b F F d')
    assert output == 'C F a b d', '문자열이 중복된 경우, 중복을 제거하고 조건에 맞게 정렬이 이루어져야합니다.'

    output = part3('C c O o d D E e S T a t e s')
    assert output == 'C D E O S T a c d e o s t', '문자열이 중복된 경우, 중복을 제거하고 조건에 맞게 정렬이 이루어져야합니다.'
    

def test_part3_validation():
    from src.Part_3 import part3

    assert cnt_func_calls(part3, 'POP_JUMP_IF_FALSE') < 3, 'if문을 많이 사용하지 않고 문제를 해결할 수 있습니다.'
    assert cnt_func_calls(part3, 'CALL_FUNCTION') + cnt_func_calls(part3, 'CALL_METHOD') > 0, '내장함수, 메소드를 하나 이상 사용해야 합니다.'
    