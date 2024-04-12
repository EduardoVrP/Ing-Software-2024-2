import React, { useState, useEffect } from 'react';
import './CRUDUsuario.css';
import UsuarioForm from './UsuarioForm';

const CRUDUsuario = () => {
  const [usuarios, setUsuarios] = useState([]);
  const [editingUser, setEditingUser] = useState(null);

  useEffect(() => {
    fetchUsuarios();
  }, []);

  const fetchUsuarios = async () => {
    try {
      const response = await fetch('API_URL/usuarios');
      const data = await response.json();
      setUsuarios(data);
    } catch (error) {
      console.error('Error fetching usuarios: ', error);
    }
  };

  const addUser = async (user) => {
    try {
      await fetch('API_URL/usuarios', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(user),
      });
      fetchUsuarios();
    } catch (error) {
      console.error('Error adding user: ', error);
    }
  };

  const deleteUser = async (idUsuario) => {
    try {
      await fetch(`API_URL/usuarios/${idUsuario}`, {
        method: 'DELETE',
      });
      fetchUsuarios();
    } catch (error) {
      console.error('Error deleting user: ', error);
    }
  };

  const updateUser = async (updatedUser) => {
    try {
      await fetch(`API_URL/usuarios/${updatedUser.idUsuario}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedUser),
      });
      fetchUsuarios();
      setEditingUser(null);
    } catch (error) {
      console.error('Error updating user: ', error);
    }
  };

  const editUser = (user) => {
    setEditingUser(user);
  };

  const cancelEdit = () => {
    setEditingUser(null);
  };


  return (
    <div className="crud-usuario-container">
      <h1>Usuarios</h1>
      <UsuarioForm onSubmit={addUser} editingUser={editingUser} onUpdate={updateUser} onCancelEdit={cancelEdit} />
      <div className="usuarios-list">
        {usuarios.map((user) => (
          <div key={user.idUsuario} className="usuario-item">
            <p>{`${user.nombre} ${user.apPat} ${user.apMat || ''}`}</p>
            <p>{user.email}</p>
            <div className="usuario-buttons">
              <button onClick={() => editUser(user)}>Editar</button>
              <button onClick={() => deleteUser(user.idUsuario)}>Eliminar</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default CRUDUsuario;
