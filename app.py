from flask import Flask
from flask_login import LoginManager
from flask_login import login_required

from config import Config
from database import db

from routes.chamados import chamados_bp
from models.usuario import Usuario

from routes.auth import auth_bp

import models

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth.login"
login_manager.login_message = "Faça login para acessar o sistema."
login_manager.login_message_category = "warning"


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))


app.register_blueprint(chamados_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)