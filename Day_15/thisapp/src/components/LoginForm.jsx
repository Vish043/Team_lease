import React,{useState} from "react";

const LoginForm = ({ onLoginSuccess}) => {
    const [form, setForm] = useState({username: '', password: ''});
    const [error, setError] = useState ('');

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value});
    };

    const handleSubmit = (e) => {
        e.preventDefault ();

        if (form.username === 'user' && form.password === 'pass'){
            onLoginSuccess (form.username);
        }else{
            setError('Invalid credentials');
        }
    };
    return (
        <form onSubmit = {handleSubmit}>
            <h2>Login</h2>
            <input
            type="text"
            name = "username"
            placeholder = "Username"
            value={form.username}
            onChange={handleChange}
            required
            /><br /><br />
            <input 
            type = "password"
            name = "password"
            placeholder="Password"
            value = {form.password}
            onChange={handleChange}
            required
            /> <br /><br />
            <button type = "submit">Login</button>
            {error && <p style={{color:'red'}}>{error}</p>}
        </form>
    );
};

export default LoginForm;