class RedBlack:
    class Node:
        def __init__(self, data, is_red=True, left=None, right=None, parent=None):
            self.data = data
            self.is_red = is_red
            self.left = left
            self.right = right
            self.parent = parent
            self.count = 1
        
        @property
        def is_left_child(self):
            return self == self.parent.left

        @property
        def is_right_child(self):
            return self == self.parent.right
        
        @property
        def sibling(self):
            if self.is_left_child:
                return self.parent.right
            else:
                return self.parent.left

    null:Node = Node(None, False)

    def __init__(self):
        self.root = RedBlack.null
    
    def search(self, data):
        def search_recursive(root):
            if root is RedBlack.null:
                return root
            
            if data < root.data:
                return search_recursive(root.left)
            elif data > root.data:
                return search_recursive(root.right)
            else:
                return root
        
        return search_recursive(self.root)
    
    def insert(self, data):
        if self.root is RedBlack.null:
            self.root = self.Node(data, False, RedBlack.null, RedBlack.null, RedBlack.null)
            return

        node = self.root
        while True:
            if data < node.data:
                if node.left is not self.null:
                    node = node.left
                else:
                    node.left = self.Node(data, True, RedBlack.null, RedBlack.null, node)
                    if node.is_red:
                        self._insert_fixup(node.left)

                    self.root.is_red = False
                    return

            elif data > node.data:
                if node.right is not self.null:
                    node = node.right
                else:
                    node.right = self.Node(data, True, RedBlack.null, RedBlack.null, node)
                    if node.is_red:
                        self._insert_fixup(node.right)

                    self.root.is_red = False
                    return
                
            else:
                node.count += 1
                return
    
    def _insert_fixup(self, node):
        while node.parent.is_red:
            uncle = node.parent.sibling

            if uncle.is_red:
                node.parent.is_red = False
                uncle.is_red = False
                node.parent.parent.is_red = True
                node = node.parent.parent
            
            else:
                if node.parent.is_left_child and node.is_left_child:
                    node.parent.is_red = False
                    node.parent.parent.is_red = True
                    self._right_rotate(node.parent.parent)

                elif node.parent.is_left_child and node.is_right_child:
                    node.is_red = False
                    node.parent.parent.is_red = True
                    self._left_rotate(node.parent)
                    self._right_rotate(node.parent)
                
                elif node.parent.is_right_child and node.is_left_child:
                    node.is_red = False
                    node.parent.parent.is_red = True
                    self._right_rotate(node.parent)
                    self._left_rotate(node.parent)

                elif node.parent.is_right_child and node.is_right_child:
                    node.parent.is_red = False
                    node.parent.parent.is_red = True
                    self._left_rotate(node.parent.parent)

    def _left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left is not RedBlack.null:
            right_child.left.parent = node
        
        self._transplant(node, right_child)

        right_child.left = node
        node.parent = right_child

    def _right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right is not RedBlack.null:
            left_child.right.parent = node

        self._transplant(node, left_child)

        left_child.right = node
        node.parent = left_child
    
    def delete(self, data):
        node = self.search(data)
        color_is_red = node.is_red

        if node is RedBlack.null:
            return

        if node.left is RedBlack.null:
            fix_node = node.right
            self._transplant(node, node.right)
        elif node.right is RedBlack.null:
            fix_node = node.left
            self._transplant(node, node.left)
        else:
            min_node = node.right
            while min_node.left is not RedBlack.null:
                min_node = min_node.left
            
            color_is_red = min_node.is_red
            fix_node = min_node.right

            if min_node.parent == node:
                fix_node.parent = min_node
            else:
                self._transplant(min_node, min_node.right)
                min_node.right = node.right
                min_node.right.parent = min_node
            
            self._transplant(node, min_node)
            min_node.left = node.left
            min_node.left.parent = min_node
            min_node.is_red = node.is_red

        if not color_is_red:
            self._delete_fixup(fix_node)
            
    def _transplant(self, node, child):
        if node.parent is RedBlack.null:
            self.root = child
        elif node.is_left_child:
            node.parent.left = child
        else:
            node.parent.right = child
        
        child.parent = node.parent

    def _delete_fixup(self, node):
        while node.data != self.root.data and not node.is_red:
            sibling = node.sibling

            if sibling.is_red:
                sibling.is_red = False
                node.parent.is_red = True

                if node.is_left_child:
                    self._left_rotate(node.parent)
                    sibling = node.parent.right
                else:
                    self._right_rotate(node.parent)
                    sibling = node.parent.left
                
            if not sibling.left.is_red and not sibling.right.is_red:
                sibling.is_red = True
                node = node.parent

            else:    
                if node.is_left_child and not sibling.right.is_red:
                    sibling.left.is_red = False
                    sibling.is_red = True 
                    self._right_rotate(sibling)
                    sibling = node.parent.right
                elif node.is_right_child and not sibling.left.is_red:
                    sibling.right.is_red = False
                    sibling.is_red = True 
                    self._left_rotate(sibling)
                    sibling = node.parent.left
                
                sibling.is_red = node.parent.is_red
                node.parent.is_red = False
                if node.is_left_child:
                    sibling.right.is_red = False
                    self._left_rotate(node.parent)
                else:
                    sibling.left.is_red = False
                    self._right_rotate(node.parent)
                node = self.root
        
        node.is_red = False

    def preorder(self):
        def preorder_recursive(root):
            if root is self.null:
                return
            
            print(root.data, end=' ')
            preorder_recursive(root.left)
            preorder_recursive(root.right)

        preorder_recursive(self.root)
        print()

    def inorder(self):
        def inorder_recursive(root):
            if root is self.null:
                return
            
            inorder_recursive(root.left)
            print(root.data, end=' ')
            inorder_recursive(root.right)

        inorder_recursive(self.root)
        print()

    def postorder(self):
        def postorder_recursive(root):
            if root is self.null:
                return
            
            postorder_recursive(root.left)
            postorder_recursive(root.right)
            print(root.data, end=' ')

        postorder_recursive(self.root)
        print()
