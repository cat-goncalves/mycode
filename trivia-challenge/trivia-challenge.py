#!/usr/bin/env python3

from random import randint
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app= Flask(__name__)

questions= [
    {
        "question": "How many legs does a spider have?",
        "answer": "Eight",
    },
    { 
        "question" : "What is the name of the toy cowboy in Toy Story?",
        "answer": "Woody"
    },
    {
        "question" : "What is the color of an emerald?",
        "answer" : "Green"
    },
    {
        "question" : "If you freeze water, what do you get?",
        "answer" : "Ice"
    }]

@app.route("/")
def index():
    # jsonify returns legal JSON
    # return jsonify(questions)
    q = questions[randint(1, len(questions))]
    print({q["question"]})
    return render_template("index.html", question = q["question"])

@app.route("/<answer>")
def guess():
    return

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
