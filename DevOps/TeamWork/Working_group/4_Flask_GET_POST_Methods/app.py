from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/multp" , methods = ["GET", "POST"])
def multiplication():
    if request.method == "POST":
        value1 = request.form.get("value1")
        value2 = request.form.get("value2")
        return render_template("number.html", multp = int(value1)*int(value2))
    else:
        return render_template("number.html")

if __name__== "__main__":
    app.run(debug = True)
