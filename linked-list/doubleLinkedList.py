class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
            newNode.prev = self.head
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
            newNode.prev = lastNode

    def print_forward(self):
        if self.head is None:
            print('list is empty')
        else:
            currentNode = self.head
            while True:
                if currentNode is None:
                    break
                print(currentNode.data)
                currentNode = currentNode.next

    def print_backward(self):
        if self.head is None:
            print('list is empty')
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            while True:
                if lastNode == self.head:
                    print(lastNode.data)
                    break
                print(lastNode.data)
                lastNode = lastNode.prev

node1 = Node(90)
node2 = Node(91)
node3 = Node(92)
node4 = Node(93)
linkedList = LinkedList()
linkedList.insert(node1)
linkedList.insert(node2)
linkedList.insert(node3)
linkedList.print_forward()
print('----------')
linkedList.print_backward()
