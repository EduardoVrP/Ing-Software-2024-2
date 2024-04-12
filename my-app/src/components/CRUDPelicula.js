import React, { useState, useEffect } from 'react';
import './CRUDPelicula.css';
import PeliculaForm from './PeliculaForm';

const CRUDPelicula = () => {
  const [peliculas, setPeliculas] = useState([]);
  const [editingPelicula, setEditingPelicula] = useState(null);

  useEffect(() => {
    fetchPeliculas();
  }, []);

  const fetchPeliculas = async () => {
    try {
      const response = await fetch('http://localhost:3000/api/peliculas');
      const data = await response.json();
      setPeliculas(data);
    } catch (error) {
      console.error('Error fetching películas: ', error);
    }
  };

  const addPelicula = async (pelicula) => {
    try {
      await fetch('http://localhost:3000/api/peliculas', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(pelicula),
      });
      fetchPeliculas();
    } catch (error) {
      console.error('Error adding película: ', error);
    }
  };

  const deletePelicula = async (idPelicula) => {
    try {
      await fetch(`http://localhost:3000/api/peliculas/${idPelicula}`, {
        method: 'DELETE',
      });
      fetchPeliculas();
    } catch (error) {
      console.error('Error deleting película: ', error);
    }
  };

  const updatePelicula = async (updatedPelicula) => {
    try {
      await fetch(`http://localhost:3000/api/peliculas/${updatedPelicula.idPelicula}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedPelicula),
      });
      fetchPeliculas();
      setEditingPelicula(null);
    } catch (error) {
      console.error('Error updating película: ', error);
    }
  };

  const editPelicula = (pelicula) => {
    setEditingPelicula(pelicula);
  };

  const cancelEdit = () => {
    setEditingPelicula(null);
  };

  return (
    <div className="crud-pelicula-container">
      <h1>Películas</h1>
      <PeliculaForm onSubmit={addPelicula} editingPelicula={editingPelicula} onUpdate={updatePelicula} onCancelEdit={cancelEdit} />
      <div className="peliculas-list">
        {peliculas.map((pelicula) => (
          <div key={pelicula.idPelicula} className="pelicula-item">
            <p>{pelicula.nombre}</p>
            <p>Género: {pelicula.genero}</p>
            <p>Duración: {pelicula.duracion} minutos</p>
            <p>Inventario: {pelicula.inventario}</p>
            <div className="pelicula-buttons">
              <button onClick={() => editPelicula(pelicula)}>Editar</button>
              <button onClick={() => deletePelicula(pelicula.idPelicula)}>Eliminar</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default CRUDPelicula;
