// function call(name, cb){
//     setTimeout(function (){
//         console.log(name);
//         cb(name);
//     }, 1000);
// }

// function back(cb) {
//     setTimeout(function () {
//         console.log('back');
//         cb('back');
//     }, 1000);
// }

// function hell(cb) {
//     setTimeout(function () {
//         cb('callback hell');
//     }, 1000);
// }

// call('kim', function(name){
//     console.log(name + '반가워');
//     back(function (txt){
//         console.log(txt + '을 실행했구나');
//         hell(function(message) {
//             console.log('여기는 ' + message);
//         });
//     });
// });

////////////////////////////////////////////////////////////////
//promise로 변경

function call(name){
    return new Promise((resolve) => {
        setTimeout(function (){
        console.log(name);
        resolve(name);
        }, 1000);
    });
}

function back() {
    return new Promise((resolve) => {
        setTimeout(function () {
        console.log('back');
        resolve('back');
        }, 1000);
    });
}

function hell() {
    return new Promise((resolve) => {
        setTimeout(function () {
            resolve('callback hell');
        }, 1000);
    });
}

call('kim')
    .then(function(name){
        console.log(name + '반가워');
        return back();
    })
    .then(function(txt){
        console.log(txt + '을 실행했구나');
        return hell();
    })
    .then(function(message){
        console.log('여기는 ' + message);  
    });

    //////////////////////////////////////////////////////////
// async await으로 변경

async function exec() {
    let name = await call('kim');
    console.log(name + '반가워');

    let txt = await back();
    console.log(txt + '을 실행했구나');

    let message = await hell();
    console.log('여기는 ' + message);
}

exec();

async function exec() {
    let name = await call('kim');
    console.log(name + '반가워');

    const result = await back();
    console.log(`${result}를 실행했구나`);

    const msg = await hell();
    console.log(`여기는 ${msg}`);
}
