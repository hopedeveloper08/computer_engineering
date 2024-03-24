from flask import Flask, render_template, request
from trie import Trie


app = Flask(__name__)

trie = Trie()
with open("input.txt", 'r') as f:
    for data in f.read().split('\n'):
        trie.insert_new_word(*data.split(','))


def trie_to_dict(node):
    result = {"meaning": node.meaning, "children": []}
    for i, child in enumerate(node.children):
        if child:
            child_dict = trie_to_dict(child)
            child_dict["char"] = chr(i + ord('a'))
            result["children"].append(child_dict)

    return result

@app.route('/')
def index():
    trie.show_all_words()
    trie_dict = trie_to_dict(trie.root)
    return render_template('index.html', trie=trie_dict)

@app.route('/insert', methods=['POST'])
def insert_word():
    word = request.form['word']
    meaning = request.form['meaning']
    if word.isalpha():
        trie.insert_new_word(word, meaning)

    trie_dict = trie_to_dict(trie.root)
    return render_template('index.html', trie=trie_dict)

@app.route('/delete', methods=['POST'])
def delete_word():
    word = request.form['word']
    if word.isalpha():
        trie.delete_word(word)
        
    trie_dict = trie_to_dict(trie.root)
    return render_template('index.html', trie=trie_dict)

@app.route('/search', methods=['POST'])
def search_meaning():
    word = request.form['word']
    if word.isalpha():
        meaning = trie.search_meaning(word)

    trie_dict = trie_to_dict(trie.root)
    return render_template('index.html', trie=trie_dict, search_result=meaning)

@app.route('/change', methods=['POST'])
def change_meaning():
    word = request.form['word']
    if word.isalpha():
        new_meaning = request.form['new_meaning']
        success = trie.change_meaning(word, new_meaning)

    trie_dict = trie_to_dict(trie.root)
    return render_template('index.html', trie=trie_dict, change_result=success)

@app.route('/find', methods=['POST'])
def find_with_prefix():
    prefix = request.form['prefix']
    if prefix.isalpha():
        words = trie.find_with_prefix(prefix)

    trie_dict = trie_to_dict(trie.root)
    return render_template('index.html', trie=trie_dict, find_result=words)

    
if __name__ == '__main__':
    app.run(debug=True)
