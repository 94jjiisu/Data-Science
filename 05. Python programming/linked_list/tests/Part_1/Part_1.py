import dis
import pytest
from random import *


@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from src.Part_1 import Queue, Stack
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


@pytest.mark.timeout(10)
def test_part1_Queue_working_normally():
    from src.Part_1 import Queue
    from random import shuffle

    try:
        test_li = ([n for n in range(0,10)])
        shuffle(test_li)

        que = Queue()
        for item in test_li:
            que.enqueue(item)
        
        for _ in range(0,len(test_li)):
            assert test_li.pop(0) == que.dequeue(), 'enqueue가 Queue로직대로 작동해야합니다.'
            assert test_li == que.return_queue(), \
                'return_queue에는 남아있는 값들이 리스트 형태로 반환되어야합니다.'

        assert que.dequeue() == None, 'Queue에 아무것도 없는 상태에서 dequeue를 실행하는 경우 None를 반환해야합니다.'


    except Exception as e:
        pytest.fail(f'{e} \n 에러가 발생하였습니다. 코드를 다시 한 번 확인해주세요.')
    

@pytest.mark.timeout(10)
def test_part1_Stack_working_normally():
    from src.Part_1 import Stack
    from random import shuffle

    try:
        test_li = ([n for n in range(0,10)])
        shuffle(test_li)

        stk = Stack()
        for item in test_li:
            stk.push(item)
        
        for _ in range(0,len(test_li)):
            assert test_li.pop(-1) == stk.pop(), 'pop이 Stack로직대로 작동해야합니다.'
            assert test_li == stk.return_stack(), \
                'return_stack에는 남아있는 값들이 리스트 형태로 반환되어야합니다.'

        assert stk.pop() == None, 'Stack에 아무것도 없는 상태에서 pop을 실행하는 경우 None를 반환해야합니다.'

        
    except Exception as e:
        pytest.fail(f'{e} \n 에러가 발생하였습니다. 코드를 다시 한 번 확인해주세요.')
    
