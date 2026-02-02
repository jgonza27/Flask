from flask_login import LoginManager
from aplicacion.models import Usuarios

login_manager = LoginManager()
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    """Carga un usuario desde la base de datos por su ID"""
    return Usuarios.query.get(int(user_id))