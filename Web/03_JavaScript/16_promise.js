/*
promise
- 비동기 함수를 동기 처리하기 위해 만든 객체
- 미래에 실패/성공에 대한 결과 값을 "약속" 한다는 의미
- 성공, 실패 분리해서 반환
    - 성공, 실패에 대한 결과는 then, catch 메서드로 이어 받아서 처리 가능
- > 성공이던 실패던 무언가의 "최종 결과" 
*/

///////////////////////////////////////////////////////////////////

// 1. promise를 생성하는 코드
function promise1(flag){
    return new Promise(function(resolve, reject){
        if (flag){
            resolve(`현재 프로미스의 상태는 fulfilled(이행)! then 메서드로 연결~ 이 때 flag 값은 ${flag}!`,)
        } else{
            reject(`현재 프로미스의 상태는 rejected(거절)! catch 메서드로 연결~ 이 때 flag 값은 ${flag}!`,)
        }
    })
}


// 2. promise 사용 코드
promise1(5 > 3) 
   .then(function(result){
    console.log(result);
   })
   .catch(function(error){
    console.log(error);
   });

// 프로미스 예제
function goMart(){
    console.log('마트에 가서 어떤 음료 살지 고민...');
}

function pickDrink(callback){
    return new Promise((resolve, reject) => {
    // 3초 고민 후에 결정
        setTimeout(function(){
            console.log("고민끝!")
            product = "제로콜라";
            price = 2000;
            resolve(); // 매개변수로 넘긴 콜백함수를 실행
        }, 3000);
    });
}

function pay(){
    console.log(`상품명: ${product}, 가격: ${price}` );
}

let product;
let price;
goMart();
pickDrink().then(pay);

//////////////////////////////////////////////////////////

// 프로미스 체이닝

function add(n1, n2) {
  return new Promise(function (resolve, reject) {
    setTimeout(function () {
      const result = n1 + n2;
      resolve(result);
    }, 1000);
  });
}

function mul(n) {
  return new Promise(function (resolve, reject) {
    setTimeout(function () {
      const result = n * 2; // 14
      //   resolve(result); // resolve(14)
      reject(new Error('의도적으로 발생시킨 에러!!!'));
    }, 700);
  });
}

function sub(n) {
  return new Promise(function (resolve, reject) {
    setTimeout(function () {
      const result = n - 1;
      resolve(result); // resolve(13)
    }, 500);
  });
}

add(4, 3)
  .then(function (result) {
    console.log('1: ', result); // 7
    return mul(result); // return mul(7)
  })
  .then(function (result) {
    console.log('2: ', result); // 14
    return sub(result); // return sub(14)
  })
  .then(function (result) {
    console.log('3: ', result); // 13
  })
  .catch(function (error) {
    console.log(error);
  });