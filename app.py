from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/<path:url>")
def home(url='/'):
    return "This is the home page. Your URL is: %s " % url

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    return "%s + %s = %s" % (a, b, a + b)


@app.route('/about')
def about():
    return "This is the about page!"

if __name__ == "__main__":
    app.run()
