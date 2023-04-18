"""
Bare Minimum Requirements
해시충돌 상황을 판단하고 해결해봅니다.

요구사항:
    주어진 소스코드를 참조하여 결과값에서 충돌발생되는 부분을 수정해주세요.

    충돌이 발생하지 않도록 체이닝기법을 이해하고 활용하여 코드를 작성해주세요.

    충돌이 발생하지 않는다면 'A', 'B', 'C', 'D', 'E' 값이 순서상관없이 모두 연결되어 나올 것입니다.
    아래 입력값과 출력값을 참조하며 문제를 해결해봅니다.

    입력값:
        hash_table = [[] for _ in range(10)]
        
        insert_hash(hash_table, 10, 'A')  
        insert_hash(hash_table, 15, 'B')  
        insert_hash(hash_table, 17, 'C')  
        insert_hash(hash_table, 20, 'D')  
        insert_hash(hash_table, 25, 'E')  

        print(hash_table)

    출력값:
        [['A', 'D'], [], [], [], [], ['B', 'E'], [], ['C'], [], []]

"""

def insert_hash(hash_table, key, value):
    hash_table[key % len(hash_table)].extend(value)
