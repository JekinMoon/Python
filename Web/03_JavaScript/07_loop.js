// 1. for문
// 횟수를 기준으로 하는 반복문

console.log('=== for문 ===')

for (let i=0 ; i < 10; i++){
    console.log(i);
}


console.log('==================');

for (let i=0 ; i <= 10; i++){
    console.log(i);
}

console.log('==================');

for (let i=10 ; i >= 1; i--){
    console.log(i);
}

console.log('==================');

for (let i=0 ; i <= 20; i+=3){
    console.log(i);
}

console.log('==================');

// 1부터 100까지 합 구하기
let sum = 0;
for (let i=1 ; i < 101; i++){
    sum += i;
}
console.log('1~100까지의 합', sum);

console.log('==================');

// 이중 for 문
console.log('이중 for문');

for (let i = 0; i < 3; i++){
    for (let j = 0; j < 5; j++){
    // i는 고정된 상태로 j만 1씩 커지면서 해당 scope의 코드 실행됨
    // j의 루프가 완료되면 i가 1씩 커지는 것
        console.log('i: ', i, 'j: ', j  );
    }
}

// 2. while문
// 조건을 기준으로한 반복

console.log(`=== while문 ===`)

let i = 0;

// 무한루프(i가 계속 0 이기 때문)
// while(i < 5){
//     console.log(i);
// }


while (i < 5) {
    console.log(i);
    i++;
}

console.log('===============');
let blinker = '초록불';

while (blinker === '초록불'){
    console.log('당장 길을 건너세요!');
    blinker = prompt('신호등 상태를 입력하세요 (초록불/빨간불)');
    // 예외처리
    if (blinker !== '초록불'){
        continue; // 초록불이면 계속 콘솔 찍기
    } else if (blinker !== '빨간불'){
        break; //루프를 빠져나가는 코드
    } else {
        blinker = prompt('신호등 상태를 다시 정확하게 입력하세요(초록불/빨간불)');
    }
}

