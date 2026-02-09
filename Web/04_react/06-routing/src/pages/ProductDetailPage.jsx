// import { productInfos } from "../components/Productlist";
import { useNavigate, useParams } from "react-router-dom";

function ProductDetailPage({products}) {
    const {productId} = useParams(); // string 타입으로 반환 ex) '2'
    const product = products[Number(productId) - 1];

    // navigate
    const navigate = useNavigate();

    return ( 
        <div>
            <h1>Product Detail Page</h1>
            <button onClick={() => navigate(-1)}>뒤로 가기</button>
            <button onClick={() => navigate('/')}>홈으로 이동하기</button>
            {products.length !== 0 ? (
            <ul>
                <li>상품번호: {product.id}</li>
                <li>상품명: {product.name}</li>
                <li>판매자: {product.email}</li>
                <li>상세 설명: {product.body}</li>
            </ul>
            ) : (
                <div>Loading...</div>
            )}
        </div>
     );
}

export default ProductDetailPage;