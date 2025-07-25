import ClassComponent from './components/ClassComponent';
import FunctionalComponent from './components/FunctionalComponent';
import PropsComponent from './components/PropsComponent';

function App() {

  return (
    <>
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