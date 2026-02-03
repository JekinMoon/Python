import logo from './logo.svg';
import './App.css';
import Practice1 from './practice1';
import Practice2 from './practice2';
import Practice3 from './practice3';
import Practice4 from './practice4';


function App() {
  const name = 'Moon';
  const styles = {
    backgroundColor: 'yellow',
    color: 'pink',
    fontSize: '48px',
  };
  return (
    <>
    <div className="App">
      {/* JSX 문법*/}
      {/* 1. 하나로 감싸인 요소 */}
      <div>반가워요</div>
      {/*
      2. javascript 표현식 사용
      - {}로 감싸면 js 표현식 사용 가능
      - {} 안에서 삼항 연산자 사용 가능 (if, for문 등은 안됨)
       */}
      <div>{name} 안녕하세요</div>
      <div>{name === "Moon" ? "반갑습니다" : "누구세요?"}</div>


      {/* 
      3. style 속성
      - 리액트에서 dom요소에 스타일 적용시 문자열x -> 객체 사용
      - 스타일 이름 중 하이픈(-) 포함시 camelCase로 작성해야 함
      */}
      <div style={styles}>하이</div>
      <div style={{ 
        backgroundColor: 'yellow',
        color: 'pink',
        fontSize: '48px',
      }}>반가워요</div>


      {/*
      4. className 사용
      - class 속성이 아닌 className 속성 사용!

      5. 종료 태그가 없는 태그의 사용
      - 기존의 종료 태그가 없는 태그를 사용하더라도 종료 태그를 작성해야 함 or self-closing

      6. 주석
      - // : jsx 외부 주석
      */}
    </div>
    <div></div>
    <Practice1 />
    <Practice2 />
    <Practice3 />
    <Practice4 />
   </>
  );
}

export default App;
