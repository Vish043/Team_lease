import React from 'react'

const headerStyle ={
  backgroundColor:'#1e293b',
  color:'white',
  padding:'1rem 2rem',
  display: 'flex',
  justifyContent:'space-between',
  alignItems:'center',
};
const navStyle = {

  display:'flex',
  gap:'1rem',
};

export const Header = () => {
  return (
    <header style = {headerStyle}>
      <h1>Welcome to Main Page with Header!!</h1>
      <nav style={navStyle}>
        <a href='/' style={{color:'white',textDecoration:'none'}}>Home</a>
        <a href='/about' style={{color:'white',textDecoration:'none'}}>About</a>
        <a href='/contact' style={{color:'white',textDecoration:'none'}}>Contact</a>

      </nav>
    </header> 
  )
}