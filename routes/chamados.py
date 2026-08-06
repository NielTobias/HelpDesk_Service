from flask import Blueprint, render_template
from flask_login import login_required
from models.chamado import Chamado

chamados_bp = Blueprint(
    "chamados",
    __name__
)


@chamados_bp.route("/")
def home():
    return render_template("home/index.html")


@chamados_bp.route("/chamados")
@login_required
def listar_chamados():

    chamados = Chamado.query.order_by(
        Chamado.data_abertura.desc()
    ).all()

    return render_template(
        "chamados/listar.html",
        chamados=chamados
    )


@chamados_bp.route("/chamados/novo")
@login_required
def novo_chamado():
    return render_template("chamados/novo.html")


@chamados_bp.route("/chamados/editar/<int:id>")
@login_required
def editar_chamado(id):
    return render_template(
        "chamados/editar.html",
        id=id
    )