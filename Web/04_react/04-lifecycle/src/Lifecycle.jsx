import { useState } from "react";
import LifecycleChild from "./LifecycleChild";

function LifeCycleFunc(){
    const [number, setNumber] = useState(0); 
    const [visible, setVisible] = useState(true);

    const changeNumber = () => {
        setNumber(number + 1 ); 
    };

    const changeVisible=() =>{
        setVisible(!visible);
    };
    return (
        <div>
            <button onClick={changeNumber}>Plus</button>
            <button onClick={changeVisible}>On/Off</button>

            {visible && <LifecycleChild number={number} />}
        </div>
    ) 
};

export default LifeCycleFunc;
