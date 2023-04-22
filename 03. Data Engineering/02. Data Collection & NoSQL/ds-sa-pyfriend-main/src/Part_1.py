"""
문제 목록

1. 파이썬 True 와 False
2. 파이썬 문자열
3. 파이썬 리스트
4. 파이썬 딕셔너리

- "빈칸을 채워주세요" 는 지우고 테스트가 통과할 수 있도록 알맞은 코드를 입력해야 합니다.
"""

from unittest import TestCase

"""
1. 파이썬 True 와 False
"""


class PythonBooleans(TestCase):
    """
    파이썬에서 불리안 (boolean) 은 True 와 False 만 존재하는 것이 아닙니다.

    if 5 < 3:
        print('참입니다')
    else:
        print('참이 아닙니다')

    위 코드에서 if 조건문에서는 5 가 3 보다 작은 경우 '참입니다', 아닌 경우에는
    '참이 아닙니다' 라는 문구가 출력이 됩니다.

    그렇다면 어느 경우에 '참입니다' 혹은 '참이 아닙니다' 를 더 출력할 수 있을까요?

    제일 먼저 파이썬의 불리안에 대해서 알아보겠습니다.

    또한 여기에서 사용되는 비교 연산자는 '==' 이 아닌 'is' 를 사용합니다.
    이 둘의 차이가 뭘까요?
    
    if 에 '5 < 3' 말고도 어떤 값들이 어떤 결과를 보여주는지 하나씩 확인하면서
    진행해주세요!
    """
    def truth_function(self, condition):
        """
        해당 함수는 파라미터로 받는 'condition' 의 값이 truthy 하면 True 를,
        아닌 경우에는 False 를 리턴합니다.

        파라미터:
            - condition: truthy 여부를 확인할 값

        예를 들어 'condition' 이 42 가 주어진다면 True 를 리턴합니다.


        Hint:
        파이썬의 'bool' 함수를 활용해서 확인할 수 있습니다. 
            - bool(42) => True
        """
        if condition:
            return True
        else:
            return False

    def test_about_true(self):
        """
        가장 기본적으로 True 를 먼저 두고 연습하겠습니다.
        """
        assert True is self.truth_function(True)

    def test_about_false(self):
        assert False is self.truth_function(False)

    def test_about_none(self):
        """
        파이썬에서 None 은 어떤 값인가요?
        """
        assert False is self.truth_function(None)

    def test_about_zero(self):
        assert False is self.truth_function(0)

    def test_about_empty_collections(self):
        """
        명시적인 값들뿐만 아니라 컬렉션 자료형 등
        불리안으로 표시할 수 있습니다!
        """
        assert False is self.truth_function([])
        assert False is self.truth_function(())
        assert False is self.truth_function({})
        assert False is self.truth_function(set())

    def test_about_blank_strings(self):
        assert False is self.truth_function("")

    def test_about_others(self):
        """
        이번에는 애매한 상황들이 주어집니다.

        띄어쓰기 하나만 있는 문자열도 참일까요?

        이외에도 궁금하신 것들을 실험해보세요!
        """
        assert True is self.truth_function(1)
        assert True is self.truth_function([0])
        assert True is self.truth_function((0,))
        assert True is self.truth_function("파이썬도 뱀인가")
        assert True is self.truth_function(' ')
        assert True is self.truth_function('0')


"""
2. 파이썬 문자열
"""


class PythonStrings(TestCase):
    """
    이번에는 문자열에 대해서 알아보겠습니다.

    파이썬에서 문자열을 어떻게 사용하고 계신가요?

    한 줄로 작성되는 문자열부터 여러 줄로 나뉘어서 사용하는 문자열까지
    여러 형태의 문자열을 실험해 보세요!
    """

    def test_about_double_quoted_strings(self):
        """
        `isinstance` 라는 함수는 어떻게 사용이 되고 인스턴스(instance) 란
        무엇일까요?
        """
        string = "Hello world!"
        assert True is isinstance(string, str)

    def test_about_single_quoted_strings(self):
        """
        파이썬에서는 ' 와 " 를 둘 다 사용할 수 있습니다
        """
        string = 'Hello world!'
        assert True is isinstance(string, str)

    def test_about_triple_quote_strings(self):
        """
        지금 주석에서도 보실 수 있듯이 \""" 는 어떤 의미를 가질까요?
        """
        string = """Hello world!"""
        assert True is isinstance(string, str)

    def test_about_triple_single_quotes(self):
        string = '''Hello world!'''
        assert True is isinstance(string, str)

    def test_about_raw_strings(self):
        """
        파이썬에서 문자열 앞에 'r' 이 붙게 되면 무슨 뜻일까요?

        일반 문자열과 어떤 차이를 지녔는지 알아보세요
        """
        string = r"Hello world!"
        assert True is isinstance(string, str)

    def test_about_single_and_double_quotes_1(self):
        string = 'Hello, "world!"'
        assert 'Hello, "world!"' == string

    def test_about_single_and_double_quotes_2(self):
        string = "Don't"
        assert "Don't" == string

    def test_about_backslashes_1(self):
        """
        조금 섞어서 사용된 문자열을 읽는 연습을 해보겠습니다.
        """
        a = "\"Don't\""
        b = '"Don\'t"'
        assert True is (a == b)

    def test_about_backslashes_2(self):
        """
        아래 문자열의 길이를 파악해보세요.

        처음에 생각했던 길이와 맞나요?
        """
        string = "Batman,\n\Gotham"
        assert 15 == len(string)

    def test_about_triple_quoted_strings_1(self):
        """
        아래 문자열은 길이가 어떨까요?
        
        처음에 생각했던 길이와 맞나요?
        """
        string = """
Hello,
world!
"""
        assert 15 == len(string)

    def test_about_triple_quoted_strings_2(self):
        """
        아래 두 문자열은 과연 같을까요?

        비교를 해보시고 두 문자열이 같으면 True, 아니면 False 를 넣어주세요
        """
        a = "Hello \"world\"."
        b = """Hello "world"."""
        assert True is (a == b)

    def test_about_string_concatenation_1(self):
        string = "Hello, " + "world"
        assert "Hello, world" == string

    def test_about_string_concatenation_2(self):
        """
        아래 문자열은 에러가 날까요?

        파이썬의 문자열 concatenation 에 대해서 더 보겠습니다
        """
        string = "Hello" ", " "world"
        assert "Hello, world" == string

    def test_about_plus_signs_1(self):
        hi = "Hello, "
        there = "world"
        hi += there
        assert "Hello, world" == hi

    def test_about_plus_signs_2(self):
        original = "Hello, "
        hi = original
        there = "world"
        hi += there
        assert "Hello, " == original

    def test_about_escape_characters(self):
        """
        다음 코드에서 `string` 을 표현할 수 있는 두 가지 방법을 생각해보세요!

        어떻게 하면 "\n" 과 같은 문자열을 다르게 나타낼 수 있을까요?

        마지막으로 `string` 의 길이를 확인해봅니다.
        이와 같은 다른 특수문자들도 한번 확인해보세요!
        """
        string = "\n"
        assert '\n' == string
        assert "\n" == string
        assert 1 == len(string)


"""
3. 파이썬 리스트
"""


class PythonLists(TestCase):
    """
    파이썬에서 list 는 어떻게 활용할 수 있을까요?

    이번에는 파이썬에서의 리스트에 대해서 살펴보겠습니다.
    """
    def test_about_list_creation(self):
        """
        제일 먼저 리스트는 어떤 데이터 타입인지 길이는 어떻게 되는지
        보겠습니다.

        리스트의 타입을 확인하면 나오는 문자열을 이용해 통과해보세요!
        """
        empty_list = list()
        assert "<class 'list'>" == str(type(empty_list))
        assert 0 == len(empty_list)

    def test_about_list_literals(self):
        """
        파이썬에서 리스트에 항목을 추가하는 방법은 어떤가요?

        `append` 메소드를 사용해서도 추가할 수 있지만
        이외에 어떤 방법을 추가할 수 있는지 알아봅니다.
        """
        nums = list()
        assert [] == nums

        nums[0:] = [1]
        assert [1] == nums

        nums[1:] = [2]
        assert [1, 2] == nums

        nums.append(333)
        assert [1, 2, 333] == nums

    def test_about_list_elements(self):
        """
        파이썬의 리스트의 인덱스는 어떤지 확인해 봅니다.

        뒤에서부터 접근할 수 있는 인덱스를 잘 활용하면 매우 편리해질 수도
        있습니다.

        각 항목이 어떤 단어를 가리키는지 파악하실 수 있나요?
        """
        story = ['once', 'upon', 'a', 'time']

        assert "once" == story[0]
        assert "time" == story[3]
        assert "time" == story[-1]
        assert "upon" == story[-3]

    def test_about_slicing_lists_1(self):
        """
        리스트를 자르는 것을 흔히 slicing 이라고 합니다.

        파이썬에서는 슬라이싱을 어떻게 할 수 있고 리스트의 범위를 벗어나는
        경우들에는 어떻게 해야 할까요?
        """
        story = ['once', 'upon', 'a', 'time']

        assert ['once'] == story[0:1]
        assert ['once', 'upon'] == story[0:2]
        assert [] == story[2:2]
        assert ['a', 'time'] == story[2:20]
        assert [] == story[4:0]
        assert [] == story[4:100]
        assert [] == story[5:0]

    def test_about_slicing_lists_2(self):
        story = ['once', 'upon', 'a', 'time']

        assert ['a', 'time'] == story[2:]
        assert ['once', 'upon'] == story[:2]

    def test_about_list_and_ranges_1(self):
        """
        range 는 어떻게 사용할 수 있나요?
        리스트와는 어떻게 활용할 수 있는지 살펴보겠습니다.

        `range(1, 6)` 를 그냥 사용하게 되면 `[1, 2, 3, 4, 5]` 가 될까요?

        range 를 활용해 리스트를 만들었을 때 어떤 항목들이 들어가나요?
        """
        assert range == type(range(5))
        assert False is ([1, 2, 3, 4, 5] == range(1, 6))
        assert [0, 1, 2, 3, 4] == list(range(5))
        assert [5, 6, 7, 8] == list(range(5, 9))

    def test_about_list_and_ranges_2(self):
        """
        range 에 대해서 더 알아봅니다.

        다음 코드들에서 생성된 리스트를 만들어보세요!

        예를 들어 `list(range(6, 2, -3))` 은 어떤 결과를 보여주나요?
        """
        assert [5, 4] == list(range(5, 3, -1))
        assert [0, 2, 4, 6] == list(range(0, 8, 2))
        assert [1, 4, 7] == list(range(1, 8, 3))
        assert [5, 1, -3] == list(range(5, -7, -4))
        assert [5, 1, -3, -7] == list(range(5, -8, -4))

    def test_about_insert(self):
        """
        리스트에 항목을 추가할 때에는 어떻게 하는지 알아보겠습니다.

        insert 와 append 의 차이점은 무엇인지 살펴봅니다.
        """
        gandalf=['you', 'shall', 'pass']
        gandalf.insert(2, 'not')
        assert ['you', 'shall', 'not', 'pass'] == gandalf

        gandalf.insert(0, 'Hey')
        assert ['Hey', 'you', 'shall', 'not', 'pass'] == gandalf

    def test_about_pop(self):
        """
        리스트에 다른 메소드에 대해서 알아보겠습니다.

        pop 및 다른 메소드들에 대해서 알아봅니다.
        """
        stack=[10, 20, 30, 40]
        stack.append('last')

        assert [10, 20, 30, 40, 'last'] == stack

        popped_value=stack.pop()
        assert 'last' == popped_value
        assert [10, 20, 30, 40] == stack

        popped_value=stack.pop(1)
        assert 20 == popped_value
        assert [10, 30, 40] == stack


"""
4. 파이썬 딕셔너리
"""


class PythonDictionaries(TestCase):
    """
    이번에는 파이썬 딕셔너리에 대해서 알아봅니다.

    파이썬의 딕셔너리는 리스트와는 다르게 작동합니다.
    그렇다면 키-값 쌍으로 동작하는 딕셔너리에 대해서 알아보겠습니다.
    """
    def test_about_dictionary_creation(self):
        """
        파이썬 딕셔너리 생성에 대해서 알아보겠습니다.

        딕셔너리는 어떻게 생성할 수 있을까요?
        딕셔너리의 타입은 뭔가요?
        """
        empty_dict=dict()
        assert "<class 'dict'>" == str(type(empty_dict))
        assert {} == empty_dict
        assert 0 == len(empty_dict)

    def test_about_dictionary_literals(self):
        empty_dict={}
        assert type({}) == type(empty_dict)

        cities={'france': 'paris', 'korea': 'seoul'}
        assert 2 == len(cities)

    def test_about_accessing_dictionaries(self):
        """
        딕셔너리에서 원하는 값에 접근하는 방법에 대해서 알아보겠습니다.
        
        아래와 같이 접근하게 되면 어떤 값들을 확인할 수 있을까요?
        """
        cities={'france': 'paris', 'korea': 'seoul'}
        assert "paris" == cities['france']
        assert "seoul" == cities['korea']

    def test_about_changing_dictionaries(self):
        """
        딕셔너리에 저장된 값들은 불변이 아닙니다.

        그렇다면 어떻게 딕셔너리에 저장된 값들을 변경할 수 있는지
        살펴보겠습니다.
        """
        cities={'france': 'paris', 'korea': 'seoul'}
        cities['france'] = 'lyon'

        expected = {'korea': 'seoul', 'france': "lyon"}
        assert expected == cities

    def test_about_dictionary_order(self):
        """
        딕셔너리는 분명 리스트와 다릅니다.
        
        순서대로 인덱스가 존재하는 것도 아니고 키-값으로 이루어진 형태입니다.

        그렇다면 딕셔너리들을 비교할 때 키-값들이 순서로 들어가야 할까요?
        """
        dict1={'france': 'paris', 'korea': 'seoul'}
        dict2={'korea': 'seoul', 'france': 'paris'}

        assert True is (dict1 == dict2)

    def test_about_keys_and_values(self):
        """
        이번에는 파이썬 딕셔너리의 메소드들에 대해서도 알아보겠습니다.

        `keys()` 나 `values()` 등을 사용하면 더 잘 활용할 수 있습니다.

        다른 메소드들은 어떤 것들이 있을까요?
        """
        cities={'france': 'paris', 'korea': 'seoul'}
        assert 2 == len(cities.keys())
        assert 2 == len(cities.values())
        assert True is ('france' in cities.keys())
        assert True is ('paris' in cities.values())
        assert False is ('seoul' in cities.keys())
        assert False is ('korea' in cities.values())
