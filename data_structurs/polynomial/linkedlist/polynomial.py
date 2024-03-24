class Node:
    def __init__(self, coef, exp, link=None):
        self.coef = coef
        self.exp = exp
        self.link = link

    def __repr__(self):
        return f"{self.coef}x^{self.exp}"


class Polynomial:

    """ O(1) """
    def __init__(self):
        self.head = Node(None, None)

    """ O(list_size) """
    def add_term(self, exp, coef):
        if coef == 0:
            return False
        current = self.head.link
        prev = self.head
        while current:
            if current.exp == exp:
                current.coef += coef
                if current.coef == 0:
                    prev.link = current.link
                return True
            elif current.exp < exp:
                node = Node(coef, exp, current)
                prev.link = node
                return True
            prev = current
            current = current.link
        node = Node(coef, exp)
        prev.link = node
        return True

    """ O(list_size) """
    def remove_term(self, exp):
        current = self.head.link
        prev = self.head
        while current:
            if current.exp == exp:
                prev.link = current.link
                return True
            prev = current
            current = current.link
        return False

    """ O(list_size) """
    def search_term(self, exp):
        current = self.head.link
        while current:
            if current.exp == exp:
                return current

        return None

    """ O(other.list_size * self.list_size) """
    def add(self, other):
        node = other.head.link
        while node:
            self.add_term(node.exp, node.coef)
            node = node.link

    """ O(other_list_size * self.list_size) """
    def sub(self, other):
        node = other.head.link
        while node:
            self.add_term(node.exp, -node.coef)
            node = node.link

    """ O(other_list_size * self.list_size * self.list_size) """
    def mult(self, other):
        result = Polynomial()
        node1 = self.head.link
        while node1:
            node2 = other.head.link
            while node2:
                exp = node1.exp + node2.exp
                coef = node1.coef * node2.coef
                result.add_term(exp, coef)
                node2 = node2.link
            node1 = node1.link

        self.head = result.head

    """ O(list_size) """
    def print(self):
        current = self.head.link
        while current:
            print(current, '+', end=' ')
            current = current.link
