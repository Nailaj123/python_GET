from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "hello flask!"
    # return flask.render_template("index.html", token="hello Flask+React")
# app.run(debug=True)
