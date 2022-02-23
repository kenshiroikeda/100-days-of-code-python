from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://images.pexels.com/photos/479009/pexels-photo-479009.jpeg?cs=srgb&dl=pexels-danielle-daniel-479009.jpg&fm=jpg" width="200">'


@app.route('/bye')
def day_bye():
    return 'Bye'


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello, {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)