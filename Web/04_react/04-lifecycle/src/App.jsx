import './App.css';
import LifeCycleFunc from './Lifecycle';
import PostList from './Practice1';
import PostLists from './Practice2';
import ColorText from './Practice3';

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

    </div>
  );
}

export default App;
