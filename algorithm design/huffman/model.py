class Node:

    def __init__(self, latter, frequency, left=None, right=None):
        self.latter = latter
        self.frequency = frequency
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{{'latter': {self.latter}, 'frequency': {self.frequency}}}"


def read_data_from_file():
    with open('input.txt', 'r') as f:
        file = f.read().split('\n')

    data = []
    for row in file:
        if ',' in row:
            l, f = row.split(',')
            data.append(Node(l, int(f)))

    return data


def write_to_file(data):
    with open('output.txt', 'w') as f:
        for key, value in data.items():
            f.writelines(f"{key},{value}\n")


def build_huffman_tree(data):
    while len(data) > 1:
        data = sorted(data, key=lambda x: x.frequency)

        left = data.pop(0)
        right = data.pop(0)

        parent = Node(None, left.frequency + right.frequency, left, right)

        data.append(parent)

    return data[0]


def huffman_encoding(node, code, codes):
    if node:
        if node.latter:
            codes[node.latter] = code
        huffman_encoding(node.left, code + "0", codes)
        huffman_encoding(node.right, code + "1", codes)


def main():
    data = read_data_from_file()
    root = build_huffman_tree(data)
    codes = dict()
    huffman_encoding(root, "", codes)
    write_to_file(codes)


if __name__ == '__main__':
    main()
