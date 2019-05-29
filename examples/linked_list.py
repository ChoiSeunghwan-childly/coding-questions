class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def insertNode(self, newNode):
        node = self.head
        while node.next != None:
            node = node.next

        node.next = newNode
        newNode.next = None

    def printNode(self):
        node = self.head
        while node.next != None:
            node = node.next
            print(node.data)

li = LinkedList()

for i in range(10):
    li.insertNode(Node(i))

li.printNode()