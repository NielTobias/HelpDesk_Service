from flask import Blueprint, render_template, request, redirect, url_for, flash

from flask_login import login_user, logout_user, login_required

from models.usuario import Usuario

auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]

        senha = request.form["senha"]

        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and usuario.verificar_senha(senha):

            login_user(usuario)

            return redirect(url_for("chamados.home"))

        flash("E-mail ou senha inválidos.", "danger")

    return render_template("auth/login.html")


@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(url_for("auth.login"))