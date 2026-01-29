const user = {
    name : '이몽룡',
    age : 18,
    like : ['강아지', '고양이'],
    isMarried : true,
    girlfriend : {
        name : '성춘향',
        age : 16
    }    
};

console.log(user); 


console.log("===")

let mathScore = "77";
let engScore = "88";

let avgScore1 = (Number(mathScore) + Number(engScore)) / 2;
let avgScore2 = (parseInt(mathScore) + parseInt(engScore)) / 2;
let avgScore3 = (parseFloat(mathScore) + parseFloat(engScore)) / 2;

console.log(avgScore1);
console.log(avgScore2);
console.log(avgScore3);