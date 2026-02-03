from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, PasswordField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField

class formArticulo(FlaskForm):
    nombre = StringField("Nombre:", validators=[DataRequired("Tienes que introducir el dato")])
    precio = DecimalField("Precio:", validators=[DataRequired("Tienes que introducir el dato")])
    iva = IntegerField("IVA:", validators=[DataRequired("Tienes que introducir el dato")])
    descripcion = TextAreaField("Descripción:", validators=[DataRequired("Tienes que introducir el dato")])
    photo = FileField("Imagen:")
    stock = IntegerField("Stock:", validators=[DataRequired("Tienes que introducir el dato")])
    CategoriaId = SelectField("Categoría:", coerce=int, validators=[DataRequired("Tienes que introducir el dato")])
    submit = SubmitField('Enviar')

class formCategoria(FlaskForm):
    nombre = StringField("Nombre:", validators=[DataRequired("Tienes que introducir el dato")])
    submit = SubmitField('Enviar')

class formSINO(FlaskForm):
    si = SubmitField('Si')
    no = SubmitField('No')

class LoginForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Entrar')

class formUsuario(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    nombre = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Registrar')
