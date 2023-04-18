import pytest


@pytest.fixture(autouse=True)
def test_part3_import():
    try:
        from src.Part_3 import Deque
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


@pytest.mark.timeout(10)
def test_part1_Queue_append():
    from src.Part_3 import Deque
    from random import shuffle

    try:
        li = ([n for n in range(0,8)])
        shuffle(li)

        deq = Deque()
        for item in li:
            deq.append(item)

        assert deq.ord_desc() == li, 'Deque의 append가 정상적으로 작동해야합니다.'


    except Exception as e:
        pytest.fail(f'{e} \n 에러가 발생하였습니다. 코드를 다시 한 번 확인해주세요.')


@pytest.mark.timeout(10)
def test_part1_Queue_pop():
    from src.Part_3 import Deque
    from random import shuffle

    try:
        li = ([n for n in range(0,8)])
        shuffle(li)

        deq = Deque()
        for item in li:
            deq.append(item)

        li.reverse()
        for idx in range(0, len(li)):
            assert li[idx] == deq.pop(),'Deque의 pop이 정상적으로 작동해야합니다.'

        assert deq.pop() == None, 'deque에 아무것도 없을 때 pop은 None을 반환해야합니다.'

    except Exception as e:
        pytest.fail(f'{e} \n 에러가 발생하였습니다. 코드를 다시 한 번 확인해주세요.')
        

@pytest.mark.timeout(10)
def test_part1_Queue_appendleft():
    from src.Part_3 import Deque
    from random import shuffle

    try:
        li = ([n for n in range(0,8)])
        shuffle(li)

        deq = Deque()
        for item in li:
            deq.appendleft(item)

        li.reverse()
        assert deq.ord_desc() == li, 'Deque의 appendleft가 정상적으로 작동해야합니다.'


    except Exception as e:
        pytest.fail(f'{e} \n 에러가 발생하였습니다. 코드를 다시 한 번 확인해주세요.')


@pytest.mark.timeout(10)
def test_part1_Queue_popleft():
    from src.Part_3 import Deque
    from random import shuffle

    try:
        li = ([n for n in range(0,8)])
        shuffle(li)

        deq = Deque()
        for item in li:
            deq.append(item)

        for idx in range(0, len(li)):
            assert li[idx] == deq.popleft(),'Deque의 popleft가 정상적으로 작동해야합니다.'

        assert deq.popleft() == None, 'deque에 아무것도 없을 때 popleft는 None을 반환해야합니다.'

    except Exception as e:
        pytest.fail(f'{e} \n 에러가 발생하였습니다. 코드를 다시 한 번 확인해주세요.')
    
        
@pytest.mark.timeout(10)
def test_part1_Queue_working_normally():
    from src.Part_3 import Deque
    from random import shuffle

    try:
        left = ([n for n in range(0,8)])
        right = ([n for n in range(8,16)])
        shuffle(left)
        shuffle(right)

        deq = Deque()

        for item in right:
            deq.append(item)
        
        for item in left:
            deq.appendleft(item)
        
        left.reverse()
        tot_li = left + right
        assert tot_li == deq.ord_desc(), 'append, appendleft가 정상적으로 작동해야합니다.'
    
        for _ in range(0, 8):
            assert deq.pop() == tot_li.pop(-1), 'pop메소드가 정상적으로 작동해야합니다.'
            assert deq.popleft() == tot_li.pop(0), 'popleft메소드가 정상적으로 작동해야합니다.'


    except Exception as e:
        pytest.fail(f'{e} \n 에러가 발생하였습니다. 코드를 다시 한 번 확인해주세요.')

    