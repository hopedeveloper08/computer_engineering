class Polynomial:

    def __init__(self, max_exp=100):
        self.max_exp = max_exp + 1
        self.size = 0
        self.exp = [0] * max_exp
        self.coef = [0] * max_exp

    """ O(1) """
    def get_degree(self):
        return self.exp[0]

    """ O(self.size) """
    def add_term(self, e, c):
        if e >= self.max_exp or self.size == self.max_exp:
            return False

        index = self.search_term(e)
        if index == -1:
            index = self.size
            while index > 0 and e > self.exp[index - 1]:
                self.coef[index] = self.coef[index - 1]
                self.exp[index] = self.exp[index - 1]
                index -= 1
            self.exp[index] = e
            self.coef[index] = c
            self.size += 1
        else:
            self.coef[index] += c

        if self.coef[index] == 0:
            self.remove_term(e)

    """ O(self.size) """
    def remove_term(self, e):
        index = self.search_term(e)
        if index == -1:
            return None

        temp = self.coef[index]

        for i in range(index, self.size - 1):
            self.exp[i] = self.exp[i + 1]
            self.coef[i] = self.coef[i + 1]
        self.exp[self.size - 1] = 0
        self.coef[self.size - 1] = 0

        self.size -= 1
        return temp

    """ O(log(n)) """
    def search_term(self, x):
        low = 0
        h = self.size - 1
        while low <= h:
            mid = (low + h) // 2
            if self.exp[mid] == x:
                return mid
            elif x < self.exp[mid]:
                low = mid + 1
            else:
                h = mid - 1
        return -1

    """ O(other.size * self.size) """
    def add(self, other):
        for i in range(other.size):
            self.add_term(other.exp[i], other.coef[i])

    """ O(other.size * self.size) """
    def sub(self, other):
        for i in range(other.size):
            self.add_term(other.exp[i], -other.coef[i])

    """ O(self.size * other.size * self.size) """
    def mult(self, other):
        result = Polynomial()

        for i in range(self.size):
            for j in range(other.size):
                result.add_term(self.exp[i] + other.exp[j], self.coef[i] * other.coef[j])

        self.coef = result.coef.copy()
        self.exp = result.exp.copy()
        self.size = result.size

    """ O(self.size) """
    def print(self):
        for i in range(self.size):
            if self.coef[i] != 0:
                print(f"{self.coef[i]}x^{self.exp[i]}", end=' + ')
        print()
