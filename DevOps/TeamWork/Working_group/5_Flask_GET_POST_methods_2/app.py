from flask import Flask, request, render_template

app = Flask(__name__)

def lcm(num1,num2):
    return min([i for i in range(min(num1, num2),num1*num2+1) if i%num1==0 and i%num2==0 ])

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calc", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        num1 = request.form["number1"]
        num2 = request.form.get("number2")
        return render_template("result.html", num1 = num1, num2 = num2, lcm = lcm(int(num1),int(num2)))
    else:
        return render_template("result.html")

if __name__== "__main__":
    app.run(debug=True)