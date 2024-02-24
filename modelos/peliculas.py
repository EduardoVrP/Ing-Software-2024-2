from sqlalchemy import Column, Integer, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from alchemyClasses import db
Base = declarative_base()

class Pelicula(db.Model):
    __tablename__ = 'peliculas'

    idPelicula = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    genero = Column(String(45))
    duracion = Column(Integer)
    inventario = Column(Integer, default=1)

    # Definir la relación con la tabla "rentar" si es necesario
    rentas = relationship("Rentar", back_populates="pelicula")

    def __str__(self):
        return f'Pelicula(idPelicula={self.idPelicula}, nombre="{self.nombre}", genero="{self.genero}", duracion={self.duracion}, inventario={self.inventario})'