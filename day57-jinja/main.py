import datetime
import requests
from flask import Flask, render_template

app = Flask(__name__)


def judge_gender(name):
    res = requests.get("https://api.genderize.io/?name="+name)
    return res.json()["gender"]


def judge_age(name):
    res = requests.get("https://api.agify.io?name=" + name)
    return res.json()["age"]


@app.route('/')
def home():
    return render_template("index.html", current_year=datetime.datetime.now().year)


@app.route('/guess/<string:user_name>')
def guess(user_name):
    gender = judge_gender(user_name)
    age = judge_age(user_name)
    return render_template("index.html", user_name=user_name, age=age, gender=gender,
                           current_year=datetime.datetime.now().year)


if __name__ == "__main__":
    app.run(debug=True)


