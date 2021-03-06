import random

from flask import Flask
app = Flask(__name__)


@app.route('/')
def start_game():
    return "<h1>Guess the number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route('/<int:number>')
def judge(number):
    if number > answer:
        return f"<h1 style='color: purple;'>Too High, try again!!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif number < answer:
        return f"<h1 style='color: red;'>Too Low, try again!!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return f"<h1 style='color: green;'>You found me!!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


answer = random.randint(0, 9)

if __name__ == "__main__":
    app.run(debug=True)