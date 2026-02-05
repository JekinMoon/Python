import { useState } from 'react';

function Alphabet2() {
	/**
	 * {
	 * 	id: 1,
	 * 	alpha: 'a',
	 * },
	 * ...
	 */
	const [alphabet, setAlphabet] = useState([]);
	// input 값을 state 변수로 선언
	const [inputAlpha, setIntputAlpha] = useState('');

	const addAlpha = () => {
		const newAlpha = alphabet.concat({
			id: alphabet.length + 1,
			alpha: inputAlpha,
		});
		setAlphabet(newAlpha);
		setIntputAlpha('');
	};

	const deleteAlpha = (targetId) => {
		const newAlpha = alphabet.filter((alpha) => alpha.id !== targetId);
		setAlphabet(newAlpha);
	};
	return (
		<>
			{/* onChange 이벤트로 값의 변경 감지 -> state 변수값이 변경되게끔 만들기 */}
			<input
				type='text'
				placeholder='알파벳 입력'
				value={inputAlpha}
				onChange={(e) => setIntputAlpha(e.target.value)}
			/>
			<button onClick={addAlpha}>ADD</button>
			<ol>
				{alphabet.map((value) => {
					return (
						<li key={value.id} onDoubleClick={() => deleteAlpha(value.id)}>
							{value.alpha}
						</li>
					);
				})}
			</ol>

			{/* 단축평가 */}
			{alphabet.length === 0 && <span>알파벳을 입력해주세요!</span>}
		</>
	);
}

export default Alphabet2;
