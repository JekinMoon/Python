import { useSearchParams } from "react-router-dom";

function MainPage() {
    const [searchParams, setSearchParmas] = useSearchParams();
    console.log(searchParams.get('mode')); // null or dark
    return (
        <div className={['main', searchParams.get('mode')].join(' ')}>
            <h1>Home</h1>
            <button
                onClick={() => {
                    setSearchParmas({ mode: 'dark' });
                }}
            >
                Dark Mode
            </button>
        </div>
    );
}


export default MainPage;