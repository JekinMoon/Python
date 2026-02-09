import {Link} from "react-router-dom";

function ProductItem({product}) {
    return (
        <>
            <Link to={`/products/${product.id}`}>
                <li>상품명: {product.name}</li>
                <li>상세 설명: {product.body}</li>
            </Link>
        </>
    );
}

export default ProductItem;