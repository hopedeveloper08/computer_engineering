from flask import Flask, render_template, request
from model import tournaments_schedule, print_table


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def schedule():
    data = dict()
    if request.method == 'POST':
        number_of_teams = int(request.form['number_of_teams'])
        table = tournaments_schedule(number_of_teams)
        print_table(table)
        data = table

    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
