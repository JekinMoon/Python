import { useState } from "react";

function Practice3() {
  const [writer, setWriter] = useState("");
  const [title, setTitle] = useState("");
  const [type, setType] = useState("작성자");
  const [keyword, setKeyword] = useState("");
  const [searchKeyword, setSearchKeyword] = useState("");
  const [items, setItems] = useState([]);

  const add = () => {
    if (!writer || !title) return;
    setItems([...items, { id: items.length + 1, writer, title }]);
    setWriter("");
    setTitle("");
  };

  const search = () => {
    setSearchKeyword(keyword);
  };

  const reset = () => {
    setKeyword("");
    setSearchKeyword("");
  };

  const filtered = items.filter((i) => 
    !searchKeyword || (type === "작성자" ? i.writer : i.title).includes(searchKeyword)
  );

  return (
    <div style={{ padding: "10px" }}>
      <div style={{ marginBottom: "10px" }}>
        작성자 : <input value={writer} onChange={(e) => setWriter(e.target.value)} style={{ marginRight: "30px" }} />
        제목 : <input value={title} onChange={(e) => setTitle(e.target.value)} style={{ marginRight: "10px" }} />
        <button onClick={add}>작성</button>
      </div>

      <div style={{ marginBottom: "10px" }}>
        <select value={type} onChange={(e) => setType(e.target.value)}>
          <option>작성자</option>
          <option>제목</option>
        </select>
        <input value={keyword} onChange={(e) => setKeyword(e.target.value)} style={{ marginLeft: "5px", marginRight: "5px" }} />
        <button onClick={search}>검색</button>
        <button onClick={reset}>전체</button>
      </div>

      <table border="1" style={{ borderCollapse: "collapse", width: "600px", margin: "0 auto" }}>
        <thead>
          <tr>
            <th>번호</th>
            <th>제목</th>
            <th>작성자</th>
          </tr>
        </thead>
        <tbody>
          {filtered.map((i) => (
            <tr key={i.id} onDoubleClick={() => setItems(items.filter((item) => item.id !== i.id))}>
              <td>{i.id}</td>
              <td>{i.title}</td>
              <td>{i.writer}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Practice3;