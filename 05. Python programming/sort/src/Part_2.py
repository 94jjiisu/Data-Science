"""
Bare Minimum Requirements
예외사항에 따라 어떻게 될지 결과를 예상해봅시다.

요구사항:
	중요한 조건은 재귀를 반드시 활용해야 합니다.
	마이너스값이 입력되었을 경우, 예외처리해주는 코드를 작성하세요.

	마이너스값을 입력해도 마이너스값도 정상수행되야 합니다.
	출력결과값에 대해서는 '입력받은 n부터 1씩 감소하며(또는 증가하며) 0까지 출력하면 됩니다.

	입출력값에 대한 별도 양식은 없으니 조건에 따른 구현만 하시면 됩니다.
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
def print_to_zero_pos(n, result_list):
	"""
	# 문제 1.
		1 이상의 양수를 입력받아 입력받은 수부터 0까지 구하는 함수를 작성해주세요.
		재귀함수를 꼭 사용해주셔야합니다.
		result_list안에 결과 값을 넣어주세요.
		(result_list를 어떻게 사용하는지는 아래 코드 사용 예제를 참고해주세요.)

		해당 코드 사용 예제
			pos = int(input("input : ")) # 5
			result_list = []
			print_to_zero_pos(pos, result_list)
			print(result_list) # [5,4,3,2,1,0]
	"""
	# if n < 0:
	# 	return result_list

	# if n == 0:
	# 	result_list.append(0)
	# 	print(result_list)
	# else:
	# 	return print_to_zero_pos(n-1, result_list + [n])
	if n < 0:
		return result_list
	
	result_list.append(n)
	return print_to_zero_pos(n-1, result_list)


@counter
def print_to_zero_neg(n, result_list):
	"""
	# 문제 2.
		-1 이하의 음수를 입력받아 입력받은 수부터 0까지 구하는 함수를 작성해주세요.
		재귀함수를 꼭 사용해주셔야합니다.
		result_list안에 결과 값을 넣어주세요.
		(result_list를 어떻게 사용하는지는 아래 코드 사용 예제를 참고해주세요.)

		해당 코드 사용 예제
			neg = int(input("input : ")) # -3
			result_list_neg = []
			print_to_zero_neg(neg, result_list_neg)
			print(result_list_neg) #[-3,-2,-1,0]
	"""
	# if n > 0:
	# 	return result_list

	# if n == 0:
	# 	result_list.append(0)
	# 	print(result_list)
	# else:
	# 	return print_to_zero_pos(n+1, result_list + [n])
	if n > 0:
		return result_list
	
	result_list.append(n)
	return print_to_zero_neg(n+1, result_list)