import About from "./components/about";
import Navbar from "./Navbar";
import Home from "./components/Home";
import Dashboard from "./components/Dashboard";
import DashboardSettings from "./components/DashboardSettings";
import DashboardHome from "./components/DashboardHome";
const App = () => (
    <>
        <Navbar />
        <Routes>
            <Route path ="/" element={<Home />} />
            <Route path = "/about" element = {<About />}/>
            <Route path="/dashboard" element = {<Dashboard />} >
                <Route index element = {<DashboardHome />} />
                <Route path = "home" element={<DashboardHome />} />
                <Route path = "settings" element = {<DashboardSettings />} />
            </Route>
        </Routes>
    </>
);

export default App;