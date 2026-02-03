function  Practice3() {
  const a = 10;
  const b = 5;

  return (
    <div className="App">
      {(a > b) && <h2>a가 b보다 큽니다</h2>}
    </div>
  );
}

export default Practice3;