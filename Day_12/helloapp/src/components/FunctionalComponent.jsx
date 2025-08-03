import React, { useState } from "react";
function FunctionalComponent() {
    const [name,setName] = useState(' ');
    const handleSubmit = (e) => {
        e.preventDefault();
        alert(`Name submitted: ${name}`);
        setName('')
    }
return (
    <>
    <h3>This is Functional Component Loaded</h3>
    <form onSubmit = {handleSubmit}>
        <label htmlFor = "name">Name:</label>
        <input type="text" id="name" placeholder='Enter Name' value={name}
        onChange={(e)=>setName (e.target.value)}/>
        <button type="submit">Submit</button>
    </form>
    </>
);
}
export default FunctionalComponent;