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

    def getLength(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            self.length += 1
            currentNode = currentNode.next
        return self.length

    def findFromEnd(self, position):
        length = self.getLength()
        indexOfNode = length-position
        currentPosition = 0
        lastNode = self.head
        while currentPosition < indexOfNode :
            lastNode = lastNode.next
            currentPosition += 1
        print(str(position) + 'th node from the end is : ' + str(lastNode.data))



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
linkedList = LinkedList()
linkedList.insert(node1)
linkedList.insert(node2)
linkedList.insert(node3)
linkedList.insert(node4)
linkedList.insert(node5)
linkedList.insert(node6)
linkedList.insert(node7)
linkedList.insert(node8)
linkedList.insert(node9)
linkedList.insert(node10)


linkedList.printList()
linkedList.findFromEnd(3)
