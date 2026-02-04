function Practice4() {
  const title = "Hello World";

  return (
    <div className="container">
      <h1 className="title">{title}</h1>
      <div style={{ textAlign: 'center'}}>
        <div>
          아이디: <input type="text" />
        </div>
        <div>
          비밀번호: <input type="text" />
        </div>
      </div>
    </div>
  );
}

export default Practice4;