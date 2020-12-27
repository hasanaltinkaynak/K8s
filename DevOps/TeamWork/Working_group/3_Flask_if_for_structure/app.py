from flask import Flask, render_template

app = Flask(__name__)

#@app.route("/")
#def head():
#    names = ["Ummuhan", "Hasan", "Sibel", "Fatmanur", #"Edip"]
#    return render_template("index.html", isimler = names)

@app.route("/")
def head():
    dinleyen = "Tulay"
    return render_template("index.html", listener = dinleyen)

if __name__== "__main__":
    app.run(debug = True)