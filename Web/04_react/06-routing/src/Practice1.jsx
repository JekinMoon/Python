import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Student from './Practice1-1';
import StudentNew from './practice1-2';

function Navbar () {
    return ( 
        <>
        <Link to='/'>
            <h2>ReactRouter</h2>
        </Link>
        <nav>
            <ul>
                <li style={{ margin: '4px' }}>
                    <Link to='/student/kdt'>KDT</Link>
                </li>
                <li style={{ margin: '4px' }}>
                    <Link to='/student/codingon'>코딩온</Link>
                </li>
                <li style={{ margin: '4px' }}>
                    <Link to='/student/new?name=KDT5th'>KDT 5기</Link>
                </li>
            </ul>
        </nav>

      <Routes>
        <Route path="/" element={<h1>홈페이지</h1>} />
        <Route path="/student/:name" element={<Student />} />
        <Route path="/student/new" element={<StudentNew />} />
      </Routes>
        </>
     );
}


export default Navbar;