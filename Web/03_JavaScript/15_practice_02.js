// setTimeout(function(){
//     document.body.style.backgroundColor = 'red';
//     setTimeout(function(){
//         document.body.style.backgroundColor = 'orange';
//         setTimeout (function (){
//             document.body.style.backgroundColor = 'yellow';
//             setTimeout(function(){
//                 document.body.style.backgroundColor = 'green';
//                 setTimeout(function(){
//                     document.body.style.backgroundColor = 'blue';
//                 }, 1000);
//             }, 1000);
//         }, 1000);
//     }, 1000);
// }, 1000);



/////////////////////////////////////////////////////////////

function Color(color) {
    return new Promise((resolve) => {
        setTimeout(function () {
            document.body.style.backgroundColor = color;
            resolve();
        }, 1000);
    });
}

Color('red')
    .then(() => Color('orange'))
    .then(() => Color('yellow'))
    .then(() => Color('green'))
    .then(() => Color('blue'));