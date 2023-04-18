"""
Advanced Requirements
    해싱하는 해시함수를 구현하는 방법은 다양합니다.

요구사항:
    아래의 예상입출력값을 보고 로직을 파악해주세요.

    입력받는 값은 아래 예상입출력값처럼 입력되야하며, 리스트 형태로 입력되야 합니다.

    예상입출력값
        케이스1)
        입력 : [7,2,4,5], 12
        출력 : [(5, 7)]

        케이스2)
        입력 : [12,3,9,0], 12
        출력 : [(9, 3), (0, 12)]


"""
from itertools import combinations

def hashing_sum(hashing_list, sum_value):
    hash_table = list(combinations(hashing_list, 2))
    hashing_result = []

    for i, j in hash_table:
        if i + j == sum_value:
            hashing_result.append((i, j))
    return hashing_result
