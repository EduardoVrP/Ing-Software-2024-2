from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from alchemyClasses import db
Base = declarative_base()

class Rentar(db.Model):
    __tablename__ = 'rentar'

    idRentar = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'), nullable=False)
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'), nullable=False)
    fecha_renta = Column(DateTime, nullable=False)
    dias_de_renta = Column(Integer, default=5)
    estatus = Column(Integer, default=0)

    # Definir las relaciones inversas
    usuario = relationship("Usuario", back_populates="rentas")
    pelicula = relationship("Pelicula", back_populates="rentas")

    def __str__(self):
        return f'Rentar(idRentar={self.idRentar}, idUsuario={self.idUsuario}, idPelicula={self.idPelicula}, fecha_renta={self.fecha_renta}, dias_de_renta={self.dias_de_renta}, estatus={self.estatus})'