import { Route, Routes } from 'react-router-dom';
import './styles/App.css';
import Header from './components/Header';

function App() {
  return (
    <div className="App">
      <Header />
      <Routes>
        <Route path='/' element={<h1>Home</h1>} />
        <Route path='/products' element={<h1>Products Page</h1>} />
        <Route 
          path='/products:productId' 
          elemennt={<h1>Products detail Page</h1>} />
      </Routes>
    </div>
  );
}

export default App;
