import { Route, Routes } from 'react-router-dom';
import './styles/App.css';
import Header from './components/Header';
import MainPage from './pages/Mainpage';
import ProductPage from './pages/ProductPage';
import ProductDetailPage from './pages/ProductDetailPage';
import { useEffect, useState } from 'react';
import axios from 'axios';
import NotFound from './pages/NotFound';

function App() {
  const[products, setProducts] = useState([]);

  const getProducts = async () => {
    const res = await axios.get('https://jsonplaceholder.typicode.com/comments');
    console.log(res.data);
    setProducts(res.data.slice(0,10));
  };

  useEffect(() => {
    getProducts();
  }, []);

  return (
    <div className="App">
      <Header />
      <Routes>
        <Route path='/' element={<MainPage />} />
        <Route path='/products' element={<ProductPage products={products} />} />
        <Route path='/products/:productId' element={<ProductDetailPage products={products} />} />
        <Route path='*' element={<NotFound />} />
      </Routes>
    </div>
  );
}

export default App;
