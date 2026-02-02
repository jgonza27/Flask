from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class formCategoria(FlaskForm):
    nombre = StringField("Nombre:", validators=[DataRequired("Tienes que introducir el dato")])
    submit = SubmitField('Enviar')

class formArticulo(FlaskForm):
    nombre = StringField("Nombre:", validators=[DataRequired("Tienes que introducir el dato")])
    precio = StringField("Precio:", validators=[DataRequired("Tienes que introducir el dato")])
    iva = StringField("IVA:", validators=[DataRequired("Tienes que introducir el dato")])
    descripcion = StringField("Descripción:", validators=[DataRequired("Tienes que introducir el dato")])
    photo = StringField("Imagen:")
    stock = StringField("Stock:", validators=[DataRequired("Tienes que introducir el dato")])
    CategoriaId = StringField("Categoría:", validators=[DataRequired("Tienes que introducir el dato")])
    submit = SubmitField('Enviar')

class formSINO(FlaskForm):
    si = SubmitField('Si')
    no = SubmitField('No')

class LoginForm(FlaskForm):
    username = StringField("Login", validators=[DataRequired("Tienes que introducir el dato")])
    password = PasswordField("Password", validators=[DataRequired("Tienes que introducir el dato")])
    submit = SubmitField('Entrar')