// src/App.js
import React, { useState } from 'react';
import Registration from './Registration';
import Login from './Login';
import ContactList from './ContactList';
import './App.css';

function App() {
  const [token, setToken] = useState(null);

  return (
    <div className="App">
      <h1>VividComm Chat App</h1>
      {token ? (
        <ContactList token={token} />
      ) : (
        <>
          <Registration />
          <hr />
          <Login setToken={setToken} />
        </>
      )}
    </div>
  );
}

export default App;