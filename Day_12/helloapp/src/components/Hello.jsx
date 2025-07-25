import React from 'react';

function getMessage(user) {
    return `Welcome, ${user}!`;
}

export default function Hello(){
    const name = 'Hari Krishna';
    const greeting = 'Hello, ' + name + '!';
    const message = <h3>{getMessage("Hari Krishna")}</h3>;
    const x=10,y=20;
    const result = <h3>The addition of {x} and {y} is {x+y}</h3>
const loggedIn = true;
const status = <p>{loggedIn?"Welcome again":"Login again"}</p>
const greet = ["Hello ","Hi "," Welcome"];
const greetList = <p>{greet.length>0 && "You have new greet messages"}, {greet}</p>
const style={
    color:'blue',
    fontsize:'20px',
    fontweight:'bold'
}

const styledText = <h2 style={style}>This is a styled Text</h2>
const form = (
    <form>
        <label htmlFor = "email">Email:</label>
        <input type = "email" id="email" className="input-field" />
    </form>
);
    return (
        <>
        <h1>{greeting} !!</h1>
        {message}
        {result}
        {status}
        {greetList}
        {styledText}
        {form}
        </>
    );
}