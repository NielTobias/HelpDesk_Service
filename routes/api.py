from flask import Blueprint, jsonify, request

from models.chamado import Chamado

from database import db


api_bp = Blueprint(
    "api",
    __name__,
    url_prefix="/api"
)


# ==========================================
# LISTAR TODOS OS CHAMADOS
# ==========================================

@api_bp.route("/chamados", methods=["GET"])
def listar_chamados_api():

    chamados = Chamado.query.order_by(
        Chamado.data_abertura.desc()
    ).all()

    dados = []

    for chamado in chamados:

        dados.append({
            "id": chamado.id,
            "titulo": chamado.titulo,
            "descricao": chamado.descricao,
            "categoria": chamado.categoria,
            "prioridade": chamado.prioridade,
            "status": chamado.status,
            "solicitante": chamado.solicitante,
            "tecnico": chamado.tecnico,
            "data_abertura": (
                chamado.data_abertura.isoformat()
                if chamado.data_abertura
                else None
            )
        })

    return jsonify({
        "total": len(dados),
        "chamados": dados
    })


# ==========================================
# BUSCAR UM CHAMADO
# ==========================================

@api_bp.route(
    "/chamados/<int:id>",
    methods=["GET"]
)
def buscar_chamado_api(id):

    chamado = Chamado.query.get_or_404(id)

    return jsonify({
        "id": chamado.id,
        "titulo": chamado.titulo,
        "descricao": chamado.descricao,
        "categoria": chamado.categoria,
        "prioridade": chamado.prioridade,
        "status": chamado.status,
        "solicitante": chamado.solicitante,
        "tecnico": chamado.tecnico,
        "data_abertura": (
            chamado.data_abertura.isoformat()
            if chamado.data_abertura
            else None
        )
    })

    # ==========================================
# CRIAR CHAMADO
# ==========================================

@api_bp.route(
    "/chamados",
    methods=["POST"]
)
def criar_chamado_api():

    dados = request.get_json()

    if not dados:
        return jsonify({
            "erro": "JSON não enviado."
        }), 400

    campos_obrigatorios = [
        "titulo",
        "descricao",
        "categoria",
        "prioridade",
        "solicitante"
    ]

    for campo in campos_obrigatorios:

        if campo not in dados:
            return jsonify({
                "erro": f"Campo obrigatório ausente: {campo}"
            }), 400

    chamado = Chamado(
        titulo=dados["titulo"],
        descricao=dados["descricao"],
        categoria=dados["categoria"],
        prioridade=dados["prioridade"],
        status="Aberto",
        solicitante=dados["solicitante"],
        tecnico=dados.get("tecnico")
    )

    db.session.add(chamado)
    db.session.commit()

    return jsonify({
        "mensagem": "Chamado criado com sucesso!",
        "chamado": {
            "id": chamado.id,
            "titulo": chamado.titulo,
            "descricao": chamado.descricao,
            "categoria": chamado.categoria,
            "prioridade": chamado.prioridade,
            "status": chamado.status,
            "solicitante": chamado.solicitante,
            "tecnico": chamado.tecnico
        }
    }), 201   