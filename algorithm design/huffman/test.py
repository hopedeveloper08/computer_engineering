import unittest
from model import huffman_encoding, build_huffman_tree, convert_text_to_table, huffman_decoding


class TestHuffman(unittest.TestCase):
    def test_convert_text_to_table(self):
        text = "hello world"
        table = convert_text_to_table(text)

        self.assertEqual(table['h'], 1)
        self.assertEqual(table[' '], 1)
        self.assertEqual(table['l'], 3)

        self.assertNotEqual(table['o'], 0)
        self.assertNotEqual(table['d'], 2)
        self.assertNotEqual(table[' '], 0)

    def test_build_huffman_tree(self):
        text = "a fast runner need never be afraid of the dark"
        table = convert_text_to_table(text)
        tree = build_huffman_tree(table)

        self.assertEqual(tree.freq, 46)
        self.assertEqual(tree.left.freq, 19)
        self.assertEqual(tree.right.freq, 27)

    def test_huffman_coding(self):
        text = 'congratulations you just have built a compression algorithm.'
        table = convert_text_to_table(text)
        tree = build_huffman_tree(table)
        code_table, code = huffman_encoding(tree, text)

        decode = huffman_decoding(code, code_table)

        self.assertEqual(decode, text)


if __name__ == '__main__':
    unittest.main()
