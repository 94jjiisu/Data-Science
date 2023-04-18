import dis
import pytest

def list_func_calls(fn):
    funcs = []
    bytecode = dis.Bytecode(fn)
    instrs = list(reversed([instr for instr in bytecode]))
    for (ix, instr) in enumerate(instrs):
        if instr.opname=="CALL_FUNCTION":
            load_func_instr = instrs[ix + instr.arg + 1]
            funcs.append(load_func_instr.argval)
    return funcs


@pytest.fixture(autouse=True)
def test_part2_is_square_num_import():
    try:
        from src.Part_2 import part2_is_square_num
    except :
        pytest.fail('part2_is_square_num 코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


@pytest.fixture(autouse=True)
def test_part2_is_odd_num_import():
    try:
        from src.Part_2 import part2_is_odd_num
    except :
        pytest.fail('part2_is_odd_num 코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_part2_is_square_num_lambda_used():
    from src.Part_2 import part2_is_square_num

    lambda_called = len([word for word in list_func_calls(part2_is_square_num) if '<lambda>' in str(word)])
    assert lambda_called > 0, \
        "part2_is_square_num 함수 내부에서 람다를 사용하였는지 확인해주세요. lambda를 함수의 매개변수 자리에서 사용해주세요."


def test_part2_is_odd_num_lambda_used():
    from src.Part_2 import part2_is_odd_num

    lambda_called = len([word for word in list_func_calls(part2_is_odd_num) if '<lambda>' in str(word)])
    assert lambda_called > 0, \
        "part2_is_odd_num 함수 내부에서 람다를 사용하였는지 확인해주세요. lambda를 함수의 매개변수 자리에서 사용해주세요."


def test_part2_is_square_num_return_correnct_answer():
    from src.Part_2 import part2_is_square_num

    assert part2_is_square_num([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25],\
        "매개변수로 들어온 리스트의 제곱수를 담고있는 리스트를 반환해주세요"
    assert part2_is_square_num([2, 4, 6, 8, 10, 12]) == [4, 16, 36, 64, 100, 144], \
        "매개변수로 들어온 리스트의 제곱수를 담고있는 리스트를 반환해주세요"
    assert part2_is_square_num([10, 11, 14, 16, 30, 31]) == [100, 121, 196, 256, 900, 961], \
        "매개변수로 들어온 리스트의 제곱수를 담고있는 리스트를 반환해주세요"
    

def test_part2_is_odd_num_return_correnct_answer():
    from src.Part_2 import part2_is_odd_num

    assert part2_is_odd_num([1, 2, 3, 4, 5]) == ['홀수', '짝수', '홀수', '짝수', '홀수'], \
        "매개변수로 들어온 리스트가 홀수인지 짝수인지 결과를 담고있는 리스트를 반환해주세요"
    assert part2_is_odd_num([2, 3, 6, 7, 10, 12]) == ['짝수', '홀수', '짝수', '홀수', '짝수', '짝수'], \
        "매개변수로 들어온 리스트가 홀수인지 짝수인지 결과를 담고있는 리스트를 반환해주세요"
    assert part2_is_odd_num([23, 34, 62, 42, 10, 14, 31, 57, 91]) == ['홀수', '짝수', '짝수', '짝수', '짝수', '짝수', '홀수', '홀수', '홀수'], \
        "매개변수로 들어온 리스트가 홀수인지 짝수인지 결과를 담고있는 리스트를 반환해주세요"
    