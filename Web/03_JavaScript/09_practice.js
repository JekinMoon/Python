let numbers = [];

for (let i = 1; i <= 100; i++) {
    numbers.push(i);
}
console.log('원본 배열', numbers);

for (let i = 0; i < numbers.length; i++){
    console.log(numbers[i]);
}

let sum1 = 0;
for(let num of numbers){
    sum1 += num;
}
console.log('For of 합계: ', sum1);

let sum2 = 0;
numbers.forEach((n) => {sum2 += n;});
console.log('forEach 합계: ',sum2);

let sum3 = numbers.reduce((acc, cur) => acc + cur);
console.log('reduce 합계: ', sum3);

//==================================================
let fruits1 = ['사과', '딸기', '파인애플', '수박', '참외', '오렌지', '자두', '망고'];
let fruits2 = ['수박', '사과', '참외', '오렌지', '파인애플', '망고']


let same = fruits1.filter((fruit) => fruits2.includes(fruit));
console.log(`same 배열 출력: `, same);

let diff = fruits1.filter((fruit) => !fruits2.includes(fruit));
console.log('diff 배열 출력: ', diff);


//==================================================
//평일/주말 구분
//JS에 내장된 Data객체 활용
//Date.getDay(): 요일별로 0~6(일~토)를 숫자 반환
// let now = new Date();
// console.log(now.getDay()); // 금요일 기준 5

let nowDay = new Date().getDay();

switch(nowDay) {
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
        console.log('평일');
        break;
    case 0:
    case 6:
        console.log('주말');
        break;
        default:
        console.log('몰라');
        break;
}

if (nowDay === 0){
    console.log('주말');
} else if (nowDay === 1) {
    //월요일
    console.log('평일');
} else if (nowDay === 2) {
    //화요일
    console.log('평일');
} else if (nowDay === 3) {
    //수요일
    console.log('평일');
} else if (nowDay === 4) {
    //목요일
    console.log('평일');
} else if (nowDay === 5) {
    //금요일
    console.log('평일');
} else if (nowDay === 6) {
    //토요일
    console.log('주말');
}


let today = nowDay === 0 || nowDay === 6 ? '주말' : '평일';
console.log(today);


let now = new Date();
let day = now.getDay();

if (day === 0 || day === 6) {
    console.log("주말");
} else {
    console.log("평일");
}

//==================================================
// Math.random(): 0이상 1미만 난수생성
// Math.floor(x): 양수 기준 소수점 버림 / 음수 기준 더 작은 음수로 소수점 사라짐
// Math.floor(3.23243523465437) => 3
// Math.floor(-3.23243523465437) => -4

console.log(Math.floor(Math.random() * 11)); // 10을 곱하면 10미만의 수가 나온다

// 0.2 * 10 = 2
// 0.6354 * 10 = 6.354
// 즉, Math.random() * 10의 결과는 0이상 10미만 결과 출력
// 하지만 실습 조건은 10을 포함해야 함
// Math.random() * 11
// 0 * 11 = 0
// 0.966 * 11 = 10.626
// 0.999999999 * 11 = 10.999999989
// 무조건 11 미만 숫자가 나옴
// 그리고 그 결과를 Math.floor()하면 0~10 사이 숫자가 반환됨





