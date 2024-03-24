from flask import Flask, render_template, request, redirect, url_for
from models.linkedlist_sparse_matrix import LLSparseMatrix


app = Flask(__name__)
matrix1 = LLSparseMatrix()
matrix2 = LLSparseMatrix()
matrix1.load_matrix()
matrix2.load_matrix()


def data(matrix):
    matrix_terms = list()
    for node in matrix.head_nodes:
        rp = node.right
        while rp:
            obj = {"row": rp.row, "col": rp.col, "value": rp.value}
            rp = rp.right
            matrix_terms.append(obj)

    return matrix_terms


@app.route('/')
def index():
    matrix_terms1 = data(matrix1)
    matrix_terms2 = data(matrix2)

    return render_template('index.html', matrix_terms1=matrix_terms1, matrix_terms2=matrix_terms2)


@app.route('/add_term', methods=['POST'])
def add_term():
    row = int(request.form['row'])
    col = int(request.form['col'])
    value = int(request.form['value'])
    if request.form['obj'] == '1':
        matrix1.add_term(row, col, value)
        matrix1.convert_and_print(1)
    else:
        matrix2.add_term(row, col, value)
        matrix2.convert_and_print(2)

    return redirect(url_for('index'))


@app.route('/remove_term/<int:obj>/<int:row>/<int:col>')
def remove_term(row, col, obj):
    if obj == 1:
        matrix1.remove_term(row, col)
        matrix1.convert_and_print(1)
    else:
        matrix2.remove_term(row, col)
        matrix2.convert_and_print(1)

    return redirect(url_for('index'))


@app.route('/operation/<int:obj>/<operation>', methods=['POST'])
def perform_operation(operation, obj):
    if obj == 1:
        if operation == 'add':
            matrix1.add_matrix(matrix2)
        elif operation == 'subtract':
            matrix1.subtract_matrix(matrix2)
        elif operation == 'multiply':
            matrix1.multiply_matrix(matrix2)
        elif operation == 'transpose':
            matrix1.transpose()
        matrix1.convert_and_print(1)
    else:
        if operation == 'add':
            matrix2.add_matrix(matrix1)
        elif operation == 'subtract':
            matrix2.subtract_matrix(matrix1)
        elif operation == 'multiply':
            matrix2.multiply_matrix(matrix1)
        elif operation == 'transpose':
            matrix2.transpose()
        matrix2.convert_and_print(2)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
