let age = Number(prompt("나이를 입력하세요"));

if (age < 10){
    console.log("어린이");
} else if (age < 20) {
    console.log("청소년");
} else if (age < 30) {
    console.log("20대");
} else if (age < 40) {
    console.log("30대");
} else{
    console.log("중장년");
}


let now = new Date();
let hour = now.getHours();

if (hour < 12) {
  console.log("오전입니다");
} else {
  console.log("오후입니다");
}