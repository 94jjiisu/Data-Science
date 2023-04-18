import pytest

@pytest.fixture(autouse=True)
def test_part3_import():
    try:
        from src.Part_3 import part3
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_part3_return_correct_answer():
    from src.Part_3 import part3

    assert part3(20) == 8, "1부터 20까지의 숫자중 소수는 8개 입니다!"
    assert part3(100) == 25, "1부터 100까지의 숫자중 소수는 25개 입니다!"
    assert part3(1000) == 168, "1부터 100까지의 숫자중 소수는 168개 입니다!"


def test_part3_return_error_at_0():
    from src.Part_3 import part3
    try:
        part3(0)
    except ValueError as v:
        assert True

    except Exception as e:
        pytest.fail("0 이하의 숫자가 들어온 경우 ValueError를 발생시켜야합니다.")

    else:
        pytest.fail("0 이하의 숫자가 들어온 경우 ValueError를 발생시켜야합니다.")
    
    
def test_part3_return_error_at_neg():
    from src.Part_3 import part3
    try:
        part3(-1)
    except ValueError as v:
        assert True

    except Exception as e:
        pytest.fail("0 이하의 숫자가 들어온 경우 ValueError를 발생시켜야합니다.")

    else:
        pytest.fail("0 이하의 숫자가 들어온 경우 ValueError를 발생시켜야합니다.")