// greeting이라는 클래스를 가진 요소 greetingEl 변수에 저장하고 콘솔에 출력하기 
let greetingEl = document.querySelector('.greeting');
console.log(greetingEl);

// 태그 내용 출력
console.log(greetingEl.innerHTML);
console.log(greetingEl.textContent); // 태그 안쪽을 불러올 때 더 선호되는 방식

// 태그 내부 내용 변경
// innerHTML : 태그 안쪽 HTML을 주입 (HTML 반영 o)
greetingEl.innerHTML = "안녕하세요! 행복한 금요일 조금만 더 힘을 내요!";
console.log(greetingEl);

// textContent: 태그 안쪽에 문자열을 입력(HTML 반영 x)
greetingEl.textContent = "화이팅 빠샤빠샤!!";
console.log(greetingEl);

greetingEl.textContent = '<b>화이팅</b> 빠샤빠샤!!';

// -------------------------------------------------------

// 속성 변경

const naverEl = document.querySelector('#naver');
naverEl.textContent = "구글";
naverEl.setAttribute('href', 'http://www.google.com');
console.log(naverEl);
// <a href="http://naver.com" id="naver">네이버</a> 
// 여기에서 id 속성값을 google로 바꾸기
naverEl.setAttribute('id', 'google')
console.log(naverEl);

// -------------------------------------------------------

// 속성값 가져오기
const grapeEl = document.querySelector('#grape');
const grapeUrl = grapeEl.getAttribute('src');
console.log(grapeUrl);


// id가 test인 img태그를 포도 이미지가 보이도록 src 속성 수정하기
const testEl = document.querySelector('#test');
testEl.setAttribute('src', grapeUrl);


// CSS 지정
const fruitsLi = document.querySelectorAll('.fruit'); // 노드리스트로 반환
console.log(fruitsLi[0]);

// fruitsLi의 첫 번째 태그의 스타일 속성에서 backgroundColor를 red로 바꾸기
fruitsLi[0].style.backgroundColor = 'red';
fruitsLi[1].style.fontSize = '30px';

// for of 문 활용 모든 fruitsLi 요소 순회하면서 스타일 지정
for (let el of fruitsLi) {
    el.style.backgroundColor = 'skyblue';
    el.style.fontSize = '20px';
    el.style.fontWeight = 'bold';
}

// classList 활용
const h1El = document.querySelector('h1');
h1El.classList.add('title');
console.log(h1El);

// title 클래스 포함 여부 확인 후 불리언으로  반환
console.log(h1El.classList.contains('title')); 

h1El.classList.remove('title');
console.log(h1El.classList.contains('title'));

h1El.classList.toggle('title'); // title 클래스가 없다면 추가, 있다면 삭제
console.log(h1El.classList.contains('title'));

h1El.classList.toggle('title'); // title 클래스가 없다면 추가, 있다면 삭제
console.log(h1El.classList.contains('title'));


if(h1El.classList.contains('title')){
    console.log('이건 타이틀 이에요');
} else{
    console.log('이건 타이틀 아니에요');
}

// -------------------------------------------------------


// 요소 조회
const fruitsEl = document.querySelector('#fruits');

// 자식 요소 조회
console.log('자식 요소 조회', fruitsEl.children);
console.log('1번 인덱스 자식 요소 조회', fruitsEl.children[1]); // 인덱스로 접근 가능

// 형제 요소 조회
const sbEl = document.querySelector('#sb');

console.log('#sb 이전 요소', sbEl.previousElementSibling); // 사과 태그
console.log('#sb 다음 요소', sbEl.nextElementSibling); // 포도 태그
console.log('#sb 다다음 요소', sbEl.nextElementSibling.nextElementSibling); // 수박 태그


// -------------------------------------------------------

// 새로운 요소 생성
const newLi = document.createElement('li');
newLi.textContent = '내가 만든 li';
console.log(newLi);

// createElement는 그냥 하나의 태그를 만들었을 뿐 HTML에는 아직 삽입되지 않은 상태
console.log(document.body); 

// 요소 삽입
// fruitsEl.append(newLi); // fruitsEl라는 요소에 자식 중 가장 마지막으로 newLi가 삽입
// fruitsEl.appendChild(newLi); // 위랑 똑같은 동작을 함

// append와 appendChild의 차이
// fruitsEl.append('문자열 추가 가능');
// fruitsEl.appendChild('문자열 추가 불가');

// fruitsEl.append(newLi, newLi, newLi); // 여러 요소를 한번에 삽입 가능
// fruitsEl.appendChild(newLi, newLi, newLi); // 여러 요소를 한번에 삽입 불가

// append가 더 최신 메서드여서 현재는 더 선호되고 있음

fruitsEl.prepend(newLi); // fruitsEl라는 요소에 자식 중 가장 처음으로 newLi가 삽입

// 선택한 요소에 형제로 새로운 요소 추가
fruitsEl.before(newLi);
console.log(document.body); 

fruitsEl.after(newLi);
console.log(document.body); 

// 요소 삭제
const firstChild = document.querySelector("#fruits > li"); // <li class="fruit">사과</li>
fruitsEl.removeChild(firstChild); // 사과 li 삭제

// 자기 자신 삭제
fruitsEl.remove();
