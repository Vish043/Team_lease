import React from 'react';

function PropsComponent({ name}){
    return (
        <div>
            <h1>Hello Your Name is: {name}</h1>
        </div>
    );
}
export default PropsComponent;