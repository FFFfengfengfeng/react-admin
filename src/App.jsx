import React, { Component } from 'react';
import Hello from './views/components/Hello.jsx';
import './App.css';
 
class App extends Component {
  render() {
    return (
      <div className="App">
        <Hello name="FFF"></Hello>
        <Hello name="WWW"></Hello>
      </div>
    );
  }
}
 
export default App;