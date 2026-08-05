from app import app
from database import db
from models.usuario import Usuario

with app.app_context():

    usuario = Usuario(
        nome="Administrador",
        email="admin@helpdesk.com"
    )

    usuario.definir_senha("123456")

    db.session.add(usuario)
    db.session.commit()

    print("Usuário administrador criado!")