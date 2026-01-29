let str = "     Hello JavaScript World      ";

console.log("원본 str", str);

// .length
console.log('길이: ', str.length); // 함수 x, 하나의 속성

// .trim : 공백 제거
console.log('공백 제거: ', str.trim()); // "Hello JavaScript World" 앞뒤 공백 제거됨
console.log('원본str', str); // 원본 변경x

// 대소문자 변환
console.log("대문자 변환:", str.toUpperCase()); // "HELLO JAVASCRIPT WORLD"
console.log('원본str', str); // 원본 변경x

console.log("소문자 변환:", str.toLowerCase()); // "hello javascript world"
console.log('원본str', str); // 원본 변경x


// 탐색
console.log('글자 인덱스 찾기:', str.indexOf("J")); // 11
console.log('단어 인덱스 찾기:', str.indexOf("Java")); // 11 => 매개변수로 받은 문자열의 첫번째 글자 인덱스 반환
console.log('없는 단어 인덱스 찾기:', str.indexOf("Jva")); // -1 => 매개변수로 받은 문자열이 없다면 -1로 반환

// .indexOf()로도 문자열에 포함 여부 알 수 있음 => -1 반환하면 없다는 것
console.log('문자열의 포함 여부 확인:', str.includes("Java")); // true => 불리언으로 반환
console.log('문자열의 포함 여부 확인:', str.includes("Jva")); // false

// 슬라이싱
console.log('슬라이싱:', str.slice(6,16)); // ello JavaS 6번 인덱스부터 15번 인덱스 문자열까지 출력
console.log('원본str', str); // 원본 변경x

// 치환
console.log('한 글자 치환:', str.replace('a','e')); // 문자열 중에서 가장 처음 나오는 a 문자를 e로 치환 
console.log('한 단어 치환:', str.replace('World', 'Universe')); // Hello JavaScript Universe 단어도 치환 가능 
console.log('전부 치환:', str.replaceAll('l', 'v')); // Hevvo JavaScript Worvd 
console.log('원본str', str); // 원본 변경x

// 분할
// ''(공백)을 매개변수로 전달 시 문자열의 모든 글자들이 하나씩 짤려서 배열로 반환
console.log('"" 기준 분할:', str.split('')); 

// " "(공백 한 칸)을 기준으로 문자열로 나눠서 배열로 반환
console.log('" " 기준 분할:', str.split(' ')); // ['', '', '', '', '', 'Hello', 'JavaScript', 'World', '', '', '', '', '', '']

// 분할하는 기준의 매개변수는 사라지고 배열로 만들어져서 반환
console.log('l 기준 분할:', str.split('l')); // ['     He', '', 'o JavaScript Wor', 'd      ']
console.log('원본str', str); // 원본 변경x

// 합치기
let str2 = "with JavaScript";
console.log("문자열 합치기:", str.concat(str2)); // Hello JavaScript World      with JavaScript

console.log(`문자열 합치기2: ${"Hello ".concat(str2)}`); // Hello with JavaScript
console.log(`문자열 합치기3: ${"Hello ".concat(str2), str}`); // Hello JavaScript World 
console.log(`문자열 합치기4: ${"Hello ".concat("I'm Moon", ' nice to meet you')}`); // Hello I'm Moon nice to meet you

console.log('원본str', str); // 원본 변경x
console.log('원본str2', str2); // 원본 변경x
