"""
Bare Minimum Requirements
정렬을 구현하며 분할정복에 익숙해집니다.

요구사항:
    정렬은 대부분의 상황에서 활용되는 대표적인 개념입니다.
    분할정복 알고리즘을 한 번 상기하면서 정렬이라는 목적을 달성해봅니다.

    분할정복 알고리즘 개념을 적용하여 퀵소트를 작성해주세요.
    파이썬에서 제공되는 sort와 같은 내장함수를 사용하면 안됩니다.
    분할정복을 활용하여 구현하시길 바랍니다.
    
    각 문제 코드 위에 작성된 '@counter'는 변경하지 마세요.
"""

class counter:
    """
    해당 코드를 수정하지 마세요! 
    """
    def __init__(self, function):
        self.function = function
        self.cnt = 0

    def __call__(self, *args, **kwargs):
        self.cnt += 1
        return self.function(*args, **kwargs)


@counter    # 삭제하거나 변경하지 마세요!
def quick_sort(li):
    """
    정렬되지 않은 리스트를 매개변수로 받아 오름차순으로 정렬된 리스트를 반환하는 
    quick_sort를 만들어주세요.

    작성되어있는 quick_sort함수를 재귀함수로 사용해주세요.
    quick_sort함수 내부에 새로운 재귀함수로 구현하시면 안됩니다. 
    """
    if len(li) <= 1:
        return li

    pivot = li[0]
    tail = li[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x> pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)