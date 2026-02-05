import { useState, useEffect } from "react";
import axios from "axios";

function PostLists() {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        const getPosts = async () => {
            const response =await axios.get('https://jsonplaceholder.typicode.com/posts');
            setPosts(response.data);
        };

        setTimeout(() => {
            getPosts();
        }, 2000);
    }, []);

    return (
        <div style={{ padding: '20px'}}>
            <h1>Post List</h1>
        {posts.length === 0 ?(
            <h2>Loading...</h2>
        ) : (
            <ul>
                {posts.map((post) => (
                 <li key={post.id} style={{ marginBottom: "20px"}}>
                    <h3>{post.title}</h3>
                    <p>{post.body}</p>
                 </li>
                ))}
            </ul>
        )}
        </div>
    );
}

export default PostLists;