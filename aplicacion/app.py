from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from aplicacion import config
from aplicacion.models import Articulos, Categorias, db
from aplicacion.forms import formArticulo, formCategoria

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

@app.route('/articulos/new', methods=["get", "post"])
def articulos_new():
    form = formArticulo()
    # Consultamos las categorías para el desplegable del formulario
    categorias = [(c.id, c.nombre) for c in Categorias.query.all()]
    form.CategoriaId.choices = categorias
    
    if form.validate_on_submit():
        try:
            f = form.photo.data
            nombre_fichero = secure_filename(f.filename)
            f.save(app.root_path + "/static/img/" + nombre_fichero)
        except:
            nombre_fichero = ""
            
        art = Articulos()
        form.populate_obj(art)
        art.image = nombre_fichero
        
        db.session.add(art)
        db.session.commit()
        
        return redirect(url_for("inicio"))
    else:
        return render_template("articulos_new.html", form=form)
    
@app.route('/categorias/new', methods=["get", "post"])
def categorias_new():
    form=formCategoria(request.form)
    if form.validate_on_submit():
        cat=Categorias(nombre=form.nombre.data)
        db.session.add(cat)
        db.session.commit()
        return redirect(url_for("categorias"))
    else:
        return render_template("categorias_new.html",form=form)
    