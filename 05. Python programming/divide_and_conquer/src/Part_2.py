"""
Bare Minimum Requirements
정렬을 구현하며 분할정복에 익숙해집니다.

요구사항:
    정렬은 대부분의 상황에서 활용되는 대표적인 개념입니다.
    분할정복 알고리즘을 한 번 상기하면서 정렬이라는 목적을 달성해봅니다.

    분할정복 알고리즘 개념을 적용하여 머지소트(합병정렬)를 작성해주세요.
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


def merge(left, right):
    """
    문제 1. 
        두 리스트를 받아 합치는 merge함수를 구현해주세요.
        단 매개변수로 들어오는 리스트는 오름차순으로 정렬된 상태의 리스트이며,
        반환되는 리스트역시 오름차순으로 정렬된 상태의 리스트여야합니다. 

        ex)
            l = [4,6,7,10]
            r = [1,3,9,12]
            merge(l,r) => [1, 3, 4, 6, 7, 9, 10, 12]

        파이썬에서 제공되는 sort와 같은 내장함수를 사용하면 안됩니다.
    """
    i = j = 0
    sorted = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1
    
    sorted.extend(left[i:])
    sorted.extend(right[j:])
    
    return sorted


@counter # 삭제하거나 변경하지 마세요!
def merge_sort(li):
    """
    문제 2.
        문제 1에서 만든 merge 함수를 사용하여 merge_sort를 완성해주세요.
        정렬되지 않은 리스트를 매개변수로 받아 오름차순으로 정렬된 리스트를 반환하는 
        merge_sort를 만들어주세요.

        작성되어있는 merge_sort함수를 재귀함수로 사용해주세요.
        merge_sort함수 내부에 새로운 재귀함수로 구현하시면 안됩니다. 
    """
    length = len(li)
    if length == 1:
        return li
    
    mid = length // 2

    left_partition = merge_sort(li[:mid])
    right_partition = merge_sort(li[mid:])

    return merge(left_partition, right_partition)
