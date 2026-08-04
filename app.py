from flask import Flask

from config import Config
from database import db
from routes.chamados import chamados_bp

import models


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(chamados_bp)

    return app


app = create_app()

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)