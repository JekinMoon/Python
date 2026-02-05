import { useState } from "react";

function Practice2() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [users, setUsers] = useState([]);

  const addUser = () => {
    if (!name || !email) return;
    const newUser = users.concat({
      id: users.length + 1,
      name: name,
      email: email,
    });
    setUsers(newUser);
    setName("");
    setEmail("");
  };

  const deleteUser = (targetId) => {
    const newUsers = users.filter((user) => user.id !== targetId);
    setUsers(newUsers);
  };

  return (
    <div style={{ padding: "10px" }}>
      <input
        placeholder="이름"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        placeholder="이메일"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <button onClick={addUser}>등록</button>

      <ul style={{ listStyle: "none" }}>
        {users.map((user) => {
          return (
            <li key={user.id} onDoubleClick={() => deleteUser(user.id)}>
              <div style={{ fontWeight: "bold" }}>{user.name}</div>
              <div>{user.email}</div>
            </li>
          );
        })}
      </ul>
    </div>
  );
}

export default Practice2;