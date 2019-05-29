#  http://ejklike.github.io/2018/01/09/traversing-a-binary-tree-1.html#fn:1

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
    
    def delete(self, key):
        self.root, deleted = self.delete_value(self.root, key)
        return deleted

    def delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                #replace the node to the leftmost of node.right
                parent, child = node, node.right
                
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self.delete_value(node.left, key)
        else:
            node.right, deleted = self.delete_value(node.right, key)
        return node, deleted

    def print_pre_order(self, root):
        if root:
            print(root.data)
            self.print_pre_order(root.left)
            self.print_pre_order(root.right)

    def print_in_order(self, root):
        if root:
            self.print_in_order(root.left)
            print(root.data)
            self.print_in_order(root.right)

    def print_post_order(self, root):
        if root:
            self.print_post_order(root.left)
            self.print_post_order(root.right)
            print(root.data)

arr = [21, 28, 14, 32, 25, 18, 11, 30, 19, 15]

bst = BinaryTree()
for item in arr:
    bst.insert(item)

bst.print_pre_order(bst.root)