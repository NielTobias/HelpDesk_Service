from flask import Blueprint, jsonify

from models.chamado import Chamado


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