import { useSearchParams, useNavigate } from 'react-router-dom';

function StudentNew() {
  const [searchParams] = useSearchParams();
  const KeyWord = searchParams.get('name');
  const navigate = useNavigate();
  
  return (
    <div>
      <h2>학생 이름은 <span style={{color: 'green'}}>new</span>입니다.</h2>
      <h3>실제 이름은 <span style={{color: 'red'}}>{KeyWord}</span></h3>
      <button onClick={() => navigate(-1)}>이전 페이지로</button>
    </div>
  );
}

export default StudentNew;