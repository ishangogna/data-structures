class Node():
    def __init__(self,data):
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
            print('Empty list')
            return
        else:
            currentNode = self.head
            while True:
                if currentNode is None:
                    break
                print(currentNode.data)
                currentNode = currentNode.next

    def deleteAtIndex(self, position):
        if self.head is None:
            print('list already empty')
        else:
            currentPosition = 0
            currentNode = self.head

            while True:
                if currentPosition == position:
                    currentNode.next = None
                    prevNode.next = currentNode.next

                prevNode = currentNode
                currentNode= currentNode.next
                currentPosition += 1




node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

linkedList = LinkedList()
linkedList.insert(node1)
linkedList.insert(node2)
linkedList.printList()
linkedList.deleteAtIndex(1)
linkedList.printList()
