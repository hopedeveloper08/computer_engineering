import heapq


class Node:
    def __init__(self, freq, char, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, next_):
        return self.freq < next_.freq

    def __str__(self):
        return f"({self.freq}, {self.char}, {self.left}, {self.right})"


def read_data_from_file():
    with open('input.txt', 'r') as f:
        file = f.read()

    return file


def write_to_file(data, code):
    with open('output.txt', 'w') as f:
        f.writelines(code+'\n')
        for key, value in data.items():
            f.writelines(f"{key}: {value}\n")


# O(n)
def convert_text_to_table(text):
    table = dict()

    for char in text:
        table[char] = 0

    for char in text:
        table[char] += 1

    return table


# O(nlog(n))
def build_huffman_tree(data):
    heap = list()

    for char, freq in data.items():  # O(nlog(n))
        heapq.heappush(heap, Node(freq, char))

    while len(heap) > 1:  # O(n)
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        parent = Node(left.freq + right.freq, None, left, right)

        heapq.heappush(heap, parent)

    return heapq.heappop(heap)


# O(n)
def huffman_encoding(tree, text):
    code_table = dict()
    _encoding(tree, '', code_table)

    code = ''
    for char in text:
        code += code_table[char]

    return code_table, code


def _encoding(node, code, codes):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = code

    _encoding(node.left, code + "0", codes)
    _encoding(node.right, code + "1", codes)


# O(n^2)
def huffman_decoding(encoded_data, code_table):
    decoded_data = ""
    current_code = ""
    for bit in encoded_data:
        current_code += bit
        for char, code in code_table.items():
            if code == current_code:
                decoded_data += char
                current_code = ""
                break
    return decoded_data
