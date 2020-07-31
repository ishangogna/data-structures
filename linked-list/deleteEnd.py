class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, newNode):
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
            print('list is empty')
            return

        else:
            currentNode = self.head
            while True:
                if currentNode is None:
                    break
                print(currentNode.data)
                currentNode = currentNode.next

    def deleteEnd(self):
        if self.head is None:
            print('list is empty. nothing to delete')
            return
        #find the second last node and set its next as null
        #start at head
        secondLastNode = self.head
        #by the end of this while loop, secondLastNode will have the value of actual second last node
        while secondLastNode.next.next != None:
            secondLastNode = secondLastNode.next
        secondLastNode.next = None


firstNode = Node(1)
secondNode = Node(2)
thirdNode = Node(3)
linkedList = LinkedList()
linkedList.insert(firstNode)
linkedList.insert(secondNode)
linkedList.insert(thirdNode)

linkedList.printList()
print('after deleting last node : ')
linkedList.deleteEnd()

linkedList.printList()
