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

    def insert_after_value(self, replaceNode, newNode ):
        if self.head is None:
            print('linked list is empty. cannot insert after a particular node.')
        else:
            currentNode = self.head
            #loop over all the nodes starting from head.
            # if the current node is the node to be replaced, set the next as the new node, and new nodes next as
            # previous currentNode's next
            while True:
                if currentNode == replaceNode:
                    nextNode = currentNode.next
                    currentNode.next = newNode
                    newNode.next = nextNode
                    break
                currentNode = currentNode.next


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

node1 = Node(89)
node2 = Node(90)
node3 = Node(91)
linkedList = LinkedList()
linkedList.insert(node1)
linkedList.insert(node2)
linkedList.insert_after_value(node1, node3)
linkedList.printList()
