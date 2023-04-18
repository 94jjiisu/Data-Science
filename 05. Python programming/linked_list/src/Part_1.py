"""
Bare Minimum Requirements

요구사항
    큐, 스택을 구현해주세요.
    각 메소드에 작성되어있는 문제를 확인하여 코드를 작성해주세요.

    단 collections 라이브러리는 사용하지 마세요.
    메소드 이름은 변경하지 마세요.
    메소드의 매개변수를 추가하거나 삭제하지 마세요.
"""
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        


class Queue():

    def __init__(self):
        """
        # 문제 1.
        Queue의 생성자 함수를 구현해주세요.
        구현하시려는 로직에 맞게 해당 함수를 구현해주세요.
        아래 pass를 지워주시고 코드를 작성해주시면 됩니다. 
        """
        self.front = None
        self.rear = None
    

    def enqueue(self,item):
        """
        #. 문제 2.
        queue에 item 매개변수에 들어온 값을 집어넣는 메소드를 구현해주세요.

        input: item
            queue로 들어갈 값입니다.
        output: 
            반환값은 없습니다.
        아래 pass를 지워주시고 코드를 작성해주시면 됩니다. 
        """
        new_node = LinkedListNode(item)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        #return new_node.data



    def dequeue(self):
        """
        #. 문제 3.
        queue 동작에 알맞게 값을 queue에서 삭제하는 메소드를 구현해주세요.

        input: 
            input은 없습니다.
        output: 
            queue동작에 맞게 queue에서 삭제된 값을 반환해주세요.
            만약 삭제한 값이 없다면 None을 반환해주세요.
        아래 pass를 지워주시고 코드를 작성해주시면 됩니다. 
        """
        if self.front is not None:
            old_front = self.front
            self.front = old_front.next
            return old_front.data
            
        if self.front is None:
            self.rear = None            
            return None


    def return_queue(self):
        """
        #. 문제 4.
        queue내부에 있는 값을 반환하는 메소드를 구현해주세요.

        input: 
            input은 없습니다.
        output: 
            queue내부에 있는 값을 리스트 형태로 반환해주세요.
        아래 pass를 지워주시고 코드를 작성해주시면 됩니다. 
        """
        queue = []
        node = self.front
        while node:
            queue.append(node.data)
            node = node.next
        return queue


class Stack():
    def __init__(self):
        """
        # 문제 5.
        Stack의 생성자 함수를 구현해주세요.
        구현하시려는 로직에 맞게 해당 함수를 구현해주세요.
        아래 pass를 지워주시고 코드를 작성해주시면 됩니다. 
        """
        #self.data = []

        self.top = None


    def push(self, item):
        """
        #. 문제 6.
        Stack에 item 매개변수에 들어온 값을 집어넣는 메소드를 구현해주세요.

        input: item
            Stack로 들어갈 값입니다.
        output: 
            반환값은 없습니다.
        아래 pass를 지워주시고 코드를 작성해주시면 됩니다. 
        """
        #self.data.append(item)
        new_node = LinkedListNode(item)
        new_node.next = self.top
        self.top = new_node
        #return new_node.data


    def pop(self):
        """
        #. 문제 7.
        Stack 동작에 알맞게 값을 Stack에서 삭제하는 메소드를 구현해주세요.

        input: 
            input은 없습니다.
        output: 
            Stack동작에 맞게 Stack에서 삭제된 값을 반환해주세요.
            만약 삭제한 값이 없다면 None을 반환해주세요.
        아래 pass를 지워주시고 코드를 작성해주시면 됩니다. 
        """
        # if len(self.data) > 0:
        #     return self.data.pop()
        # return None
        if self.top is not None:
            popped_node = self.top
            self.top = popped_node.next
            return popped_node.data
        else:
            return None


    def return_stack(self):
        """
        #. 문제 8.
        Stack내부에 있는 값을 반환하는 메소드를 구현해주세요.

        input: 
            input은 없습니다.
        output: 
            Stack내부에 있는 값을 리스트 형태로 반환해주세요.
        아래 pass를 지워주시고 코드를 작성해주시면 됩니다. 
        """
        stack = []
        node = self.top
        while node:
            stack.append(node.data)
            node = node.next
        return list(reversed(stack))

    
