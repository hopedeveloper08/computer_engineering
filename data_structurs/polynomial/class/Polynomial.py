class Term:
    def __init__(self, e, c):
        self.exp = e
        self.coef = c


class Polynomial:
    """ O(1) """
    def __init__(self, max_exp=1000):
        self.max_exp = max_exp + 1
        self.size = 0
        self.data = [Term(0, 0)] * self.max_exp

    """ O(1) """
    def get_degree(self):
        return self.data[0].exp

    """ O(self.size + O(log(size))) """
    def add_term(self, e, c):
        if e >= self.max_exp or self.size == self.max_exp:
            return False

        index = self.search_term(e)
        if index == -1:
            index = self.size
            while index > 0 and e > self.data[index - 1].exp:
                self.data[index] = self.data[index - 1]
                index -= 1
            self.data[index] = Term(e, c)
            self.size += 1
        else:
            self.data[index].coef += c

        if self.data[index].coef == 0:
            self.remove_term(e)

    """ O(self.size) """
    def remove_term(self, e):
        index = self.search_term(e)
        if index == -1:
            return None

        coef = self.data[index].coef

        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = Term(0, 0)

        self.size -= 1
        return coef

    """ O(log(size)) """
    def search_term(self, x):
        l = 0
        h = self.size - 1
        while l <= h:
            mid = (l + h) // 2
            if self.data[mid].exp == x:
                return mid
            elif x < self.data[mid].exp:
                l = mid + 1
            else:
                h = mid - 1
        return -1

    """ O(other.size * self.size) """
    def add(self, other):
        for i in range(other.size):
            self.add_term(other.data[i].exp, other.data[i].coef)

    """ O(other.size * self.size) """
    def sub(self, other):
        for i in range(other.size):
            self.add_term(other.data[i].exp, -other.data[i].coef)

    """ O(self.size * other.size * self.size) """
    def mult(self, other):
        result = Polynomial()

        for i in range(self.size):
            for j in range(other.size):
                result.add_term(self.data[i].exp + other.data[j].exp, self.data[i].coef * other.data[j].coef)

        self.data = result.data.copy()
        self.size = result.size

    """ O(self.size) """
    def print(self):
        for i in range(self.size):
            if self.data[i].coef != 0:
                print(f"{self.data[i].coef}x^{self.data[i].exp}", end=' + ')
        print()
