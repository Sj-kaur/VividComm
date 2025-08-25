import React, { useState } from 'react';
import Registration from './Registration';
import Login from './Login';
import './App.css';

function App() {
  const [token, setToken] = useState(null);

  return (
    <div className="App">
      <h1>VividComm Chat App</h1>
      {token ? (
        <div>
          <p>You are logged in!</p>
          {/* Here you would add a Logout button and other protected content */}
        </div>
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