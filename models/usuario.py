from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from database import db


class Usuario(UserMixin, db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(
        db.String(120),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )   # Nunca armazenamos a senha em texto puro.
        # Apenas o hash gerado pelo Werkzeug.
    senha_hash = db.Column(
        db.String(255),
        nullable=False
    )

    perfil = db.Column(
        db.String(30),
        default="usuario"
    )

    ativo = db.Column(
        db.Boolean,
        default=True
    )

    criado_em = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def definir_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

    def __repr__(self):
        return f"<Usuario {self.email}>"