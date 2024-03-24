from model.stack import Stack


class Node:
    """ O(1) """
    def __init__(self, state, action):
        self.state = state
        self.action = action

    """ O(1) """
    def __repr__(self):
        return f"{self.state}"


class Maze:
    """ O(1) """
    def __init__(self, start, finish, move="normal"):
        self.size = None
        self.method = move
        self.start = start
        self.finish = finish
        self.maze = self.load_maze()
        self.path = self.solution()

    """ O(self.size) """
    def load_maze(self):
        with open("maze.txt") as f:
            temp = f.read().split("\n")
            self.size = len(temp) - 1

        maze = []
        for row in range(self.size):
            maze.append(temp[row].split(' '))
        maze[self.start[0]][self.start[1]] = '0'
        maze[self.finish[0]][self.finish[1]] = '0'
        return maze

    """ O(1) """
    def move(self, mouse, explored):
        row, col = mouse.state
        movements = (
            (row, col + 1),
            (row + 1, col + 1),
            (row + 1, col),
            (row + 1, col - 1),
            (row, col - 1),
            (row - 1, col - 1),
            (row - 1, col),
            (row - 1, col + 1)
        )

        horse = (
            (row + 1, col + 2),
            (row + 2, col + 1),
            (row + 2, col - 1),
            (row + 1, col - 2),
            (row - 1, col - 2),
            (row - 2, col - 1),
            (row - 2, col + 1),
            (row - 1, col + 2)
        )

        result = list()
        type_move = self.method
        if type_move == "normal":
            type_move = movements
        else:
            type_move = horse

        for r, c in type_move:
            if 0 <= r < self.size and 0 <= c < self.size and self.maze[r][c] == '0' and [r, c] not in explored:
                result.append([r, c])

        mouse.action = result

    """ O(self.size^2) """
    def solution(self):
        stack = Stack()
        current = Node(self.start, None)
        stack.push(current)
        explored = list()

        while True:
            current = stack.view()

            if stack.is_empty() or current.state == self.finish:
                path = self.result(stack)
                return path

            if not current.action or len(current.action) == 0:
                self.move(current, explored)

            if len(current.action) == 0:
                stack.pop()
            else:
                next_move = current.action.pop(0)
                if next_move not in explored:
                    node = Node(next_move, None)
                    stack.push(node)
                    explored.append(node.state)
                else:
                    if len(current.action) == 0:
                        stack.pop()

    """ O(stack size^2) """
    @staticmethod
    def result(stack):
        path = list()
        while not stack.is_empty():
            path.append(stack.pop())

        path.reverse()
        return path
