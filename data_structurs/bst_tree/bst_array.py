class BST:
    def __init__(self, max_level):
        self.max_size = 2 ** max_level
        self.tree = [0] * self.max_size

    def search(self, data):
        index = 0
        while index < self.max_size:
            if self.tree[index] == data:
                return index
            elif data < self.tree[index]:
                index = (2 * index) + 1
            elif data > self.tree[index]:
                index = (2 * index) + 2
        return -1

    def insert(self, data):
        if self.tree[0] == 0:
            self.tree[0] = data
            return True

        index = 0
        while index < self.max_size:
            if self.tree[index] == data:
                return False
            elif data < self.tree[index]:
                if self.tree[(2 * index) + 1] == 0:
                    self.tree[(2 * index) + 1] = data
                    return True
                index = (2 * index) + 1
            elif data > self.tree[index]:
                if self.tree[(2 * index) + 2] == 0:
                    self.tree[(2 * index) + 2] = data
                    return True
                index = (2 * index) + 2

    def delete(self, data):
        delete_index = self.search(data)

        def find_min_index(index):
            while self.tree[2 * index + 1] != 0:
                index = 2 * index + 1
            return index

        def delete_node(index):
            if self.tree[index] == 0:
                return False
            elif self.tree[2 * index + 1] == 0 and self.tree[2 * index + 2] == 0:
                self.tree[index] = 0
            elif self.tree[2 * index + 1] == 0:
                self.tree[index] = self.tree[2 * index + 2]
                delete_node(2 * index + 2)
            elif self.tree[2 * index + 2] == 0:
                self.tree[index] = self.tree[2 * index + 1]
                delete_node(2 * index + 1)
            else:
                min_right_child_index = find_min_index(2 * index + 2)
                self.tree[index] = self.tree[min_right_child_index]
                delete_node(min_right_child_index)

        delete_node(delete_index)
        return True

    def preorder(self, index=0):
        if index < self.max_size and self.tree[index] != 0:
            print(self.tree[index], end=' ')
            self.preorder(2 * index + 1)
            self.preorder(2 * index + 2)

    def inorder(self, index=0):
        if index < self.max_size and self.tree[index] != 0:
            self.inorder(2 * index + 1)
            print(self.tree[index], end=' ')
            self.inorder(2 * index + 2)

    def postorder(self, index=0):
        if index < self.max_size and self.tree[index] != 0:
            self.postorder(2 * index + 1)
            self.postorder(2 * index + 2)
            print(self.tree[index], end=' ')
