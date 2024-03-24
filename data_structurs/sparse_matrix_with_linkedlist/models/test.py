from models.linkedlist_sparse_matrix import LLSparseMatrix
import unittest


class TestLinklist(unittest.TestCase):

    def test_add_term(self):
        sp = LLSparseMatrix()

        sp.add_term(0, 0, 1)
        self.assertEquals(sp.head_nodes[0].right.value, 1)
        self.assertEquals(sp.head_nodes[0].down.value, 1)

        sp.add_term(1, 1, 2)
        self.assertEquals(sp.head_nodes[1].right.value, 2)
        self.assertEquals(sp.head_nodes[1].down.value, 2)

        sp.add_term(2, 2, 3)
        self.assertEquals(sp.head_nodes[2].right.value, 3)
        self.assertEquals(sp.head_nodes[2].down.value, 3)

        self.assertEquals(sp.rows, 3)
        self.assertEquals(sp.cols, 3)

        sp.add_term(1, 3, 4)
        self.assertEquals(sp.head_nodes[1].right.right.value, 4)
        self.assertEquals(sp.head_nodes[3].down.value, 4)

        self.assertEquals(sp.rows, 3)
        self.assertEquals(sp.cols, 4)

        sp.add_term(3, 1, 4)
        self.assertEquals(sp.head_nodes[3].right.value, 4)
        self.assertEquals(sp.head_nodes[1].down.down.value, 4)

        self.assertEquals(sp.rows, 4)
        self.assertEquals(sp.cols, 4)

    def test_remove_term(self):
        sp = LLSparseMatrix()

        sp.add_term(0, 0, 1)
        sp.add_term(1, 1, 2)
        sp.add_term(2, 2, 3)
        sp.remove_term(1, 1)

        self.assertNotEquals(sp.head_nodes[0].right, None)
        self.assertNotEquals(sp.head_nodes[0].down, None)
        self.assertEquals(sp.head_nodes[1].right, None)
        self.assertEquals(sp.head_nodes[1].down, None)
        self.assertNotEquals(sp.head_nodes[2].right, None)
        self.assertNotEquals(sp.head_nodes[2].down, None)

    def test_transpose(self):
        sp = LLSparseMatrix()

        sp.add_term(0, 0, 1)
        sp.add_term(0, 1, 2)
        sp.add_term(0, 2, 3)
        sp.transpose()

        self.assertEquals(sp.head_nodes[1].down, None)
        self.assertEquals(sp.head_nodes[2].down, None)
        self.assertEquals(sp.head_nodes[0].down.value, 1)
        self.assertEquals(sp.head_nodes[0].right.value, 1)
        self.assertEquals(sp.head_nodes[1].right.value, 2)
        self.assertEquals(sp.head_nodes[0].down.down.value, 2)
        self.assertEquals(sp.head_nodes[2].right.value, 3)
        self.assertEquals(sp.head_nodes[0].down.down.down.value, 3)

    def test_add_matrix(self):
        sp = LLSparseMatrix()
        sp2 = LLSparseMatrix()

        sp.add_term(0, 0, 1)
        sp.add_term(1, 1, 2)
        sp.add_term(2, 2, 3)
        sp2.add_term(0, 0, 10)
        sp2.add_term(1, 1, 10)
        sp2.add_term(2, 0, 10)
        sp.add_matrix(sp2)

        self.assertEquals(sp.head_nodes[0].right.value, 11)
        self.assertEquals(sp.head_nodes[0].down.value, 11)
        self.assertEquals(sp.head_nodes[1].right.value, 12)
        self.assertEquals(sp.head_nodes[1].down.value, 12)
        self.assertEquals(sp.head_nodes[2].right.right.value, 3)
        self.assertEquals(sp.head_nodes[2].down.value, 3)
        self.assertEquals(sp.head_nodes[2].right.value, 10)
        self.assertEquals(sp.head_nodes[0].down.down.value, 10)

    def test_subtract_matrix(self):
        sp = LLSparseMatrix()
        sp2 = LLSparseMatrix()

        sp.add_term(0, 0, 1)
        sp.add_term(1, 1, 2)
        sp.add_term(2, 2, 3)
        sp2.add_term(0, 0, 10)
        sp2.add_term(1, 1, 10)
        sp2.add_term(2, 2, 3)
        sp.subtract_matrix(sp2)

        self.assertEquals(sp.head_nodes[0].right.value, -9)
        self.assertEquals(sp.head_nodes[0].down.value, -9)
        self.assertEquals(sp.head_nodes[1].right.value, -8)
        self.assertEquals(sp.head_nodes[1].down.value, -8)

    def test_multiply_matrix(self):
        matrix1 = LLSparseMatrix()
        matrix1.add_term(0, 0, 2)
        matrix1.add_term(1, 1, 3)

        matrix2 = LLSparseMatrix()
        matrix2.add_term(0, 0, 4)
        matrix2.add_term(0, 1, 5)
        matrix2.add_term(1, 1, 6)

        matrix1.multiply_matrix(matrix2)

        self.assertEqual(matrix1.search_term(0, 0).value, 8)
        self.assertEqual(matrix1.search_term(0, 1).value, 10)
        self.assertEqual(matrix1.search_term(1, 1).value, 18)


if __name__ == '__main__':
    unittest.main()
