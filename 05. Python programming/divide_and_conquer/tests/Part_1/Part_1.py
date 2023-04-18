from random import *
import copy
import pytest


@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from src.Part_1 import quick_sort
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_quick_sort_running_normally():
    from src.Part_1 import quick_sort

    li = [54, 26, 93, 17, 77, 31]
    assert quick_sort(li) == [17, 26, 31, 54, 77, 93], "정렬이 이루어져야합니다."

    li = [10, 2, 3, 4, 1, 7, 0]
    assert quick_sort(li) == [0, 1, 2, 3, 4, 7, 10], "정렬이 이루어져야합니다."


def test_quick_sort_100():
    from src.Part_1 import quick_sort

    li = []
    for _ in range(0, 100):
        n = randint(1, 1000)
        li.append(n)

    li_copy = copy.deepcopy(li)
    li_sorted = sorted(li_copy)

    assert li_sorted == quick_sort(li), f"어떤 경우에서도 정렬이 이루어져야합니다.\ninput => {li}\noutput => {quick_sort(li)}"


def test_quick_sort_func_calls():
    from src.Part_1 import quick_sort
    
    assert quick_sort.cnt > 30, "재귀함수로 문제를 해결해주세요!"
    