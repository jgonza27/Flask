from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from aplicacion import config
from aplicacion.models import Articulos, Categorias, db

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config.from_object(config)

db.init_app(app)

@app.route('/')
@app.route('/categoria/') 
@app.route('/categoria/<id>')
def inicio(id='0'):
    # Si la id es '0' (o nula), intentamos obtener categoría, que será None
    # pero nuestra lógica en el template ya sabe manejarlo.
    if id == '0':
        categoria = None
        articulos = Articulos.query.all()
    else:
        categoria = Categorias.query.get(id)
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