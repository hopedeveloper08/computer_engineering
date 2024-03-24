import unittest
from avl import AVL


class TestAVLTree(unittest.TestCase):
    def test_insert(self):
        self.avl_tree = AVL()
        self.avl_tree.insert(10)
        self.assertEqual(self.avl_tree.root.data, 10)

        self.avl_tree.insert(5)
        self.assertEqual(self.avl_tree.root.data, 10)
        self.assertEqual(self.avl_tree.root.left.data, 5)

        self.avl_tree.insert(15)
        self.assertEqual(self.avl_tree.root.data, 10)
        self.assertEqual(self.avl_tree.root.left.data, 5)
        self.assertEqual(self.avl_tree.root.right.data, 15)

        self.avl_tree.insert(3)
        self.avl_tree.insert(4)
        self.assertEqual(self.avl_tree.root.left.data, 4)
        self.assertEqual(self.avl_tree.root.left.left.data, 3)
        self.assertEqual(self.avl_tree.root.left.right.data, 5)
        self.assertEqual(self.avl_tree.root.right.data, 15)


    def test_delete(self):
        self.avl_tree = AVL()
        self.avl_tree.insert(10)
        self.avl_tree.insert(5)
        self.avl_tree.insert(15)
        self.avl_tree.insert(3)
        self.avl_tree.insert(7)

        self.avl_tree.delete(3)
        self.assertIsNone(self.avl_tree.search(3))

        self.avl_tree.delete(5)
        self.assertIsNone(self.avl_tree.search(5))
        self.assertIsNotNone(self.avl_tree.search(7))

        self.avl_tree.delete(10)
        self.assertIsNone(self.avl_tree.search(10))
        self.assertIsNotNone(self.avl_tree.root)
        self.assertIsNotNone(self.avl_tree.root.left)
        self.assertEqual(self.avl_tree.root.data, 15)

        self.avl_tree.delete(100)
        self.assertIsNone(self.avl_tree.search(100))

    def test_search(self):
        self.avl_tree = AVL()
        self.avl_tree.insert(10)
        self.avl_tree.insert(5)
        self.avl_tree.insert(15)
        self.avl_tree.insert(3)
        self.avl_tree.insert(2)
        self.avl_tree.insert(1)
        self.assertIsNotNone(self.avl_tree.search(10))
        self.assertIsNotNone(self.avl_tree.search(5))
        self.assertIsNotNone(self.avl_tree.search(15))
        self.assertIsNotNone(self.avl_tree.search(3))
        self.assertIsNotNone(self.avl_tree.search(2))
        self.assertIsNotNone(self.avl_tree.search(1))

        self.assertIsNone(self.avl_tree.search(100))
        self.assertIsNone(self.avl_tree.search(0))


if __name__ == '__main__':
    unittest.main()
