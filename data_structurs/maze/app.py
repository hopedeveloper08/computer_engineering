from flask import Flask, render_template, request
from model import Maze
import random


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def menu():
    if request.method == 'POST':
        n = int(request.form["size"])
        if n:
            maze = list()
            for _ in range(n):
                maze.append(['0'] * n)
            walls = list(request.form.keys())
            walls.pop(0)
            for i in walls:
                d, m = divmod(int(i), n)
                maze[d][m] = '1'

            with open("maze.txt", 'w') as f:
                for i in maze:
                    f.writelines(' '.join(i))
                    f.write("\n")

    return render_template('home.html')


@app.route('/random/<n>', methods=['GET'])
def random_maze(n):
    n = int(n)
    maze = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(random.choices(['0', '1'], weights=[60, 40], k=1).pop())
        maze.append(temp)

    with open("maze.txt", 'w') as f:
        for i in maze:
            f.writelines(' '.join(i))
            f.write("\n")

    return render_template("home.html")


@app.route('/create', methods=['POST', 'GET'])
def create_maze():
    return render_template('create.html')


@app.route('/solution', methods=['GET'])
def solution():
    with open("location.txt") as f:
        loc = f.read().split('\n')
        s = [int(loc[0]), int(loc[1])]
        f = [int(loc[2]), int(loc[3])]
        method = "normal"
        if len(loc) != 5:
            method = "horse"

    maze = Maze(start=s, finish=f, move=method)
    print(maze.path)
    return render_template("solution.html", path=maze.path, maze=maze.maze)


@app.route('/show', methods=['GET'])
def show_maze():
    with open("maze.txt") as f:
        temp = f.read().split("\n")

    maze = []
    for row in range(len(temp)):
        maze.append(temp[row].split(' '))

    return render_template("show.html", maze=maze)


@app.route('/location', methods=['GET', 'POST'])
def set_location():
    if request.method == 'POST':
        with open("location.txt", 'w') as f:
            for i in request.form.values():
                f.write(f"{i}\n")

        return render_template("home.html")

    return render_template("location.html")


if __name__ == '__main__':
    app.run()
