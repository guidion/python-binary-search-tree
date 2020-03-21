class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_root(self):
        if self.root is None:
            return True
        else:
            return False

    def add(self, value):
        if self.is_root():
            self.root = Node(value=value)
        else:
            node = self.get_node(self.root, value)
            if value <= node.value:
                node.left = Node(value=value)
            else:
                node.right = Node(value=value)

    def get_node(self, node, value):
        if node is not None:
            if value <= node.value:
                new_node = self.get_node(node.left, value)
            else:
                new_node = self.get_node(node.right, value)
            if new_node is not None:
                node = new_node
        return node

    def inorder(self, node, value):
        if node:
            if self.inorder(node.left, value):
                return True
            print(node.value)
            if node.value == value:
                return True
            if self.inorder(node.right, value):
                return True
        return False
    
    def preorder(self, node, value):
        if node:
            print(node.value)
            if node.value == value:
                return True
            else:
                if self.preorder(node.left, value):
                    return True
                if self.preorder(node.right, value):
                    return True
        return False
    
    def posorder(self, node, value):
        if node:
            if self.posorder(node.left, value):
                return True
            if self.posorder(node.right, value):
                return True
            print(node.value)
            if node.value == value:
                return True
        return False

tree = BinarySearchTree()

tree.add('F')
tree.add('B')
tree.add('A')
tree.add('D')
tree.add('C')
tree.add('E')
tree.add('G')
tree.add('I')
tree.add('H')

# result = tree.preorder(tree.root, 'X')
# result = tree.inorder(tree.root, 'X')
# result = tree.posorder(tree.root, 'X')

result = tree.preorder(tree.root, 'D')
# result = tree.inorder(tree.root, 'D')
# result = tree.posorder(tree.root, 'D')

if result:
    print("Nodo encontrado")
else:
    print("Nodo no encontrado")

