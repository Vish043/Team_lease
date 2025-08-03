import ClassComponent from './components/ClassComponent';
import FunctionalComponent from './components/FunctionalComponent';
import PropsComponent from './components/PropsComponent';
import { Header } from './components/Header';

function App() {

  return (
    <>
        <Header />
        <hr />
        <ClassComponent/>
        <hr />
        <FunctionalComponent/>
        <hr />
        <PropsComponent name="Swami Narayan" />
        <hr />
        
    </>
  );
}

export default App