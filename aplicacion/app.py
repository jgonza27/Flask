from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from aplicacion import config

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config.from_object(config)

# ImportError: cannot import name 'db' from partially initialized module 'aplicacion.app'
# (most likely due to a circular import)
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy(app)

from aplicacion.models import Articulos, Categorias, db
db.init_app(app)


@app.route('/')
@app.route('/categoria/<id>')
def inicio(id='0'):
    categoria = Categorias.query.get(id)
    if id == '0':
        articulos = Articulos.query.all()
    else:
        articulos = Articulos.query.filter_by(CategoriaId=id)

    categorias = Categorias.query.all()
    return render_template(
        "inicio.html",
        articulos=articulos,
        categorias=categorias,
        categoria=categoria
    )


@app.route('/categorias')
def categorias():
    categorias = Categorias.query.all()
    return render_template("categorias.html", categorias=categorias)


@app.errorhandler(404)
def page_not_found(error):
    return render_template(
        "error.html",
        error="Página no encontrada..."
    ), 404
