import React, { useState } from "react";

function Practice03() {
    const[number, setNumber] = useState(0);
    const increase = () => setNumber(number + 1);
    const decrease = () => setNumber(number - 2);

return (
        <div>
            <h1>{number}</h1>
            <button onClick={increase}>Plus 1</button>
            <h1>{number}</h1>
            <button onClick={decrease}>Minus 2</button>
        </div>
    );
}
export default Practice03;