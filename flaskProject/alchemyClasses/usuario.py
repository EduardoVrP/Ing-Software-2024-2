from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from alchemyClasses import db
from alchemyClasses.rentar import Rentar

Base = declarative_base()

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    apPat = Column(String(200), nullable=False)
    apMat = Column(String(200))
    password = Column(String(64), nullable=False)
    email = Column(String(500), unique=True)
    profilePicture = Column(String)  # Aquí podrías usar un tipo adecuado para almacenar imágenes (dependiendo de cómo las almacenes en tu base de datos)
    superUser = Column(Boolean)

    # Relaciones
    rentas = relationship("Rentar", back_populates="usuario")

    def __str__(self):
        return f"ID: {self.idUsuario}, Nombre: {self.nombre}, Apellido Paterno: {self.apPat}, Apellido Materno: {self.apMat}, Email: {self.email}, Super Usuario: {self.superUser}"
