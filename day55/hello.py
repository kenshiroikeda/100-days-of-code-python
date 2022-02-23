from flask import Flask
app = Flask(__name__)


def make_bold(fun):
    def wrapper_function():
        html_str = '<b>' + fun() + '</b>'
        return html_str
    return wrapper_function


def make_emphasis(fun):
    def wrapper_function():
        html_str = '<em>' + fun() + '</em>'
        return html_str
    return wrapper_function


def make_underlined(fun):
    def wrapper_function():
        html_str = '<u>' + fun() + '</u>'
        return html_str
    return wrapper_function



@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://images.pexels.com/photos/479009/pexels-photo-479009.jpeg?cs=srgb&dl=pexels-danielle-daniel-479009.jpg&fm=jpg" width="200">'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def day_bye():
    return 'Bye'


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello, {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)