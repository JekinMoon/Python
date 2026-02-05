import { useState, useEffect } from "react";
import{fakePosts} from './Practice1-1'


function PostList() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    setTimeout(() => {
      setPosts(fakePosts);
    }, 2000);
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1 style={{fontSize: '20px', fontWeight: 'normal'}}>🕊️Post List</h1>
      {posts.length === 0 ? (
        <h2>Loading...</h2>
      ) : (
        <ul>
          {posts.map((post) => (
            <li key={post.id} style={{ marginBottom: "20px" }}>
              <h3>{post.title}</h3>
              <p>{post.body}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default PostList;