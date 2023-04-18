import pytest

@pytest.fixture(autouse=True)
def test_part2_import():
    try:
        from src.Part_2 import search_shortest_route
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')

def test_part2_adj_list1():
    from src.Part_2 import search_shortest_route

    connection_info = {
        'A': ['B', 'C'],
        'B': ['C', 'D'],
        'C': ['D'],
        'D': ['C'],
        'E': ['F'],
        'F': ['C']
    }
    
    assert search_shortest_route(connection_info, 'B', 'D') == ['B', 'D'], '정확한 경로를 찾아야합니다.'


def test_part2_adj_list2():
    from src.Part_2 import search_shortest_route

    connection_info = {
        'A': ['B', 'C', 'D'],
        'B': ['C', 'E'],
        'C': ['D', 'F'],
        'D': ['C', 'E'],
        'E': ['F'],
        'F': ['C']
    }
    
    assert search_shortest_route(connection_info, 'B', 'D') == ['B','C','D'], '정확한 경로를 찾아야합니다.'