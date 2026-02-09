import { useParams, useNavigate } from 'react-router-dom';

function Student() {
  const { name } = useParams();
  const navigate = useNavigate();
  
  return (
    <div>
      <h2>이곳은 <span style={{color: 'orange'}}>{name}</span>입니다.</h2>
      <button onClick={() => navigate(-1)}>이전 페이지로</button>
    </div>
  );
}

export default Student;