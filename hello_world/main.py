from flask import Flask
from flask import render_template

app = Flask("Hello")


@app.route("/hello")
def hello():
    return render_template('hello.html', name="Kerry")

@app.route("/hello/<name>")
def hello2(name):
    return render_template("hello.html", name=name)
6


@app.route("/test")
def test():
    return "sucess"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
