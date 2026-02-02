from flask import session
from flask_login import LoginManager
from aplicacion.models import Usuarios

login_manager = LoginManager()
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return Usuarios.query.get(int(user_id))

def login_user(Usuario):
    session["id"] = Usuario.id
    session["username"] = Usuario.username
    session["admin"] = Usuario.admin

def logout_user():
    session.pop("id", None)
    session.pop("username", None)
    session.pop("admin", None)