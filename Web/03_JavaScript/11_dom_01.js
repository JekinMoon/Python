// script 태그 위치가 head > titile 아래였을 때
console.log(document); // html 문서
console.log(document.head); // html 내 head 태그
console.log(document.body); // null
// html도 위에서부터 코드가 순차적으로 실행되기 때문에 
// JS를 불러온 뒤에 body 태그가 생성되어서 body가 null로 반환됨

// script 태그 위치가 html 닫히는 태그 위였을 때
console.log(document); // html 문서
console.log(document.head); // html 내 head 태그
console.log(document.body); // html 내 body 태그
// body가 생성된 이후 js 코드를 불러오면
// 문제 없이 body 태그를 불러올 수 있는 것

// 이런 불편함을 개선하고자
// script 태그에 type=module 속성을 부여할 경우
// html이 모두 로드된 두 js코들르 불러와 실행시킴
// 현재 html에 적힌 script 태그 형태
// <script type="module" src="./11_dom_01.js"></script>
// head태그 내부 title 아래 위치



// document 객체를 활용한 HTML 요소 선택
// 이전 방식(legacy)
console.log(document.getElementById('green'));
console.log(document.getElementsByClassName('default'));
console.log(document.getElementsByTagName('div'));

console.log("======================================");

// 선호되는 방식
// querySelector
// CSS 선택자로 HTML 요소를 가져옴
// 제일 처음 발견한 요소 하나만 반환
console.log(document.querySelector("#green"));
console.log(document.querySelector(".default"));
console.log(document.querySelector("input"));
console.log(document.querySelector('[name="id"]'));


console.log("======================================");


// querySelectorAll
// CSS 선택자에 만족하는 모든 HTML 요소들을 NodeList라는 배열과 유사한 형태로 반환
// 불러온 요소들에 대한 순회가 가능 (forEach 활용)
console.log(document.querySelectorAll('.default'));
console.log(document.querySelectorAll('.others'));
console.log(document.querySelectorAll('div'));

// forEach 활용 NodeList 순회
const divEl = document.querySelectorAll("div");
console.log('querySelectorAll 활용 모든 div 요소 선택:', divEl);
divEl.forEach((el) => console.log("순회한 요소:", el) );

// for of 활용 NodeList 순회
const classDefaultEl = document.querySelectorAll('.default');
for (let el of classDefaultEl){
    console.log('for of 활용 .default 요소 순회:', el);
}






