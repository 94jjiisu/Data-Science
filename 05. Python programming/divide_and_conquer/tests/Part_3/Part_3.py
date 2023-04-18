import pytest


@pytest.fixture(autouse=True)
def test_part3_import():
    try:
        from src.Part_3 import part3
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_part3_return_correct_answer1():
    from src.Part_3 import part3

    li =  [
        [0,0,1,1],
        [0,0,1,1],
        [1,1,1,1],
        [0,0,1,1]
    ]

    assert part3(li) == "(01(1100)1)"


def test_part3_return_correct_answer2():
    from src.Part_3 import part3

    li = [
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,1,1,0,0],
        [1,1,1,1,1,1,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,1,1],
        [1,1,1,1,0,0,1,1]
    ]

    assert part3(li) == "(1(0010)1(0001))"


def test_part3_return_correct_answer3():
    from src.Part_3 import part3

    li = [
        [0,0,1,1,0,0,0,0],
        [0,0,1,1,0,0,0,0],
        [1,1,1,1,1,1,0,0],
        [1,1,1,1,1,1,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [0,0,1,1,0,0,1,1],
        [0,0,1,1,0,0,1,0]
    ]

    assert part3(li) == "((0111)(0010)(1101)(000(1110)))"


def test_part3_return_correct_answer4():
    from src.Part_3 import part3

    li = [
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [0,0,0,1,1,1,0,0],
        [0,0,0,1,1,1,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,1,1],
        [1,1,1,1,0,0,1,1]
    ]

    assert part3(li) == "((110(0101))(0010)1(0001))"