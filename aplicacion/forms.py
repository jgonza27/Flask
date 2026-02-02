from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DecimalField, IntegerField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField

class formCategoria(FlaskForm):
    nombre = StringField("Nombre:", validators=[DataRequired("Tienes que introducir el dato")])
    submit = SubmitField('Enviar')

class formArticulo(FlaskForm):
    nombre = StringField("Nombre:", validators=[DataRequired("Tienes que introducir el dato")])
    precio = DecimalField("Precio:", validators=[DataRequired("Tienes que introducir el dato")])
    iva = IntegerField("IVA:", validators=[DataRequired("Tienes que introducir el dato")])
    descripcion = TextAreaField("Descripción:", validators=[DataRequired("Tienes que introducir el dato")])
    photo = FileField("Imagen:")
    stock = IntegerField("Stock:", validators=[DataRequired("Tienes que introducir el dato")])
    CategoriaId = SelectField("Categoría:", coerce=int, validators=[DataRequired("Tienes que introducir el dato")])
    submit = SubmitField('Enviar')

class formSINO(FlaskForm):
    si = SubmitField('Si')
    no = SubmitField('No')

class LoginForm(FlaskForm):
    username = StringField("Login", validators=[DataRequired("Tienes que introducir el dato")])
    password = PasswordField("Password", validators=[DataRequired("Tienes que introducir el dato")])
    submit = SubmitField('Entrar')