from flask import Flask

app = Flask(__name__)

@app.route("/")
def first():
    return f"Bu dizin kök dizinidir"

@app.route("/second")
def second():
    return f"This is second page"

@app.route("/forth/152")
def sub():
    return f"this is the subpage of fourth page"

@app.route("/fifth/<string:id>")
def forth(id):
    return f"Id of this page is {id}"

if __name__ == "__main__":
    app.run(debug = True)