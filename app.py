from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chamados")
def chamados():
    return render_template("chamados.html")


@app.route("/dashboard")
def dashboard():
    return "<h1>Dashboard em construção</h1>"


if __name__ == "__main__":
    app.run(debug=True)