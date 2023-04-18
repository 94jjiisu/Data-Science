"""
Advanced Requirements
대표적으로 활용할 수 있는 순회를 구현합니다.

요구사항:
    노드가 움직일 수 있는 경로는 다양합니다.
    순회라는 개념또한 일반적으로 많이 쓰이는 용어이지만 컴퓨터는 순회를 직관적으로 받아들이지 못합니다.
    컴퓨터가 받아들일 수 있는 순회를 구현합니다.

    중위순회를 구현하도록 합니다.
    강의노트에서 배웠던 재귀를 활용하지 않고 주어진 클래스와 함수 내에 구현을 완료하도록 합니다.

    트리를 따로 구현하지 않으셔도 됩니다.
    트리를 구성하는 노드의 형태는 다음과 같습니다
        class node:
            def __init__(self, data):
                self.data = data
                self.left = None
                self.right = None
"""

def in_order_traversal(root_node):
    seq = []
    if root_node.left:
        seq = seq + in_order_traversal(root_node.left)
    seq = seq + [root_node.data]
    if root_node.right:
        seq = seq + in_order_traversal(root_node.right)
    return seq
