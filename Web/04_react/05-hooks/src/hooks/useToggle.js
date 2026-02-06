import { useState } from "react";

export default function useToggle(initValue = false){
    const[value, setValue] = useState(initValue);

    // 토글 상태를 전환
    const toggleValue = () => {
        setValue(!value);
    };

    return [value, toggleValue];
}