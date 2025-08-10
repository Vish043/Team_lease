import React from "react";
import {signInWithPopup} from 'firebase/auth';
import {auth, provider} from './Firebase';

const Login = () => {
    const signInWithGoogle = async () => {
        try {
            const result = await signInWithPopup(auth, provider)
            console.log("User Info:", result.user);
            alert(`Welcome ${result.user.displayName}`);
        }catch (error){
            console.log("Google Sign-In Error:",error);
        }
    };
    return (
        <div style = {{textAlign : 'center', marginTop: '100px'}}>
            <h2>Sign In With Google</h2>
            <button onClick={signInWithGoogle} style={{padding: '1ppx 20px'}}>
                Sign In
            </button>
        </div>
    );
};

export default Login;