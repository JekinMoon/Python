let arr = [10, 20, 30, 40, 50];

console.log('원본 array: ', arr);
console.log('길이:', arr.length); // 함수x


// 요소 추가
arr.push(60); // 배열 가장 마지막에 추가
console.log('push(60):', arr); // [10, 20, 30, 40, 50, 60]

arr.push(60, 70, 80, 90, 100); // 여러 개 한 번에 추가 가능
console.log('push(70, 80, 90, 100):', arr); // [10, 20, 30, 40, 50, 60, 60, 70, 80, 90, 100]

arr.unshift(0); // 배열 가장 앞에 요소 추가
console.log('unshift(0):', arr); // [0, 10, 20, 30, 40, 50, 60, 60, 70, 80, 90, 100]

arr.unshift(-10, -20, -30); // 여러 개 한 번에 추가 가능하지만 매개변수에 전달한 순서로 삽입됨
console.log('unshift(0):', arr); // [-10, -20, -30, 0, 10, 20, 30, 40, 50, 60, 60, 70, 80, 90, 100]

// 요소 삭제
let del1 = arr.pop();
console.log("=== arr.pop() === ")
console.log('del1:', del1); // 100 -> arr 배열에서 가장 마지막 요소 삭제한 뒤 **삭제한 요소**를 반환

// arr.pop()이 동작하면서 원본 arr의 가장 마지막 요소인 100이 사라짐
console.log('arr (원본 배열):', arr); // [-10, -20, -30, 0, 10, 20, 30, 40, 50, 60, 60, 70, 80, 90]

let del2 = arr.shift();
console.log("=== arr.shift() === ")
console.log('del2:', del2); // -10
console.log('arr (원본 배열):', arr); // [-20, -30, 0, 10, 20, 30, 40, 50, 60, 60, 70, 80, 90]

// 원본 유지가 필요한 경우에는 이렇게 복사본을 만들어서 해당 복사본으로 배열을 수정
let arr_copy = arr; 

// 슬라이싱
console.log("=== arr.slice() === ")
let sliced = arr.slice(1, 4);
console.log("sliced:", sliced); // [-30, 0, 10]
console.log("arr:", arr); // 원본 유지됨

// splice : 기존 요소를 삭제 or 교체
console.log("=== arr.splice() === ")
arr.splice(1, 5, 15); // 1번째 인덱스부터 요소 5개 삭제, 그 자리에 15 추가
console.log('splice(1, 5, 15):', arr); // [-20, 15, 40, 50, 60, 60, 70, 80, 90]

arr.splice(2,2); // 매개변수를 2개만 작성하면, 첫 번째 매개변수 인덱스부터 두 번째 매개변수 갯수까지 삭제만 진행
console.log('splice(2, 2):', arr); // [-20, 15, 60, 60, 70, 80, 90]


// 결합
let arr2 = [10000, 20000];
console.log('concat:', arr.concat(arr2)); // [-20, 15, 60, 60, 70, 80, 90, 10000, 20000]
console.log("arr:", arr); // 원본 변경x

// 탐색
console.log('indexOf("안"):', arr.indexOf('안')); // -1 -> 배열 안에 찾는 요소 없으면 -1 반환
console.log('indexOf(10000):', arr.indexOf(10000)); // -1 -> 원본 arr에 10000 없음
console.log('indexOf(80):', arr.indexOf(80)); // 5
console.log("arr:", arr); // 원본 변경x

console.log('includes(80)', arr.includes(80)); // true -> 포함 여부 불리언으로 반환
console.log("arr:", arr); // 원본 변경x

// 정렬
let nums = [4, 2, 7, 1, 400, 6];

console.log('원본 nums: ', nums );
nums.sort();

// 기본적으로 오름차순
// 숫자 크기를 비교하는 것이 아니라 **문자** 기준으로 앞글자를 보고 정렬
// 만약 4, 400처럼 앞글자가 같다면 그때 두 번째 글자를 보고 정렬
console.log('nums.sort():', nums); // [1, 2, 4, 400, 6, 7]  

// 숫자값 기준으로 정렬하고 싶다면
// 사칙연산 사용
nums.sort((a, b) => a - b); // 암시적으로 
console.log('nums.sort((a, b => a - b):', nums);

nums.sort((a, b) => b - a); // 내림차순
// 로직 자체가 b -a 라는 것은 숫자를 기준으로 정렬하기 때문에 해당 숫자의 크기를 기준으로 정렬 됨
console.log('nums.sort((a , b ) => b - a):', nums); // [400, 7, 6, 4, 2, 1]

// 예시
let users = [
    {id: 3, name: 'Moon'},
    {id: 1, name: 'Kim'},
    {id: 4, name: 'Park'},
    {id: 2, name: 'Jang'}, 
];

users.sort((a, b) => a.id - b.id);
console.log(users);

// 배열 순서 뒤집기(원본 변형 O)
users.reverse();
console.log('reverse:', users);




// -----------------------------

// 배열 순회 메서드

// 현재 nums 배열 : [400, 7, 6, 4, 2, 1]
// map : 배열을 순회하면서 매개변수로 전달받은 콜백함수를 적용(원본 변경x)
nums = nums.map((x) => x * 2); // 각 요소를 한 번씩 선택해서 매개변수(x)로 전달하고, 전달받은 x에 2를 곱해서 배열로 반환
console.log(nums); // [800, 14, 12, 8, 4, 2] 반환된 결과를 재할당

// filter : callback 함수를 기준으로 요소를 필터링해서 반환(원본 변경x)
let filtered = nums.filter((x) => x > 5); 
console.log(filtered);

// reduce : 앞 요소에 대해 뒤 요소를 연산한 결과를 누적
// 두 번째 매개변수로 받은 0에 배열을 순회하면서 앞 요소에 뒷 요소를 더한 값을 반환
let sum = nums.reduce((acc, cur) => acc + cur, 0); 
console.log(sum); // 840

let sum2 = 0;
for (let i=0; i < nums.length; i++) {
    sum2 += nums[i];
}
console.log(sum2); // 840