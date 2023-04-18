import pytest

@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from src.Part_1 import hash_table
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')

def test_part1_hash_put():
    from src.Part_1 import hash_table

    ht = hash_table()

    ht.hash_put('Kim', 1234)
    ht.hash_put('Johne', 5678)
    ht.hash_put('Smith', 1526)
    ht.hash_put('Michael', 3748)

    assert 1234 in ht.table, 'hash_put을 통해 table안에 값이 들어가야 합니다.'
    assert 5678 in ht.table, 'hash_put을 통해 table안에 값이 들어가야 합니다.'
    assert 1526 in ht.table, 'hash_put을 통해 table안에 값이 들어가야 합니다.'
    assert 3748 in ht.table, 'hash_put을 통해 table안에 값이 들어가야 합니다.'


def test_part1_hash_search():
    from src.Part_1 import hash_table

    ht = hash_table()

    ht.hash_put('Kim', 1234)
    ht.hash_put('Johne', 5678)
    ht.hash_put('Smith', 1526)
    ht.hash_put('Michael', 3748)

    assert ht.hash_search('Kim') is not None, 'hash_search를 통해 table안에 매칭되는 값을 찾아야합니다.'
    assert ht.hash_search('Johne') is not None, 'hash_search를 통해 table안에 매칭되는 값을 찾아야합니다.'
    assert ht.hash_search('Smith') is not None, 'hash_search를 통해 table안에 매칭되는 값을 찾아야합니다.'
    assert ht.hash_search('Michael') is not None, 'hash_search를 통해 table안에 매칭되는 값을 찾아야합니다.'
