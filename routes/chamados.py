from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

from database import db
from models.chamado import Chamado


chamados_bp = Blueprint(
    "chamados",
    __name__
)


# ==========================================
# HOME
# ==========================================

@chamados_bp.route("/")
def home():

    return render_template(
        "home/index.html"
    )


# ==========================================
# LISTAR E PESQUISAR CHAMADOS
# ==========================================

@chamados_bp.route("/chamados")
@login_required
def listar_chamados():

    pesquisa = request.args.get(
        "pesquisa",
        ""
    )

    consulta = Chamado.query

    if pesquisa:

        consulta = consulta.filter(
            Chamado.titulo.ilike(
                f"%{pesquisa}%"
            )
        )

    chamados = consulta.order_by(
        Chamado.data_abertura.desc()
    ).all()

    return render_template(
        "chamados/listar.html",
        chamados=chamados,
        pesquisa=pesquisa
    )


# ==========================================
# NOVO CHAMADO
# ==========================================

@chamados_bp.route(
    "/chamados/novo",
    methods=["GET", "POST"]
)
@login_required
def novo_chamado():

    if request.method == "POST":

        chamado = Chamado(
            titulo=request.form["titulo"],
            descricao=request.form["descricao"],
            categoria=request.form["categoria"],
            prioridade=request.form["prioridade"],
            status="Aberto",
            solicitante=request.form["solicitante"],
            tecnico=request.form.get("tecnico")
        )

        db.session.add(chamado)

        db.session.commit()

        flash(
            "Chamado criado com sucesso!",
            "success"
        )

        return redirect(
            url_for(
                "chamados.listar_chamados"
            )
        )

    return render_template(
        "chamados/novo.html"
    )


# ==========================================
# EDITAR CHAMADO
# ==========================================

@chamados_bp.route(
    "/chamados/editar/<int:id>",
    methods=["GET", "POST"]
)
@login_required
def editar_chamado(id):

    chamado = Chamado.query.get_or_404(id)

    if request.method == "POST":

        chamado.titulo = request.form["titulo"]

        chamado.descricao = request.form["descricao"]

        chamado.categoria = request.form["categoria"]

        chamado.prioridade = request.form["prioridade"]

        chamado.status = request.form["status"]

        chamado.tecnico = request.form["tecnico"]

        db.session.commit()

        flash(
            "Chamado atualizado com sucesso!",
            "success"
        )

        return redirect(
            url_for(
                "chamados.listar_chamados"
            )
        )

    return render_template(
        "chamados/editar.html",
        chamado=chamado
    )


# ==========================================
# EXCLUIR CHAMADO
# ==========================================

@chamados_bp.route(
    "/chamados/excluir/<int:id>",
    methods=["POST"]
)
@login_required
def excluir_chamado(id):

    chamado = Chamado.query.get_or_404(id)

    db.session.delete(chamado)

    db.session.commit()

    flash(
        "Chamado excluído com sucesso!",
        "success"
    )

    return redirect(
        url_for(
            "chamados.listar_chamados"
        )
    )