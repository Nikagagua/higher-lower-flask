from flask import Flask
from random import randint

app = Flask(__name__)

random_number = randint(0, 9)


@app.route('/')
def home_page():
    return "<h1>Guess a number between '0' and '9'!</h1>" \
           "<img src='https://media.giphy.com/media/l0ExncehJzexFpRHq/giphy.gif' width=480 height=480>"


@app.route('/<int:number>')
def guess_number(number):
    if number > random_number:
        return f"<h2 style='color: purple'>Too High, try again!</h2>" \
               f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif number < random_number:
        return f"<h2 style='color: red'>Too Low, try again!</h2>" \
               f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return f"<h2 style='color: green'>You got it!</h2>" \
               f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
