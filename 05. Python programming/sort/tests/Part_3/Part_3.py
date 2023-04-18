from random import *
import pytest

@pytest.fixture(autouse=True)
def test_part3_import():
    try:
        from src.Part_3 import print_to_zero_pos_neg
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')

def test_part3():
    from src.Part_3 import print_to_zero_pos_neg

    for i in range(0, 5):
        t = randint(5, 10)
        li = []
        st = ''

        for i in range(0, t):
            n = randint(-20, 20)
            li.append(str(n))

        st = ','.join(li)

        result_dir = {}
        print_to_zero_pos_neg(st,result_dir)

        for i in li:
            num = int(i)
            if num > 0:
                assert result_dir[i] == list(map(str, [n for n in range(num, -1, -1)])), "어떤 경우의 수에서도 가능해야합니다."

            else:
                assert result_dir[i] == list(map(str, [n for n in range(num, 1)])), "어떤 경우의 수에서도 가능해야합니다."
                

def test_part3_is_recursion():
    from src.Part_3 import print_to_zero_pos_neg
    
    assert print_to_zero_pos_neg.cnt >= 20, "재귀로 문제를 해결해야합니다." 
    