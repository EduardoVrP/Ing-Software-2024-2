import React from 'react';
import './App.css';
import CRUDUsuario from './components/CRUDUsuario';
import CRUDPelicula from './components/CRUDPelicula';

function App() {
  return (
    <div className="App">
      <CRUDUsuario />
      <CRUDPelicula />
    </div>
  );
}

export default App;
