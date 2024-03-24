class BST:
    class Node:
        def __init__(self, data, parent):
            self.left = None
            self.right = None
            self.data = data
            self.parent = parent

    def __init__(self):
        self.root = None

    def search(self, data):
        def search_(root):
            if root is None:
                return root
            
            if data < root.data:
                return search_(root.left)
            elif data > root.data:
                return search_(root.right)
            else:
                return root
        
        return search_(self.root)

    def insert(self, data):
        def insert_(root):
            if root is None:
                return self.Node(data)
            
            if data < root.data:
                root.left = insert_(root.left)
            elif data > root.data:
                root.right = insert_(root.right)
            
            return root
        
        insert_(self.root)

    def delete(self, data):
        node = self.search(data)

        if node is None:
            return

        if node.left is None:
            node.parent = node.right
            return
        if node.right is None:
            node.parent = node.left
            return

        min_node = node.right
        if min_node:
            while min_node.left:
                min_node = min_node.left

        node.data = min_node.data
        min_node.parent.left = min_node.right

    def inorder(self):
        def inorder_(root):
            if root is None:
                return
            
            self.preorder(root.left)
            print(root.data, end=' ')
            self.preorder(root.right)

        inorder_(self.root)
