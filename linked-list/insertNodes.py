class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.length = 0

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
            llstr = ''
            while True:
                if currentNode is None:
                    break
                llstr = llstr + str(currentNode.data) + '=>'
                currentNode = currentNode.next
            print(llstr)

    def insertNodes(self, listOfNodes):
        for node in listOfNodes:
            self.insert(node)



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

linkedList = LinkedList()
linkedList.insertNodes([node1, node2, node3, node4, node5])

linkedList.printList()
