import './App.css';
import FunctionComponent from './FunctionComponent';
import Props_ex1 from './Practice01';
import Book from './Practice02';
import cover from './cover.png'; 
import Counter from './Counter';
import React from 'react';
import Practice03 from './Practice03';


function App() {
  return (
  <div className="App">
        <FunctionComponent name='로이' age={10}/>
        <FunctionComponent />

        <hr />
        <button link="https://www.google.com">Google</button>

       <Props_ex1 food="돼지국밥" /> 
       <Props_ex1 /> 
      
      <div>
      <Book
        title="괴테는 모든 것을 말했다"
        author="스즈키 유이"
        price={15300}
        type="소설"
        cover={cover}
      />

      <hr />
      <h2>useState 활용</h2>
      <Counter />
    
    <hr />

    <div>
      <Practice03 />
    </div>


    </div>

  </div>
   
  );
}

export default App;
