import React, { useState, useEffect } from 'react';
import './UsuarioForm.css';

const UsuarioForm = ({ onSubmit, editingUser, onUpdate, onCancelEdit }) => {
  const [user, setUser] = useState({
    nombre: '',
    apPat: '',
    apMat: '',
    password: '',
    email: '',
    superUser: false,
  });

  useEffect(() => {
    if (editingUser) {
      setUser(editingUser);
    } else {
      setUser({
        nombre: '',
        apPat: '',
        apMat: '',
        password: '',
        email: '',
        superUser: false,
      });
    }
  }, [editingUser]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setUser((prevUser) => ({
      ...prevUser,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (editingUser) {
      onUpdate(user);
    } else {
      onSubmit(user);
    }
    setUser({
      nombre: '',
      apPat: '',
      apMat: '',
      password: '',
      email: '',
      superUser: false,
    });
  };

  return (
    <div className="usuario-form-container">
      <h2>{editingUser ? 'Editar Usuario' : 'Agregar Usuario'}</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" name="nombre" placeholder="Nombre" value={user.nombre} onChange={handleChange} required />
        <input type="text" name="apPat" placeholder="Apellido Paterno" value={user.apPat} onChange={handleChange} required />
        <input type="text" name="apMat" placeholder="Apellido Materno" value={user.apMat} onChange={handleChange} />
        <input type="password" name="password" placeholder="Contraseña" value={user.password} onChange={handleChange} required />
        <input type="email" name="email" placeholder="Email" value={user.email} onChange={handleChange} required />
        <label>
          <input type="checkbox" name="superUser" checked={user.superUser} onChange={() => setUser((prevUser) => ({ ...prevUser, superUser: !prevUser.superUser }))} />
          Super Usuario
        </label>
        <div>
          <button type="submit">{editingUser ? 'Actualizar' : 'Agregar'}</button>
          {editingUser && <button type="button" onClick={onCancelEdit}>Cancelar</button>}
        </div>
      </form>
    </div>
  );
};

export default UsuarioForm;
