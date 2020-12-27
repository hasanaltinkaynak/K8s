from flask import Flask, render_template

app = Flask(__name__)

def toplam(num1,num2):
    return num1+num2

number1 = 12
number2 = 34
@app.route("/")
def head():
    return render_template("index.html", number1 = 12, number2=34, toplam = toplam(number1,number2))

if __name__== "__main__":
    app.run(debug = True)