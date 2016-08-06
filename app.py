from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route("/")
@app.route("/<path:url>")
def home(url='/'):
    return "This is the home page. Your URL is: %s " % url


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return "%s + %s = %s" % (a, b, a + b)


@app.route('/about')
def about():
    return "This is the about page!"


@app.route('/text', methods=['GET'])
def text():
    return render_template('text.html', title="Text")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
