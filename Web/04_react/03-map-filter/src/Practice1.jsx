import { useState } from "react";

function Practice1() {
    const [inputValue, setInputValue] = useState("");
    const [alphabet, setAlphabet] = useState(['a', 'b', 'c', 'd', 'e']);

    const addAlpha = () => {
        if (inputValue.trim()) {
            const newAlpha = alphabet.concat(inputValue);
            setAlphabet(newAlpha);
            setInputValue("");
        }
    };

    const filteredAlphabet = alphabet.filter((value) =>
        value.toLowerCase().includes(inputValue.toLowerCase())
    );

    return (
        <>
            <h2> filter와 input으로 아래와 같이 구현해봅시다</h2>
            <input
                type="text"
                placeholder="알파벳 입력"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
            />
            <button onClick={addAlpha}>추가</button>

            <ol>
                {filteredAlphabet.map((value, idx) => {
                    return <li key={idx}>{value}</li>
                })}
            </ol>
        </>
    )
}

export default Practice1;