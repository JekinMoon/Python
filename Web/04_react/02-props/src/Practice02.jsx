function Book({ title, author, price, type, cover }) {
  return (
    <div className="book">
       <h2 className="subtitle">베스트 셀러 소설</h2>        
      {cover && <img src={cover} alt={title} className="cover" />}
      <h2 className="title">{title}</h2>   
      <p className="author">저자: {author}</p>
      <p className="price">가격: {price}원</p>
      <p className="type">분류: {type}</p>
    </div>
  );
}

export default Book;