from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

from database import db
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


@chamados_bp.route("/chamados/novo", methods=["GET", "POST"])
@login_required
def novo_chamado():

    if request.method == "POST":

        chamado = Chamado(
            titulo=request.form["titulo"],
            descricao=request.form["descricao"],
            categoria=request.form["categoria"],
            prioridade=request.form["prioridade"],
            solicitante=request.form["solicitante"]
        )

        db.session.add(chamado)
        db.session.commit()

        flash("Chamado criado com sucesso!", "success")

        return redirect(url_for("chamados.listar_chamados"))

    return render_template("chamados/novo.html")


@chamados_bp.route("/chamados/editar/<int:id>")
@login_required
def editar_chamado(id):
    return render_template(
        "chamados/editar.html",
        id=id
    )