from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin  # <--- Importante

db = SQLAlchemy()

class Usuarios(db.Model, UserMixin):  # <--- Heredamos de UserMixin
    """Tabla de usuarios para la gestión de acceso"""
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    admin = Column(Boolean, default=False)

    def __repr__(self):
        return f'<Usuarios: {self.username}>'

class Categorias(db.Model):
    """Categorías de los artículos"""
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    articulos = relationship(
        "Articulos",
        cascade="all, delete-orphan",
        back_populates="categoria",
        lazy='dynamic'
    )

    def __repr__(self):
        return f'<Categorias:  {self.id}>'

class Articulos(db.Model):
    """Artículos de nuestra tienda"""
    __tablename__ = 'articulos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    precio = Column(Float, default=0)
    iva = Column(Integer, default=21)
    descripcion = Column(String(255))
    image = Column(String(255))
    stock = Column(Integer, default=0)
    CategoriaId = Column(Integer, ForeignKey('categorias.id'), nullable=False)
    categoria = relationship("Categorias", back_populates="articulos")

    def precio_final(self):
        return self.precio + (self.precio * self.iva / 100)

    def __repr__(self):
        return f'<Articulos: {self.id}>'