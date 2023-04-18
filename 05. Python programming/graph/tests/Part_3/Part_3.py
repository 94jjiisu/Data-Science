import pytest

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

@pytest.fixture(autouse=True)
def test_part3_import():
    try:
        from src.Part_3 import in_order_traversal
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_part3_fst():
    from src.Part_3 import in_order_traversal

    root_node = node(30)
    root_node.left = node(12)
    root_node.right = node(13)
    root_node.left.left = node(11)
    root_node.left.right = node(15)
    root_node.right.right = node(19)
    root_node.right.right.left = node(16)
    root_node.right.right.right = node(20)
    
    assert in_order_traversal(root_node) == [11, 12, 15, 30, 13, 16, 19, 20], '트리에 대한 중위순회를 구현해야합니다.'


def test_part3_snd():
    from src.Part_3 import in_order_traversal

    root_node = node(10)
    root_node.left = node(11)
    root_node.right = node(15)
    root_node.left.left = node(16)
    root_node.left.right = node(19)
    root_node.right.right = node(30)
    root_node.right.right.left = node(9)
    root_node.right.right.right = node(17)
    
    assert in_order_traversal(root_node) == [16, 11, 19, 10, 15, 9, 30, 17], '트리에 대한 중위순회를 구현해야합니다.'