import {Link} from 'react-router-dom';

const Navbar = () => (
    <nav style = {{ padding: '10px', background: '#eee'}}>
        <Link to="/" style={{marginRight: '10px'}}>Home</Link>
        <Link to="/about" style={{marginRight: '10px'}}>About</Link>
        <Link to="/dashboard">Dashboard</Link>
    </nav>
);

export default Navbar;