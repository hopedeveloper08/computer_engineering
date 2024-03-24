class Node:
    def __init__(self, is_data=True, row=None, col=None, value=None, down=None, right=None):
        self.down = down
        self.right = right
        self.is_data = is_data
        if is_data:
            self.row = row
            self.col = col
            self.value = value

    def __repr__(self):
        if self.is_data:
            return f"({self.row}, {self.col}, {self.value})"

        return "head"


class LLSparseMatrix:
    def __init__(self, max_size=1000):
        self.rows = 0
        self.cols = 0
        self.max_size = max_size
        self.head_nodes = list()

    """ O(row * cols) """
    def load_matrix(self):
        with open("models/input.txt") as file:
            matrix = file.read().split('\n')
            matrix.pop()

        for idx, row in enumerate(matrix):
            row = row.split(' ')
            for col, cell in enumerate(row):
                if cell != '0':
                    self.add_term(r=idx, c=col, v=int(cell))

    """ O(rows + cols) """
    def add_term(self, r, c, v):
        if r >= self.max_size or c >= self.max_size:
            return False

        self.__update_dimensions(r, c)

        node = self.search_term(r, c)
        if node:
            node.value += v
            if node.value == 0:
                self.remove_term(r, c)
            return True

        self.__add_new_term(r, c, v)

    """ O(rows + cols) """
    def __update_dimensions(self, r, c):
        for _ in range(max(r, c) + 1 - len(self.head_nodes)):
            self.head_nodes.append(Node(is_data=False))

        self.rows = max(r + 1, self.rows)
        self.cols = max(c + 1, self.cols)

    """ O(rows + cols) """
    def __add_new_term(self, r, c, v):
        node = Node(row=r, col=c, value=v)

        rp, prev_rp = self.head_nodes[r].right, self.head_nodes[r]
        while rp and rp.col < c:
            prev_rp, rp = rp, rp.right
        node.right, prev_rp.right = rp, node

        cp, prev_cp = self.head_nodes[c].down, self.head_nodes[c]
        while cp and cp.row < r:
            prev_cp, cp = cp, cp.down
        node.down, prev_cp.down = cp, node

    """ O(rows + cols) """
    def remove_term(self, r, c):
        if r >= self.max_size or c >= self.max_size:
            return False

        if r >= len(self.head_nodes) or c >= len(self.head_nodes):
            return False

        prev_rp, rp = self.head_nodes[r], self.head_nodes[r].right
        while rp and rp.col < c:
            prev_rp, rp = rp, rp.right

        if not rp or rp.row != r or rp.col != c:
            return False

        prev_cp, cp = self.head_nodes[c], self.head_nodes[c].down
        while cp and cp.row < r:
            prev_cp, cp = cp, cp.down

        prev_rp.right, prev_cp.down = rp.right, cp.down

        last = self.head_nodes[-1]

        while not last.right and not last.down:
            self.head_nodes.pop()
            self.rows -= 1
            self.cols -= 1
            if len(self.head_nodes) != 0:
                last = self.head_nodes[-1]
            else:
                break

        return rp.value

    """ O(cols) """
    def search_term(self, r, c):
        if r >= self.max_size or c >= self.max_size:
            return None

        rp = self.head_nodes[r].right
        while rp and rp.col < c:
            rp = rp.right

        if not rp or rp.row != r or rp.col != c:
            return None

        return rp

    """ O(max(rows, cols) * rows) """
    def transpose(self):
        for head in self.head_nodes:
            head.down, head.right = head.right, head.down
            node = head.down
            while node:
                node.row, node.col = node.col, node.row
                node.right, node.down = node.down, node.right
                node = node.down

        self.rows, self.cols = self.cols, self.rows

    """ O(max(rows, cols)**2 * rows) """
    def add_matrix(self, other):
        for node in other.head_nodes:
            current_node = node.right
            while current_node:
                self.add_term(current_node.row, current_node.col, current_node.value)
                current_node = current_node.right

    """ O(max(rows, cols)**2 * rows) """
    def subtract_matrix(self, other):
        for node in other.head_nodes:
            current_node = node.right
            while current_node:
                self.add_term(current_node.row, current_node.col, -current_node.value)
                current_node = current_node.right

    """ O(max(rows, cols)**2 * rows) """
    def multiply_matrix(self, other):
        result = LLSparseMatrix()

        for i in range(self.rows):
            for j in range(other.cols):
                dot_product = 0
                for k in range(self.cols):
                    term1 = self.search_term(i, k)
                    term2 = other.search_term(k, j)
                    if term1 and term2:
                        dot_product += term1.value * term2.value

                if dot_product != 0:
                    result.add_term(i, j, dot_product)

        self.head_nodes = result.head_nodes

    """ O(max(rows, cols)**2 """
    def print_sparse_matrix(self):
        print("rows:")
        for i in range(self.rows):
            print(f"head({i}) -> ", end='')
            node = self.head_nodes[i].right
            while node:
                print(node.value, end=' -> ')
                node = node.right
            print("null")

        print("\ncols:")
        for j in range(self.rows):
            print(f"head({j}) -> ", end='')
            node = self.head_nodes[j].down
            while node:
                print(node.value, end=' -> ')
                node = node.down
            print("null")

    """ O(max(rows, cols)**2 """
    def convert_and_print(self, obj):
        matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for node in self.head_nodes:
            rp = node
            while rp.right:
                rp = rp.right
                matrix[rp.row][rp.col] = rp.value

        with open(f"output{obj}.txt", 'w') as file:
            for row in matrix:
                print(*row)
                for cell in row:
                    file.write(f"{cell} ")
                file.write("\n")
