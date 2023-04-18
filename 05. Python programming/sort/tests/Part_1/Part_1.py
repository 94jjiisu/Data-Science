from random import *
import dis
import copy
import pytest

@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from src.Part_1 import bubble_sort, insertion_sort, selection_sort
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def count_func_calls(fn, s = ''):
    cnt = 0
    bytecode = dis.Bytecode(fn)
    instrs = list(reversed([instr for instr in bytecode]))
    for (ix, instr) in enumerate(instrs):
        print(ix, instr)
        if instr.opname==s:
            cnt += 1
    return cnt


def list_funcs_calls(fn):
    funcs = []
    bytecode = dis.Bytecode(fn)
    instrs = list(reversed([instr for instr in bytecode]))
    for (ix, instr) in enumerate(instrs):
        if instr.opname=="CALL_FUNCTION":
            load_func_instr = instrs[ix + instr.arg + 1]
            funcs.append(load_func_instr.argval)
    return funcs


def test_bubble_running_normally():
    from src.Part_1 import bubble_sort

    li = [54, 26, 93, 17, 77, 31]
    bubble_sort(li)
    assert li == [17, 26, 31, 54, 77, 93]

    li = [10, 2, 3, 4, 1, 7, 0]
    bubble_sort(li)
    assert li == [0, 1, 2, 3, 4, 7, 10]


def test_bubble_sort_8000():
    from src.Part_1 import bubble_sort

    li = []
    for i in range(0, 8000):
        n = randint(1, 100000)
        li.append(n)
    li_copy = copy.deepcopy(li)
    li_sorted = sorted(li_copy)

    bubble_sort(li)

    assert li_sorted == li, "어떤 경우에서도 정렬이 이루어져야합니다."


def test_bubble_func_calls():
    from src.Part_1 import bubble_sort
    
    assert count_func_calls(bubble_sort, "CALL_METHOD") == 0, '메소드를 사용하면 안됩니다.'
    assert "sorted" not in list_funcs_calls(bubble_sort), 'sorted 내장함수를 사용하면 안됩니다.'
    assert count_func_calls(bubble_sort, "POP_JUMP_IF_FALSE") != 0, "조건문을 사용해야합니다."
    assert count_func_calls(bubble_sort, "FOR_ITER") != 0, "반복문을 사용해야합니다."


def test_insertion_running_normally():
    from src.Part_1 import insertion_sort

    li = [54, 26, 93, 17, 77, 31]
    insertion_sort(li)
    assert li == [17, 26, 31, 54, 77, 93]

    li = [10, 2, 3, 4, 1, 7, 0]
    insertion_sort(li)
    assert li == [0, 1, 2, 3, 4, 7, 10]


def test_insertion_sort_8000():
    from src.Part_1 import insertion_sort

    li = []
    for i in range(0, 8000):
        n = randint(1, 100000)
        li.append(n)
    li_copy = copy.deepcopy(li)
    li_sorted = sorted(li_copy)

    insertion_sort(li)

    assert li_sorted == li, "어떤 경우에서도 정렬이 이루어져야합니다."


def test_insertion_func_calls():
    from src.Part_1 import insertion_sort
    
    assert count_func_calls(insertion_sort, "CALL_METHOD") == 0, '메소드를 사용하면 안됩니다.'
    assert "sorted" not in list_funcs_calls(insertion_sort), 'sorted 내장함수를 사용하면 안됩니다.'
    assert count_func_calls(insertion_sort, "POP_JUMP_IF_FALSE") != 0, "조건문을 사용해야합니다."
    assert count_func_calls(insertion_sort, "FOR_ITER") != 0, "반복문을 사용해야합니다."


def test_selection_running_normally():
    from src.Part_1 import selection_sort

    li = [54, 26, 93, 17, 77, 31]
    selection_sort(li)
    assert li == [17, 26, 31, 54, 77, 93]

    li = [10, 2, 3, 4, 1, 7, 0]
    selection_sort(li)
    assert li == [0, 1, 2, 3, 4, 7, 10]


def test_selection_sort_8000():
    from src.Part_1 import selection_sort

    li = []
    for i in range(0, 8000):
        n = randint(1, 100000)
        li.append(n)
    li_copy = copy.deepcopy(li)
    li_sorted = sorted(li_copy)

    selection_sort(li)

    assert li_sorted == li, "어떤 경우에서도 정렬이 이루어져야합니다."


def test_selection_func_calls():
    from src.Part_1 import selection_sort
    
    assert count_func_calls(selection_sort, "CALL_METHOD") == 0, '메소드를 사용하면 안됩니다.'
    assert "sorted" not in list_funcs_calls(selection_sort), 'sorted 내장함수를 사용하면 안됩니다.'
    assert count_func_calls(selection_sort, "POP_JUMP_IF_FALSE") != 0, "조건문을 사용해야합니다."
    assert count_func_calls(selection_sort, "FOR_ITER") != 0, "반복문을 사용해야합니다."