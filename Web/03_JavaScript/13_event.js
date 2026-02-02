// div 선택
const div1 = document.querySelector("#div1");
const div2 = document.querySelector("#div2");
const div3 = document.querySelector("#div3");
const div4 = document.querySelector("#div4");

// addEventListener : 이벤트를 감지해서 함수를 실행
div1.addEventListener("click", () => alert("div1 클릭!"));
div2.addEventListener("mouseover", () => console.log("div2 마우스 오버!"));
div3.addEventListener("click", () => (div3.style.backgroundColor = "red"));
div4.addEventListener("click", changeDiv);

function changeDiv(){
    const divs = document.querySelectorAll("div");
    for (const div of divs){
        div.style.backgroundColor = "black";
        div.style.color = "white";
    }
}

// 이벤트 객체
// 브라우저에서 발생한 이벤트에 대한 정보를 담은 객체
const allDivs = document.querySelectorAll("div");
allDivs.forEach(div => {
    div.addEventListener("click", (e) => console.log("event", e));
});

const input = document.querySelector("input");
// input.value = "value"

input.addEventListener("keydown", (e) => {
    console.log("value", e.target);

    console.log("code", e.code);
})

// 폼 이벤트
const testForm = document.querySelector("#test-form");
testForm.addEventListener("submit", (e) => {
    e.preventDefault(); // 새로고침 발생 방지
    console.log("submit");
})

// onclick함수
function handleH1Click(){
    const h1 = document.querySelector("h1");
    h1.style.backgroundColor = "crimson";
}

