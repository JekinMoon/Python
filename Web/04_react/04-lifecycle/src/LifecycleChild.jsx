import { useEffect, useState } from "react";

function LifecycleChild({number}){
    const [input, setInput] = useState('');
    // mount 시점에 실행
    useEffect(() => {
        console.log("컴포넌트 마운트!")
    }, []);

    // unmount 시점에 실행
    useEffect(() => {
        return () => {
            console.log('컴포넌트 언마운트!');
        };
    },[]);

    // mount 또는 update 시점에 실행
    useEffect(() => {
        console.log('컴포넌트 마운트 or 업데이트!');
    });
    
    // input 상태가 업데이트 될 때 실행
    useEffect(() => {
        console.log('마운트, input 상태가 변경됨에 따라');
    }, [input]);
    
    return (
        <div>
            자식 컴포넌트
            <div>현재 Number 값은 {number}입니다. </div>
            <input type="text" value={input} onChange={(e)=> setInput(e.target.value)}/>
        </div>
    );
}

export default LifecycleChild;