"""
Bare Minimum Requirements
Greedy를 활용하면서 알고리즘의 흐름을 이해해보자.

요구사항:
    Greedy의 개념과 과정은 단순하지만 결과에 따라 설계에 많은 영향을 줍니다.

    특정값을 출력하는 상황을 고려해봅시다.

    문제설명 : 초기방향은 물건 값을 입력하면 '잔돈갯수' 만을 출력하도록 설계되었다.

    따라서, 받은 잔돈의 종류와 종류별 잔돈갯수를 출력하기 위해 코드를 작성해봅시다
    아래 예시입력값과 출력값을 참조하며 문제를 해결해봅니다.

    입력값:
    100
    출력값:
    {700: 1, 100: 2}
"""

def changes(price):
    change = 1000 - price
    coin_list = [700, 400, 300, 100, 50, 10]

    sol = {}

    for coin in coin_list:
        while change >= coin:
            if change - coin >= 0:
                sol.setdefault(coin, 0)
                sol[coin] += 1
                change -= coin
    return sol