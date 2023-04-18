import pytest

@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from src.Part_1 import search_route
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_part1_traversal1():
    from src.Part_1 import search_route

    connection_info = {
        'A': ['B', 'C'],
        'B': ['C', 'D'],
        'C': ['D'],
        'D': ['C'],
        'E': ['F'],
        'F': ['C']
    }

    assert search_route(connection_info, 'B', 'D') == ['B', 'C', 'D'], '정확한 경로를 찾아야합니다.'


def test_part1_traversal2():
    from src.Part_1 import search_route

    connection_info = {
        'A': ['B', 'C'],
        'B': ['C'],
        'C': ['E', 'F'],
        'D': ['C'],
        'E': ['F'],
        'F': ['C']
    }

    assert search_route(connection_info, 'B', 'D') == None, '경로가 없는 경우 None을 반환해야합니다.'

