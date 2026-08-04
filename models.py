from datetime import datetime

from database import db


class Chamado(db.Model):
    __tablename__ = "chamados"

    id = db.Column(db.Integer, primary_key=True)

    titulo = db.Column(db.String(120), nullable=False)

    descricao = db.Column(db.Text, nullable=False)

    categoria = db.Column(db.String(50), nullable=False)

    prioridade = db.Column(db.String(20), nullable=False)

    status = db.Column(
        db.String(20),
        nullable=False,
        default="Aberto"
    )

    solicitante = db.Column(db.String(100), nullable=False)

    tecnico = db.Column(db.String(100))

    data_abertura = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    data_fechamento = db.Column(
        db.DateTime
    )