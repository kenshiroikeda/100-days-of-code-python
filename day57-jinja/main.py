import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", current_year=datetime.datetime.now().year)


if __name__ == "__main__":
    app.run(debug=True)


