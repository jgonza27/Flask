from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from aplicacion.app import app
from aplicacion.models import Usuarios

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    """Carga un usuario desde la base de datos por su ID"""
    return Usuarios.query.get(int(user_id))