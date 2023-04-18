"""
Advanced Requirements
재귀에 대한 개념과 내장함수의 내부로직을 이해한다.

요구사항:
    파이썬에서는 개발자 편의성을 위해 다양한 내장함수를 제공하고 있습니다.
    개발복잡도와 사이드이펙트로 인해 내장함수를 사용하지 못 하는 경우도 있습니다.
    내장함수는 간편한 기능이긴 하지만 문제가 확장되는 경우 
    예상되는 결과를 도출해주지 못 하는 경우도 있습니다.
    내장함수의 원리와 자신이 직접 구현해보는 기능의 적합성을 판단해봅니다.

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
def recursion_advanced(str):
    """
    # 문제
        재귀를 활용하여 주어진 문자를 뒤집어주는 프로그래밍을 진행합니다.
        문자열에 직접 영향을 주는 reverse와 같은 내장함수를 사용하면 안됩니다.

        # 예상 입출력 1
            input : 'testing...'
            output: '...gnitset'
        
        # 예상 입출력 2
            input : 'Codestates'
            output: 'setatsedoC'
    """
    if len(str) <= 1:
        return str[0]
    else:
        return str[-1] + recursion_advanced(str[:-1])
