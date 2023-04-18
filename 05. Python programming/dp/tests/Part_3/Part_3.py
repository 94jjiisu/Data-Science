import pytest

@pytest.fixture(autouse=True)
def test_part3_import():
    try:
        from src.Part_3 import word_logic, number_logic
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')

        
def test_part3_number_logic():
    from src.Part_3 import word_logic, number_logic

    assert number_logic(0) == 'Zero.', "매개변수로 들어간 숫자의 정확한 문자열을 반환해야합니다."
    assert number_logic(11) == 'Eleven.', "매개변수로 들어간 숫자의 정확한 문자열을 반환해야합니다."
    assert number_logic(12) == 'Twelve.', "매개변수로 들어간 숫자의 정확한 문자열을 반환해야합니다."
    assert number_logic(1043283) == 'One million, forty-three thousand, two hundred and eighty-three.', "매개변수로 들어간 숫자의 정확한 문자열을 반환해야합니다."
    assert number_logic(63235859) == 'Sixty-three million, two hundred and thirty-five thousand, eight hundred and fifty-nine.', "매개변수로 들어간 숫자의 정확한 문자열을 반환해야합니다."
