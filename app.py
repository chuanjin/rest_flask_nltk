from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/<path:path>")
def home(path=''):
    return "Welcome!"

if __name__ == "__main__":
    app.run()
