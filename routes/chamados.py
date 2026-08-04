from flask import Blueprint, render_template

chamados_bp = Blueprint(
    "chamados",
    __name__
)


@chamados_bp.route("/")
def home():
    return render_template("index.html")


@chamados_bp.route("/chamados")
def chamados():

    return render_template("chamados.html")