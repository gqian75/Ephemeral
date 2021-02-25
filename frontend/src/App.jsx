import React from 'react';
import logo from './logo.svg';
import './App.css';
import useAxios from 'axios-hooks'

function App() {

const[{data}]= useAxios("/api/test");





  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React {data}
        </a>
      </header>
    </div>
  );
}

export default App;
