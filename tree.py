class Node:
    def __init__(self, data=0, left = None , right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insert_value(self.root, data)
        return self.root is not None

    def insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self.insert_value(node.left, data)
            else:
                node.right = self.insert_value(node.right, data)
        return node
        