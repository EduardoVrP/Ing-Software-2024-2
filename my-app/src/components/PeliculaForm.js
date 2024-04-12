import React, { useState, useEffect } from 'react';
import './PeliculaForm.css';

const PeliculaForm = ({ onSubmit, editingPelicula, onUpdate, onCancelEdit }) => {
  const [pelicula, setPelicula] = useState({
    nombre: '',
    genero: '',
    duracion: 0,
    inventario: 1,
  });

  useEffect(() => {
    if (editingPelicula) {
      setPelicula(editingPelicula);
    } else {
      setPelicula({
        nombre: '',
        genero: '',
        duracion: 0,
        inventario: 1,
      });
    }
  }, [editingPelicula]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setPelicula((prevPelicula) => ({
      ...prevPelicula,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (editingPelicula) {
      onUpdate(pelicula);
    } else {
      onSubmit(pelicula);
    }
    setPelicula({
      nombre: '',
      genero: '',
      duracion: 0,
      inventario: 1,
    });
  };

  return (
    <div className="pelicula-form-container">
      <h2>{editingPelicula ? 'Editar Película' : 'Agregar Película'}</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" name="nombre" placeholder="Nombre" value={pelicula.nombre} onChange={handleChange} required />
        <input type="text" name="genero" placeholder="Género" value={pelicula.genero} onChange={handleChange} />
        <input type="number" name="duracion" placeholder="Duración (minutos)" value={pelicula.duracion} onChange={handleChange} required />
        <input type="number" name="inventario" placeholder="Inventario" value={pelicula.inventario} onChange={handleChange} required />
        <div>
          <button type="submit">{editingPelicula ? 'Actualizar' : 'Agregar'}</button>
          {editingPelicula && <button type="button" onClick={onCancelEdit}>Cancelar</button>}
        </div>
      </form>
    </div>
  );
};

export default PeliculaForm;
