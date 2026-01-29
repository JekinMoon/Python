// 1. if문
console.log("=== if문 ===");

let a = 10;
if (a > 5){
    // if문의 조건이 true일 때 실행할 코드
    console.log(`${a}이(가) 5보다 크다`);
}

// 코드가 한 줄일 때는 scope 생략이 가능
if (a > 3) console.log(`${a}이(가) 3보다 크다`);

// if - else
if (a > 20) {
    console.log(`${a}이(가) 20보다 크다`);
} else{
    // if문의 모든 조건이 false인 경우에도 무조건 실행시킬 코드
    console.log(`${a}이(가) 20보다 작거나 같다`);
}

// if - else if  -else
let score = 85;

if(score >= 90) {
    console.log('A');
} else if (score >= 80){
    console.log('B');
} else if (score >= 70){
    console.log('C');
} else if (score >= 60){
    console.log('D');
} else{
    console.log('F');
}

// // if 문을 따로따로 작성하는 경우
// if(score < 90 && score >= 80){
//     console.log('B')
// }

// // 마지막 else문도 else if문으로 작성 가능
// // ex)
// else if (score < 60){
//     console.log('F');
// }
// 이렇게 될 경우에는 코드를 쓰는 입장에서도 글자를 많이 써야 하고
// 실행될 때에도 조건에 만족하는지 불필요하게 검사를 진행함


// // 2. if문 중첩
// console.log("=== if문 중첩 ===");

// let userId = 'Moon';
// let userPw = '1234*';

// let userInputId = prompt('아이디를 입력해주세요');

// if (userId === userInputId){
//     // 아이디가 맞음
//     let userInputPw = prompt('비밀번호를 입력하세요');
//     if (userPw === userInputPw){
//         //비밀번호가 맞음
//         alert("로그인 성공");
//     } else{
//         alert('비밀번호가 일치하지 않습니다.');
//     }
// } else{
//     alert("아이디가 일치하지 않습니다.");
// }


// 2. Switch
// console.log('=== switch문 ===');

// let b = Number(prompt('숫자를 입력해주세요'));

// switch (b) {
//     case 1:
//         console.log('b가 1이네요');
//         // switch문에서 케이스 내 코드 작성 시 무조건 break 사용해야 함
//         break;
//     case 2:
//     case 3:
//     case 4:
//         // case만 연달아 작성한 경우 해당 케이스 중 하나라도 만족하면 ":" 다음 코드 실행
//         console.log('b가 2~4 중 하나네요');
//     case 5:
//         console.log('b가 5네요');
//     default:
//         // 위의 모든 조건들이 불만족할 때 무조건 실행되는 코드
//         // default로 실행할 코드가 없다면 작성하지 않아도 괜찮음
//         // default문 꼭 작성하지 않아도 괜찮음(생략 가능)
//         console.log('b가 뭔지 모르겠습니다.');
//         break;
// }

// 3. 삼항연산자
console.log('=== 삼항 연산자 ===');
// 간단한 조건문을 간결하게 표현하는데 사용

let num =100;

// 일반 if문
if (num > 50){
    console.log('num이 50보다 크다');
} else{
    console.log('num이 50보다 작거나 같아요');
}

// 동일한 로직 삼항연산자로 변환
// 조건 ? 조건이 true일 때 실행될 코드 : 조건이 false일 때 실행될 코드
num > 50 
    ? console.log('num이 50보다 크다') // ? 다음은 참일 때 실행
    : console.log('num이 50보다 작거나 같아요'); // : 다음은 거짓일 때 실행


// 삼항연산자 실습
let now = new Date().getHours();
console.log('현재시간', now);

now < 12 ? console.log('오전') : console.log('오후');


