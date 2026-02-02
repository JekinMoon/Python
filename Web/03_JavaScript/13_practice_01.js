const button = document.querySelector('button');
const h2 = document.querySelector('h2');

//  버튼을 "클릭"했을 때
button.addEventListener('click', function () {
  // red, green, blue 변수에 각각 0 ~ 255 범위의 랜덤한 숫자 생성
  let r = Math.floor(Math.random() * 256);
  let g = Math.floor(Math.random() * 256);
  let b = Math.floor(Math.random() * 256);
  const newColor = `rgb(${r}, ${g}, ${b})`; // rgb(red, green, blue) 형태로 문자열을 newColor 변수에 저장하기

  document.body.style.backgroundColor = newColor; // 배경색 변경하기
  h2.innerText = newColor; // newColor 변수에 저장한 rgb() 컬러 코드를 h2의 내용(content)으로 바꾸기
});