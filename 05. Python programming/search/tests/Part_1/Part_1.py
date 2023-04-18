import pytest

@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from src.Part_1 import dfs_recur, bfs_queue

    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_dfs_recur1():
    from src.Part_1 import dfs_recur, bfs_queue

    dfs_graph = {
        1: [2,3,4],
        2: [5],
        3: [6],
        4: [],
        5: [7],
        6: [5],
        7: [6],
    }
    assert dfs_recur(2, dfs_graph, dfs_list=[]) == [2, 5, 7, 6], "그래프의 dfs를 구현해야합니다."

def test_dfs_recur2():
    from src.Part_1 import dfs_recur, bfs_queue

    dfs_graph = {
        1: [5],
        2: [1,4],
        3: [5],
        4: [5],
        5: [3]
    }
    assert dfs_recur(2, dfs_graph, dfs_list=[]) == [2, 1, 5, 3, 4], "그래프의 dfs를 구현해야합니다."

def test_bfs_queue1():
    from src.Part_1 import dfs_recur, bfs_queue

    bfs_graph = { 
        1: [2,3,4],
        2: [5],
        3: [6],
        4: [],
        5: [7],
        6: [5],
        7: [6],
    }
    assert bfs_queue(2, bfs_graph) == [2, 5, 7, 6], "그래프의 bfs를 구현해야합니다."

def test_bfs_queue2():
    from src.Part_1 import dfs_recur, bfs_queue
    
    bfs_graph = {
        1: [5],
        2: [1,4],
        3: [5],
        4: [5],
        5: [3]
    }
    assert bfs_queue(2, bfs_graph) == [2, 1, 4, 5, 3], "그래프의 bfs를 구현해야합니다."