class Polynomial:
    """ O(1) """
    def __init__(self, max_exp=1000):
        self.max_exp = max_exp + 1
        self.coef = [0] * max_exp
        self.degree = 0

    """ O(1) """
    def add_term(self, e, c):
        if e >= self.max_exp:
            return False

        self.coef[e] += c
        if e > self.degree:
            self.degree = e

    """ O(self.degree) """
    def remove_term(self, e):
        if e > self.max_exp:
            return False

        self.coef[e] = 0

        if e == self.degree:
            temp_e = e - 1
            while self.coef[temp_e] == 0 and temp_e > 0:
                temp_e -= 1
            if temp_e > 0:
                self.degree = temp_e
            else:
                self.degree = 0

    """ O(other.degree) """
    def add(self, other):
        for i in range(other.degree + 1):
            self.add_term(i, other.coef[i])

    """ O(other.degree) """
    def sub(self, other):
        for i in range(other.degree + 1):
            self.add_term(i, -other.coef[i])

    """ O(self.degree * other.degree) """
    def mult(self, other):
        temp = [0] * self.max_exp

        for i in range(self.degree + 1):
            for j in range(other.degree + 1):
                temp[i + j] += self.coef[i] * other.coef[j]

        self.degree = self.degree + other.degree
        self.coef = temp

    """ O(self.degree) """
    def print(self):
        for i in range(self.degree, -1, -1):
            if self.coef[i] != 0:
                print(f"{self.coef[i]}x^{i}", end=' ')
            if i > 0 and self.coef[i - 1] != 0:
                print("+", end=' ')
        print()
