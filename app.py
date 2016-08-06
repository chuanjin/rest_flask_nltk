from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import re
import nltk
from collections import Counter



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


@app.route('/text', methods=['GET', 'POST'])
def text():
    results = {}
    if request.method == 'POST':
        raw = request.form.get('text')
        nltk.data.path.append('./nltk_data/')  # set the path
        print raw
        tokens = nltk.word_tokenize(raw)
        text = nltk.Text(tokens)
        nonPunct = re.compile('.*[A-Za-z0-9].*')
        filtered = [w for w in text if nonPunct.match(w)]
        results = Counter(filtered).items()
    return render_template('text.html', title="Text", results=results)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
