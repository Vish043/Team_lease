import React,{useState} from "react";
import LoginForm from "./components/LoginForm";
import MFAForm from "./components/MFAForm";

function App() {
  const [step,setStep] = useState(1);
  const [username, setUsername] = useState('');
  const [generatedOTP, setGeneratedOTP] = useState ('');

  function handleLoginSuccess(user) {
    setUsername(user)
    const otp = Math.floor(100000 + Math.random() * 900000).toString();
    setGeneratedOTP(otp);
    alert(`Simulated OTP sent: ${otp}`);
    setStep(2);
  }

  function handleMFAVerified(){
    alert('MFA Verified! ✅');
    setStep(3);
  }

  return (
    <div style={{textAlign: 'center', marginTop: '50px'}}>
      {step === 1 && <LoginForm onLoginSuccess = {handleLoginSuccess} />}
      {step === 2 && (
        <MFAForm 
          username={username}
          expectedOTP = {generatedOTP}
          onVerify={handleMFAVerified}
          />
      )}
      {step === 3 && <h2>Welcome {username} 🎉</h2>}
    </div>
  );
};

export default App;