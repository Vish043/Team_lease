import {  } from 'react';
import './App.css'
import {Header} from './components/Header'

function App(){
  return (
    <>
      <div>
      <Header/>
      <main style = {{padding:'2rem'}}>
        <h2>Welcome to react App</h2>
        <p>This is main content section!!</p>
      </main>
      </div>
    </>
  )
}

export default App