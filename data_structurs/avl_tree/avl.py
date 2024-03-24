class AVL:
    class Node:
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data
            self.count = 1
        
    def __init__(self):
        self.root = None

    @staticmethod
    def get_height(root):
        if root is None:
            return 0
        
        return 1 + max(AVL.get_height(root.left), AVL.get_height(root.right))
    
    def _balance_factor(self, root, data):
        balance = AVL.get_height(root.left) - AVL.get_height(root.right)
        if balance > 1:
            if data < root.left.data:
                return self._left_left_rotate(root) 

            return self._left_right_rotate(root)

        if balance < -1:
            if data > root.right.data:
                return self._right_right_rotate(root) 
             
            return self._right_left_rotate(root)
        
        return root
    
    def _left_left_rotate(self, root):
        left_child = root.left
        root.left = left_child.right
        left_child.right = root

        return left_child

    def _right_right_rotate(self, root):
        right_child = root.right
        root.right = right_child.left
        right_child.left = root

        return right_child

    def _left_right_rotate(self, root):
        left_child = root.left

        root.left = left_child.right
        left_child.right = root.left.left
        root.left.left = left_child

        return self._left_left_rotate(root)
    
    def _right_left_rotate(self, root):
        right_child = root.right

        root.right = right_child.left
        right_child.left = root.right.right
        root.right.right = right_child

        return self._right_right_rotate(root)

    def insert(self, data):
        def insert_(root):
            if root is None:
                return self.Node(data)
            
            if data < root.data:
                root.left = insert_(root.left)
            elif data > root.data:
                root.right = insert_(root.right)
            else:
            	root.count += 1

            return self._balance_factor(root, data)

        self.root = insert_(self.root)

    def delete(self, data):
        def delete_(root, data):
            if root is None:
                return root

            if data < root.data:
                root.left = delete_(root.left, data)
            elif data > root.data:
                root.right = delete_(root.right, data)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                
                current = root.right
                while current.left:
                    current = current.left

                root.data = current.data
                current.data = data
                
                root.right = delete_(root.right, data)

            return self._balance_factor(root, data)

        self.root = delete_(self.root, data)
    
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

    def preorder(self):
        def preorder_(root):
            if root is None:
                return
            
            print(root.data, end=' ')
            preorder_(root.left)
            preorder_(root.right)

        preorder_(self.root)
        print()

    def inorder(self):
        def inorder_(root):
            if root is None:
                return
            
            inorder_(root.left)
            print(root.data, end=' ')
            inorder_(root.right)

        inorder_(self.root)
        print()

    def postorder(self):
        def postorder_(root):
            if root is None:
                return
            
            postorder_(root.left)
            postorder_(root.right)
            print(root.data, end=' ')

        postorder_(self.root)
        print()
