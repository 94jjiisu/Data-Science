import pytest

@pytest.fixture(autouse=True)
def test_part3_import():
    try:
        from src.Part_3 import recursion_advanced
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')

def test_part3_working_normally():
    from src.Part_3 import recursion_advanced

    test_sentence = 'testing...'
    assert (recursion_advanced(test_sentence) == '...gnitset')

    test_sentence = 'Codestates'
    assert (recursion_advanced(test_sentence) == 'setatsedoC')
    
    test_sentence = 'Recursion'
    assert (recursion_advanced(test_sentence) == 'noisruceR')

def test_part3_is_recursion():
    from src.Part_3 import recursion_advanced

    print(recursion_advanced.cnt)
    assert recursion_advanced.cnt >= 29, '재귀함수로 문제를 해결해야합니다.'
