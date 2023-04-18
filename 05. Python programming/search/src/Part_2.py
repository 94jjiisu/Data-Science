"""
Advanced Requirements
재귀와 DFS에 대해 복합적으로 이해합니다.

요구사항:
    DFS를 이해하면서 내부적으로 어떤 개념과 연결되서 구현되는지 생각해봅니다.
    추상도가 높을 수록 상황에 대한 이해 및 실생활과의 연결점을 찾을 수 있는 연습을 할 수 있습니다.

    문제를 해결하는 것이 목표로 두는 것뿐만 아니라, 문제를 보기 전에 테스트 코드를 보면서 
    스스로 문제를 만들고 해결해봅니다.

    해당 문제는 그래프의 DFS 개념을 재귀적으로 구현하기입니다.
    아래 예상 입출력을 보면서 패턴을 파악하고 소스코드를 어떻게 구현할지 로직을 생각해보세요.

    Case 1.
    입력
        char_combi('2')
    출력 
        ['q', 'w', 'e']

    Case 2.
    입력
        char_combi('24')
    출력 
        ['qz', 'qx', 'qc', 'wz', 'wx', 'wc', 'ez', 'ex', 'ec']
"""

from itertools import product

def char_combi(num):
    test_result = []
    test_dict = {"2": "qwe", "3": "asd", "4": "zxc"}
    
    items = []
    for i in list(num):
        items.append(list(test_dict[i]))
    
    for i in list(product(*items)):
        test_result.append(''.join(i))

    return test_result
