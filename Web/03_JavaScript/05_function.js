// 함수 호이스팅(Hoisting)
// 함수 선언식으로 함수를 만들었을 때는 선언보다 위에서 호출 가능
// 함수 표현식, 화살표함수는 호출 불가
console.log(
  '사각형의 넓이 구하기 (함수 선언식, 선언보다 위에서 호출)',
  myFunc('어라라'),
); // 실행됨
// myFunc3(); // 함수 표현식, 선언보다 위에서 호출 // 실행 안됨
// console.log(
//   '사각형의 넓이 구하기 (화살표 함수, 선언보다 위에서 호출)',
//   square(10, 8),
// ); // 실행 안됨

// 1. 함수 선언

// 1-1. 함수 선언식 (기본적인 함수 선언 방법)
function myFunc(str) {
  // 중괄호 내부에 함수 호출 시 동작할 코드 작성
  return str;
}

myFunc('이거 콘솔에 찍히지 않아요'); // console.log() 사용 안했으니까 그냥 냅다 "이거 콘솔에 찍히지 않아요"를 쓴 것일 뿐
console.log(myFunc('이렇게 해야 정상적으로 콘솔에 찍혀요'));

// 간단 실습
// 함수를 호출만 해도 콘솔에 찍히게 하기

function myFunc2(str) {
  // 중괄호 내부에 함수 호출 시 동작할 코드 작성
  console.log(str);
}
myFunc2('이렇게 호출만 해도 콘솔에 찍혀야 해요!');

// 1-2. 함수 표현식
// 변수에 익명함수를 할당하는 방법
const myFunc3 = function () {
  console.log('이렇게 함수 표현식으로 함수를 선언할 수 있어요');
};

myFunc3();

// 1-3. 화살표 함수
// 콜백함수 (어떤 코드나 로직 안에 작성할 때 많이 사용)
const arrowFunc = () => {
  // 화살표 함수는 {}안에 꼭 return이 되어야 함
  return '이렇게 화살표 함수를 사용할 수 있어요';
};

// 한 줄로 작성 + 괄호 없는 경우에는 해당 내용을 자동으로 return
const arrowFunc2 = () => '이렇게 쓸 수도 있어요';
arrowFunc2();
console.log(arrowFunc2); // 호출 안하고 변수를 콘솔에 찍은 버전 => () => '이렇게 쓸 수도 있어요' 출력
console.log(arrowFunc2()); // () 사용해서 함수를 호출한 버전 => 이렇게 쓸 수도 있어요 출력

// 사각형의 넓이를 구하는 화살표 함수
const square = (width, height) => width * height;
console.log('사각형의 넓이 구하기', square(10, 8)); // 80

function noReturnFunc(width, height) {
  width * height;
}

console.log(noReturnFunc(5, 7)); // return 하지 않으면 그냥 함수 스코프 내부 코드 실행되고 끝