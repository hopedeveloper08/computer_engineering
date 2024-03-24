from Polynomial import Polynomial
import unittest


class TestPolynomial(unittest.TestCase):

    def test_add_term(self):
        p = Polynomial()
        p.add_term(2, 5)
        self.assertNotEqual(p.coef[2], 0)
        self.assertEqual(p.coef[2], 5)
        self.assertEqual(p.degree, 2)

        p.add_term(3, 6)
        self.assertNotEqual(p.coef[3], 0)
        self.assertEqual(p.coef[3], 6)
        self.assertEqual(p.degree, 3)

        p.add_term(3, -3)
        self.assertNotEqual(p.coef[3], 0)
        self.assertNotEqual(p.coef[3], 6)
        self.assertEqual(p.coef[3], 3)
        self.assertEqual(p.degree, 3)

        p.add_term(2, 5)
        self.assertNotEqual(p.coef[2], 0)
        self.assertNotEqual(p.coef[2], 5)
        self.assertEqual(p.coef[2], 10)
        self.assertEqual(p.degree, 3)

    def test_remove_term(self):
        p = Polynomial()
        p.add_term(0, 1)
        p.remove_term(0)
        self.assertEqual(p.coef[0], 0)
        self.assertEqual(p.degree, 0)

        p.add_term(10, 5)
        p.add_term(10, 5)
        p.add_term(10, 5)
        self.assertEqual(p.degree, 10)
        p.remove_term(10)
        self.assertEqual(p.coef[10], 0)
        self.assertEqual(p.degree, 0)

    def test_add(self):
        p = Polynomial()
        p0 = Polynomial()
        p1 = Polynomial()
        p0.add_term(3, 6)
        p1.add_term(3, 3)
        p0.add_term(2, 10)
        p1.add_term(2, 5)
        p1.add_term(10, 7)
        p0.add(p1)
        self.assertEqual(p0.degree, 10)
        self.assertEqual(p0.coef[2], 15)
        self.assertEqual(p0.coef[3], 9)
        self.assertEqual(p0.coef[10], 7)

    def test_sub(self):
        p0 = Polynomial()
        p1 = Polynomial()
        p0.add_term(3, 6)
        p1.add_term(3, 3)
        p0.add_term(2, 10)
        p1.add_term(2, 5)
        p1.add_term(10, 7)
        p0.sub(p1)
        self.assertEqual(p0.degree, 10)
        self.assertEqual(p0.coef[2], 5)
        self.assertEqual(p0.coef[3], 3)
        self.assertEqual(p0.coef[10], -7)

    def test_mult(self):
        p = Polynomial()
        p.add_term(0, 2)
        p.add_term(1, 3)
        p.add_term(2, 4)

        p.mult(p)
        self.assertEqual(p.degree, 4)
        self.assertEqual(p.coef[0], 4)
        self.assertEqual(p.coef[1], 12)
        self.assertEqual(p.coef[2], 25)
        self.assertEqual(p.coef[3], 24)
        self.assertEqual(p.coef[4], 16)
