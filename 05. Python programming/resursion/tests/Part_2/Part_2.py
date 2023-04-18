import pytest

@pytest.fixture(autouse=True)
def test_part2_import():
    try:
        from src.Part_2 import node, binary_search_tree
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')

@pytest.mark.timeout(10)
def test_part2_working_normally():
    from src.Part_2 import node, binary_search_tree

    head = node(16)  # 루트노드지정
    bt = binary_search_tree(head)
    
    bt.insert_node(12)
    bt.insert_node(19)
    bt.insert_node(11)
    bt.insert_node(13)
    bt.insert_node(18)
    bt.insert_node(20)
    bt.insert_node(9)
    bt.insert_node(8)
    bt.insert_node(10)

    assert bt.search_node(5) == False
    assert bt.search_node(-2) == False
    assert bt.search_node(18) == True


@pytest.mark.timeout(10)
def test_part2_class_methods():
    from src.Part_2 import node, binary_search_tree

    head = node(16)  # 루트노드지정
    bt = binary_search_tree(head)
    
    bt.insert_node(12)
    bt.insert_node(19)
    bt.insert_node(11)
    bt.insert_node(13)
    bt.insert_node(18)
    bt.insert_node(20)
    bt.insert_node(9)
    bt.insert_node(8)
    bt.insert_node(10)

    assert bt.search_node(5) == False, "먼저 정상적으로 작동해야합니다."
    
    assert 'search_node' in dir(binary_search_tree), "binary_search_tree 클래스 내부에 search_node 메소드가 있어야합니다"
    assert 'insert_node' in dir(binary_search_tree), "binary_search_tree 클래스 내부에 insert_node 메소드가 있어야합니다"
