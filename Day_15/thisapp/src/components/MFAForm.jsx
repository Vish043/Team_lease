import React,{useState} from "react";

const MFAForm = ({username,expectedOTP, onVerify}) => {
    const [otp,setOTP] = useState('');
    const [error, setError] = useState ('');

    const handleVerify = (e) => {
        e.preventDefault();
        if (otp === expectedOTP) {
            onVerify();
        } else{
            setError('Incorrrect OTP');
        }
    };

    return (
        <form onSubmit={handleVerify}>
            <h2>Enter OTP for {username}</h2>
            <input
                type = "text"
                maxLength = "6"
                value = {otp}
                onChange={(e) => setOTP(e.target.value)}
                placeholder="Enter 6-digit OTP"
                required
            /><br /><br />
            <button type="submit">Verify</button>
            {error && <p style={{color: 'red'}}>{error}</p>}
        </form>
    );
    };

export default MFAForm;