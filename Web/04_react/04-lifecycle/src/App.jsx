import './App.css';
import LifeCycleFunc from './Lifecycle';
import PostList from './Practice1';
import PostLists from './Practice2';
import ColorText from './Practice3';
import Total from './Practice4';

function App() {
  return (
    <div className="App">
      <LifeCycleFunc/>
      <hr />
      <PostList />
      <hr />
      <PostLists />
      <hr />
      <ColorText />
      <hr />
      <Total />
    </div>
  );
}

export default App;
