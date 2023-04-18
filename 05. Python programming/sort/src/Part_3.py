"""
Advanced Requirements
하나의 상황을 해결하면 이어서 추가적인 상황이 발생할 수 있습니다.

요구사항:
    Part 2에 이어 추가적인 상황을 해결해주세요.
    2개의 숫자(양수와 음수 모두 가능)가 입력되었을 경우, 처리해주는 코드를 추가로 작성하세요.

    입력받은 문자가 양수인지 음수인지 판별을 먼저 진행해야 합니다.

   
    재귀함수를 꼭 사용해주셔야합니다.
		result_list안에 결과 값을 넣어주세요.
		(result_list를 어떻게 사용하는지는 아래 코드 사용 예제를 참고해주세요.)

		해당 코드 사용 예제
			res = {}
            print_to_zero_pos_neg('-10,10,5,-5', res)
            import pprint
            pprint.pprint(res)

        위 코드 예상 입출력값
            입력값:
                -10,10,5,-5
            출력값:
                {'-10': ['-10', '-9', '-8', '-7', '-6', '-5', '-4', '-3', '-2', '-1', '0'],
                '-5': ['-5', '-4', '-3', '-2', '-1', '0'],
                '10': ['10', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0'],
                '5': ['5', '4', '3', '2', '1', '0']}
        
    단 Part_2 코드를 import하여 해결하지 마세요.
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


@counter 
def print_to_zero_pos_neg(nums, dir):
    nums = nums.split(',')
    if len(nums) == 1:
        if int(nums[0]) > 0:
            dir[nums[0]] = [str(i) for i in range(int(nums[0]), -1, -1)]
        else:
            dir[nums[0]] = [str(i) for i in range(int(nums[0]), 1)]
        return dir

    else:
        if int(nums[0]) > 0:
            dir[nums[0]] = [str(i) for i in range(int(nums[0]), -1, -1)]
        else:
            dir[nums[0]] = [str(i) for i in range(int(nums[0]), 1)]
        return print_to_zero_pos_neg(','.join(nums[1:]), dir)
