from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/page1")
def page1():
    return "Esta es la página 1."

@app.route("/page2")
def page2():
    return render_template("pag1.html")


if __name__ == "__main__":
    app.run(debug=True,port=5000)