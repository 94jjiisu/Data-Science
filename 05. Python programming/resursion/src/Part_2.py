"""
Bare Minimum Requirements
    연결리스트의 참조개념을 생각해보면서 트리개념에 접근해봅니다.

요구사항:
    추상화된 트리는 제공된 그림처럼 설명되지만 
    실제 컴퓨터 내부에서는 다르게 동작된다는 것을 인지하셔야 합니다.
    코딩을 하며 노드를 검색하고 추가하는 것을 넘어서서 
    트리구조로 동작하는 소프트웨어에 대해 생각해봅니다.

    트리의 모양은 'if __name__ == "__main__":' 아래 작성된 그림을 참조하세요.
    기능에 적합하도록 코드를 구현하시길 바랍니다.
    오늘 강의노트에서 학습한 트리 소스코드를 기준으로해야 코드를 작성해야 합니다.
    노드검색에 대한 결과가 동일하게 나올 수 있도록 완성하세요.
    'if __name__ == "__main__":' 구문 아래 코드와 출력값을 참조하며 문제를 해결해봅니다.
"""

class node:
    def __init__(self, value):
        """
        # 문제 1
        bst에서 사용할 수 있는 node 클래스를 작성해주세요
        """
        self.value = value
        self.left = None
        self.right = None


class binary_search_tree:
    def __init__(self, head):
        """
        문제 2.
        bst의 생성자 메소드를 작성해주세요
        """
        self.head = head


    def insert_node(self, value):
        """
        문제 3.
        bst의 동작에 맞게 값을 집어넣을 수 있도록 메소드를 작성해주세요
        """
        self.base_node = self.head
        while True:
            if value < self.base_node.value:
                if self.base_node.left != None:
                    self.base_node = self.base_node.left
                else:
                    self.base_node.left = node(value)
                    break
            else:
                if self.base_node.right != None:
                    self.base_node = self.base_node.right
                else:
                    self.base_node.right = node(value)
                    break


    def search_node(self, value):
        """
        문제 4.
        bst 내부에 value값이 있는지 True / False값을 반환하는 메소드를 작성해주세요
        """
        self.base_node = self.head

        while self.base_node:
            if self.base_node.value == value:
                return True
                break

            if self.base_node.value > value:
                if self.base_node.left != None:
                    self.base_node = self.base_node.left
                else:
                    return False

            if self.base_node.value < value:
                if self.base_node.right != None:
                    self.base_node = self.base_node.right
                else:
                    return False


if __name__ == "__main__":
    """
    아래 코드를 통해 문제의 예상 입출력을 한 번 확인해주세요.

    [아래 코드의 트리 형태]
                        16
                    /       \
                12              19
               /  \             /  \
            11      13         18   20
          /
        9
      /  \
    8     10
    """

    head = node(16)  
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

    print(bt.search_node(5))    #False
    print(bt.search_node(-2))   #False
    print(bt.search_node(18))   #True
