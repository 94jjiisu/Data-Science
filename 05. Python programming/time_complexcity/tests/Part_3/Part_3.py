import pytest

@pytest.fixture(autouse=True)
def test_part3_import():
    try:
        from src.Part_3 import part3, part3_timecomplexity
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def find_value_in_list(input_list, value_to_search):
    res = []
    for i in range(0, len(input_list)):
        for j in range(0, len(input_list[i])):
            if input_list[i][j] == value_to_search:
                res.append((i,j))
    return res


def test_part3_working_normaly():
    from src.Part_3 import part3

    input_list = [
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8,9,10],
        [1,2,4,8,16,32],
        [1,2,3,4,5,6]
    ]
    value_to_search = 8

    assert part3(input_list, value_to_search) == [(0, 7), (1, 7), (2, 3)], \
        '정확한 결과를 반환해야합니다.'


def test_part3_working_normaly2():
    from src.Part_3 import part3
    import random

    MAX_NUM = 30

    for _ in range(0,5):
        input_list = []
        input_list_len = random.randrange(1, 10)

        for i in range(0, input_list_len):
            cur_list = []
            cur_list_len = random.randrange(1, 10)
            
            for j in range(0, cur_list_len):
                cur_list.append(random.randrange(1, MAX_NUM))
            
            cur_list = list(set(cur_list))
            cur_list.sort()
            input_list.append(cur_list)

        
        value_to_search = random.randrange(1, MAX_NUM)

        assert part3(input_list, value_to_search) == find_value_in_list(input_list, value_to_search),\
            f'모든 경우에서 제대로 작동해야합니다.\ninput_list = {input_list}\nvalue_to_search = {value_to_search}\n에서 에러가 발생하였습니다.'

        

def test_part3_timecomplexity():
    from src.Part_3 import part3_timecomplexity

    t_ord = 0
    (time_complexity, reason) = part3_timecomplexity()
    for i in time_complexity:
        t_ord += ord(i)
    assert t_ord == 702, "정확한 시간복잡도를 반환해야합니다."
    assert reason != "이유를 작성해주세요" or len(reason) <= 1,\
        "시간복잡도의 이유를 작성해주세요"