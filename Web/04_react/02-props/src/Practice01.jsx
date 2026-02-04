export default function Food({ food = '돼지국밥' }) {
  return (
    <div>
      <p>
        제가 좋아하는 음식은 <span style={{ color: 'red' }}>{food}</span> 입니다.
      </p>
    </div>
  );
}