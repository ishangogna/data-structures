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
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

    def insertBeginning(self,newNode):
        #if list is empty, set new node as head node
        if self.head is None:
            self.head = newNode
        else:
            #else first store the current head node in nextNode
            #set new node as head Node
            #set new node's next as head node
            nextNode = self.head
            self.head = newNode
            newNode.next = nextNode



firstNode = Node('first node')
secondNode = Node('second node')
thirdNode = Node('zeroth Node')
linkedList = LinkedList()
linkedList.insert(firstNode)
linkedList.insert(secondNode)
linkedList.insertBeginning(thirdNode)

linkedList.printList()
