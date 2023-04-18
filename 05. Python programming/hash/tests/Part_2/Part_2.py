import pytest

@pytest.fixture(autouse=True)
def test_part2_import():
    try:
        from src.Part_2 import insert_hash
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_part2_working_normally_10():
    from src.Part_2 import insert_hash

    hash_table = [[] for _ in range(10)]
    
    insert_hash(hash_table, 10, 'A')  
    assert hash_table == [['A'], [], [], [], [], [], [], [], [], []], "문제 예시처럼 작동해야합니다."

    insert_hash(hash_table, 15, 'B')  
    assert hash_table == [['A'], [], [], [], [], ['B'], [], [], [], []], "문제 예시처럼 작동해야합니다."

    insert_hash(hash_table, 17, 'C')  
    assert hash_table == [['A'], [], [], [], [], ['B'], [], ['C'], [], []], "문제 예시처럼 작동해야합니다."

    insert_hash(hash_table, 20, 'D')  
    assert hash_table == [['A', 'D'], [], [], [], [], ['B'], [], ['C'], [], []], "문제 예시처럼 작동해야합니다."

    insert_hash(hash_table, 25, 'E')  
    assert hash_table == [['A', 'D'], [], [], [], [], ['B', 'E'], [], ['C'], [], []], "문제 예시처럼 작동해야합니다."

def test_part2_working_normally_5():
    from src.Part_2 import insert_hash
    
    hash_table = [[] for _ in range(5)]
    
    insert_hash(hash_table, 10, 'A')  
    assert hash_table == [['A'], [], [], [], []], "길이가 다른 경우에도 정상적으로 작동해야합니다."

    insert_hash(hash_table, 15, 'B')  
    assert hash_table == [['A', 'B'], [], [], [], []], "길이가 다른 경우에도 정상적으로 작동해야합니다."

    insert_hash(hash_table, 17, 'C')  
    assert hash_table == [['A', 'B'], [], ['C'], [], []], "길이가 다른 경우에도 정상적으로 작동해야합니다."

    insert_hash(hash_table, 20, 'D')  
    assert hash_table == [['A', 'B', 'D'], [], ['C'], [], []], "길이가 다른 경우에도 정상적으로 작동해야합니다."

    insert_hash(hash_table, 25, 'E')  
    assert hash_table == [['A', 'B', 'D', 'E'], [], ['C'], [], []], "길이가 다른 경우에도 정상적으로 작동해야합니다."

