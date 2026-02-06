import { useState } from "react";

function ColorText() {
  const [text, setText] = useState("검정색 글씨");
  const [color, setColor] = useState("black");

  const handleClick = (e) => {
    const { text, color } = e.target.dataset;
    setText(text);
    setColor(color);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2 style={{ color }}>{text}</h2>

      <button
        data-text="빨간색 글씨"
        data-color="red"
        onClick={handleClick}
      >
        빨간색
      </button>

      <button
        data-text="파란색 글씨"
        data-color="blue"
        onClick={handleClick}
      >
        파란색
      </button>
    </div>
  );
}

export default ColorText;




// import { useState } from "react";
// const [textColor, changeColor] = useState({color:'black', text: '검정색'});

// const handleColor = (color, text) =>{
//   changeColor({color, text});
// };
// return(
//   <>
//     <h4>글씨</h4>
//     <button onClick={(e) => handleColor('red', e.target.innerText)}>빨간색</button>
//     <button onClick={(e) => handleColor('blue', e.target.innerText)}>파란색</button>
//   </>
// )
// export default ColorText;
