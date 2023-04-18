"""
Advanced Requirements
조금 더 복잡한 코드를 구현하고 시간복잡도를 알아봅시다.
"""
"""
문제 1.
요구사항:
    이진 탐색이 무엇인지 구글링을 통해 공부해주세요.
    (지금 당장 공부하지 못했다고 너무 걱정하지 않으셔도 됩니다. n523에서 다시 한 번 공부합니다!)

    아래는 위키백과에 있는 이진 탐색 알고리즘의 설명입니다.
    https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%A7%84_%EA%B2%80%EC%83%89_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

    이진 탐색에 대해서 공부가 끝났다면 이제 구현해볼 차례입니다. 
    입력받은 2차원 리스트(input_list)에서 찾고자 하는 값(value_to_search)을 찾아 그 위치를 반환해주세요.
    단 입력받은 2차원 리스트의 모든 리스트 내부는 정렬되어있습니다. 

    input:
        input_list: 정렬된 요소들로 구성된 2차원 리스트 
            (2차원 리스트? https://dojang.io/mod/page/view.php?id=2291)
        value_to_search: 찾고자 하는 값
    
    output:
        튜플들의 리스트 
            튜플:(i번째 리스트, j번째 요소)
    
    예시: 
        input
            input_list = [
                [1,2,3,4,5,6,7,8],
                [1,2,3,4,5,6,7,8,9,10],
                [1,2,4,8,16,32],
                [1,2,3,4,5,6]
            ]
            value_to_search = 8
        
        output
            [(0,7), (1,7), (2,3)]

"""

def part3(input_list, value_to_search):
    
    output = []
    list_num = 0

    for i in input_list:
        start = 0
        end = len(i) - 1
        while start <= end:
            mid = (start + end) // 2
            if i[mid] == value_to_search:
                output.append((list_num, mid))
                break
            elif i[mid] < value_to_search:
                start = mid + 1
            else:
                end = mid - 1
        list_num += 1
    return output


"""
문제 2.
    위에서 작성한 코드의 시간 복잡도를 작성해주세요.
    만약 정답이 아니라면 작성하신 코드에서 더 효율적으로 작성할 수 있는지 확인해주세요.
"""

ANSWER = 'wrong answer'
CONSTANT = 'O(1)'
LOGARITHMIC = 'O(logn)'
LINEAR = 'O(n)'
LINEARITHMIC = 'O(nlogn)'
QUADRATIC = 'O(n^2)'
EXPONENTIAL = 'O(c^n)' 


def part3_timecomplexity():
    time_complexity = LINEARITHMIC
    reason = " 2로 계속 나누기 때문에 최종 mid 까지 logn 번 작업을 리스트 원소 개수인 n번 실행하기 때문"

    return (time_complexity, reason)
    