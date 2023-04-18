"""
Advanced Requirements
분할정복에 익숙해져봅시다.

요구사항:
    흑백으로 표현된 이미지를 압축하려합니다.
    흰 점을 나타내는 0과 검은 점을 나태내는 1로만 이루어진 이미지(2차원 리스트)에서 
    같은 숫자의 점들이 한 곳에서 많이 몰려있으면, 이를 압축하여 간단하게 표현할 수 있습니다.

    주어진 이미지가 모두 0으로만 되어있으면 압축 결과는 "0"이 되고, 
    모두 1로만 되어있으면 압축결과는 "1"이 됩니다. 
    
    만약 0과 1이 섞여있으면 전체를 한 번에 나타내지 못하고 
    왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래 이렇게 4개의 이미지로 나누어 압축하게 되며,
    이 4개의 이미지를 압축한 결과를 차례대로 괄호 안에서 묶어 표현합니다. 

    아래 입출력 예시를 확인하여 코드를 작성해주세요.

    입력 조건:
        N * N의 2차원 리스트가 입력으로 주어집니다. 
        단 N은 항상 2의 제곱수로 주어지며 1 <= N <= 64의 범위를 가집니다.

        2차원 리스트의 요소는 0또는 1의 숫자로만 구성되어 있습니다. 

    출력 조건:
        압축된 결과를 문자열로 반환해주세요.

    # 예시 1
        입력:
        [
            [0,0,1,1],
            [0,0,1,1],
            [1,1,1,1],
            [0,0,1,1]
        ]

        출력: "(01(1100)1)"

    # 예시 2
        입력: 
        [
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0],
            [0,0,0,1,1,1,0,0],
            [0,0,0,1,1,1,0,0],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,1,1],
            [1,1,1,1,0,0,1,1]
        ]

        출력: "((110(0101))(0010)1(0001))"

    # 예시 3
        입력:
        [
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]
        ]

        출력: "1"
"""

def part3(li):
    N = len(li)
    divide = len(li) // 2

    if sum(map(sum, li)) == N**2:
        return 1
    if sum(map(sum, li)) == 0:
        return 0
    
    quadrant_1 = part3([i[divide:N] for i in li[0:divide]])
    quadrant_2 = part3([i[divide:N] for i in li[divide:N]])
    quadrant_3 = part3([i[0:divide] for i in li[divide:N]])
    quadrant_4 = part3([i[0:divide] for i in li[0:divide]])

    return "({}{}{}{})".format(quadrant_4, quadrant_1, quadrant_3, quadrant_2)

    # quadrant_1 = part3(li[i][divide:N] for i in range(0, divide))
    # quadrant_2 = part3(li[i][divide:N] for i in range(divide, N))
    # quadrant_3 = part3(li[i][0:divide] for i in range(divide, N))
    # quadrant_4 = part3(li[i][0:divide] for i in range(0, divide))