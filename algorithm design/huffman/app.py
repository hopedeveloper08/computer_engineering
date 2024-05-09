from model import read_data_from_file, build_huffman_tree, huffman_encoding, huffman_decoding, write_to_file, convert_text_to_table


if __name__ == '__main__':
    text = read_data_from_file()
    table = convert_text_to_table(text)
    tree = build_huffman_tree(table)
    code_table, code = huffman_encoding(tree, text)
    write_to_file(code_table, code)

    print("decode: " + huffman_decoding(code, code_table))
