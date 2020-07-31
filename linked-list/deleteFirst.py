class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        if self.head is None:
            print("linked list is empty")
            return

        else:
            currentNode = self.head
            while True:
                if currentNode is None:
                    break
                print(currentNode.data)
                currentNode = currentNode.next

    def deleteFirst(self):
        if self.head is None:
            print('list is empty. nothing to delete')
        else:
            currentNode = self.head
            currentNode.next = secondNode
            self.head = secondNode

firstNode = Node(1)
secondNode = Node(2)
linkedList = LinkedList()
linkedList.insert(firstNode)
linkedList.insert(secondNode)
linkedList.printList()
print('list after removing first element : ')
linkedList.deleteFirst()
linkedList.printList()
