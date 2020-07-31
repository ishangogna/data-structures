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
            print('list is empty')
            return
        else:
            currentNode = self.head
            while True:
                if currentNode is None:
                    break
                print(currentNode.data)
                currentNode = currentNode.next

    def insertAt(self,newNode, position):
        if self.head is None:
            print('empty list.')
        else:
            #to keep track of currentPosition and currentNode starts at head node
            currentPosition = 0
            currentNode = self.head
            #loop runs till currentPosition becomes equal to index provided
            # and then sets prevNode's next as new node
            # and then sets new node's next as current Node
            while True:
                if currentPosition==position:
                    prevNode.next = newNode
                    newNode.next = currentNode
                    break
                prevNode = currentNode
                currentNode = currentNode.next
                currentPosition+=1


firstNode = Node(1)
secondNode = Node(2)
thirdNode = Node(3)
fourthNode = Node(4)
fifthNode = Node(5)
sixthNode = Node(6)
linkedList = LinkedList()
linkedList.insert(firstNode)
linkedList.insert(secondNode)
linkedList.insert(thirdNode)
linkedList.insert(fourthNode)
linkedList.insert(fifthNode)
linkedList.insertAt(sixthNode, 2)
linkedList.printList()
