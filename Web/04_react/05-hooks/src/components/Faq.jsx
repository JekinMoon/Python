import useToggle from "../hooks/useToggle";

function Faq() {
    const [isFaqOpen, setIsFaqOpen] = useToggle();
    return ( 
        <div>
            <h1>custom hook ex</h1>
            <div style={{cursor: 'pointer'}} onClick={setIsFaqOpen}>
                Q. 리액트에서 커스텀 훅 만들 수 있나요?
            </div>
            {isFaqOpen && <div>A. 가능!</div>}
        </div>
     );
}

export default Faq;