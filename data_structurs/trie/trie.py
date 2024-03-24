class Trie:
    class Node:
        def __init__(self):
            self.children = [None] * 26
            self.is_word = False
            self.meaning = ""
        
        def set_meaning(self, meaning):
            self.meaning = meaning
            self.is_word = True

    
    def __init__(self):
        self.root = Trie.Node()
            
    def char_to_index(self, char):
        return ord(char) - ord('a')
    
    """ O(word.size) """
    def insert_new_word(self, word, meaning):
        node = self.root

        for char in word:
            index = self.char_to_index(char)

            if not node.children[index]:
                node.children[index] = Trie.Node()

            node = node.children[index]
        
        node.set_meaning(meaning)

    """ O(word.size) """
    def search_meaning(self, word):
        node = self.root

        for char in word:
            index = self.char_to_index(char)

            if not node.children[index]:
                return None

            node = node.children[index]
        
        return node.meaning

    """ O(word.size) """
    def delete_word(self, word):
        def delete_recursive(node, word, depth):
            if node:
                if depth == len(word):
                    if node.is_word:
                        node.is_word = False
                        node.meaning = ""

                    if all(child is None for child in node.children):
                        return None
                else:
                    index = self.char_to_index(word[depth])
                    node.children[index] = delete_recursive(node.children[index], word, depth + 1)

                    if all(child is None for child in node.children) and not node.is_word:
                        return None

            return node

        self.root = delete_recursive(self.root, word, 0)

    """ O(word.size) """
    def change_meaning(self, word, new_meaning):
        node = self.root

        for char in word:
            index = self.char_to_index(char)

            if not node.children[index]:
                return False

            node = node.children[index]

        if node.is_word:
            node.meaning = new_meaning
            return True

        return False

    """ O(word.size) """
    def find_with_prefix(self, prifix):
        def collect_words_with_prefix(node, current_word, words):
            if node.is_word:
                words.append(current_word)

            for i, child in enumerate(node.children):
                if child:
                    collect_words_with_prefix(child, current_word + chr(i + ord('a')), words)
        
        node = self.root

        for char in prifix:
            index = self.char_to_index(char)

            if not node.children[index]:
                return []

            node = node.children[index]

        words = []
        collect_words_with_prefix(node, prifix, words)
        return words
 
    def show_all_words(self):
        def show_recursive(node, current_word):
            if node.is_word:
                print(current_word, ":", node.meaning)

            for i, child in enumerate(node.children):
                if child:
                    show_recursive(child, current_word + chr(i + ord('a')))

        show_recursive(self.root, "")
