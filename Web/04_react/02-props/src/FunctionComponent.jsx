import PropTypes from 'prop-types';

export default function FunctionComponent({ name = '기본 이름', age }){
    const student = "홍길동";
    // console.log(props.name);
    // const {name} = props;
    console.log(age);
    return (
        <div> 
            <h1> Hi {student}! </h1>
            {/* <div>넘겨받은 props {props.name} </div> */}
            <div>넘겨받은 props {name}</div>
        </div>
    );
}

FunctionComponent.propTypes = {
    age: PropTypes.number, 
}

