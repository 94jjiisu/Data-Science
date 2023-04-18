from random import *
import pytest

@pytest.fixture(autouse=True)
def test_part2_import():
    try:
        from src.Part_2 import changes
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


@pytest.mark.timeout(10)
def test_part2_changes():
    from src.Part_2 import changes

    assert changes(100) == {700: 1, 100: 2}, "정확한 잔돈을 딕셔너리 형태로 반환해야합니다."
    assert changes(400) == {400: 1, 100: 2}, "정확한 잔돈을 딕셔너리 형태로 반환해야합니다."
    assert changes(600) == {400: 1}, "정확한 잔돈을 딕셔너리 형태로 반환해야합니다."
    assert changes(40) == {700: 1, 100: 2, 50: 1, 10: 1}, "정확한 잔돈을 딕셔너리 형태로 반환해야합니다."


@pytest.mark.timeout(10)
def test_part2_changes_random():
    from src.Part_2 import changes

    for _ in range(0,5):
        coin = randint(1, 10) * 10
        res = changes(coin)
        coin_sum = coin
        for i in res:
            coin_sum += (i * res[i])
        assert coin_sum == 1000
        
