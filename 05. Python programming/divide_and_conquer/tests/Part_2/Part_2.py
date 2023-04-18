from random import *
import copy
import pytest


@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from src.Part_2 import merge, merge_sort
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_merge_running_normally():
    from src.Part_2 import merge
    
    left = [4,6,7,10]
    right = [1,3,9,12]
    assert merge(left, right) == [1, 3, 4, 6, 7, 9, 10, 12], \
        'merge함수는 두 리스트를 합쳐 오름차순으로 정렬된 리스트를 반환해야합니다'

    left = [1,3,5,7,9,11]
    right = [2,4,6,8,10,12]
    assert merge(left, right) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], \
        'merge함수는 두 리스트를 합쳐 오름차순으로 정렬된 리스트를 반환해야합니다'


def test_merge_random_check():
    from src.Part_2 import merge

    left = []
    right = []
    for _ in range(0, 20):
        n = randint(1, 100)
        left.append(n)

    for _ in range(0, 20):
        n = randint(1, 100)
        right.append(n)

    left.sort()
    right.sort()
    tot = left + right
    tot.sort()

    assert tot == merge(left,right), \
        f"어떤 경우에서도 두 리스트를 합쳐 정렬된 리스트를 반환해야합니다.\nleft => {left} \nright=> {right}\nmerge(left,right) => {merge(left,right)}"


def test_merge_sort_running_normally():
    from src.Part_2 import merge_sort

    li = [54, 26, 93, 17, 77, 31]
    assert merge_sort(li) == [17, 26, 31, 54, 77, 93]

    li = [10, 2, 3, 4, 1, 7, 0]
    assert merge_sort(li) == [0, 1, 2, 3, 4, 7, 10]


def test_merge_sort_100():
    from src.Part_2 import merge_sort

    li = []
    for _ in range(0, 100):
        n = randint(1, 100)
        li.append(n)

    li_copy = copy.deepcopy(li)
    li_sorted = sorted(li_copy)

    assert li_sorted == merge_sort(li), f"어떤 경우에서도 정렬이 이루어져야합니다.\ninput => {li}\noutput => {merge_sort(li)}"


def test_merge_sort_func_calls():
    from src.Part_2 import merge_sort
    
    assert merge_sort.cnt > 30, "재귀함수로 문제를 해결해주세요!"
    