// functions
/* 

function funcName(){

}

const funcName = function(){

}

*/

function saludo(){
    console.log('Hello');
}

saludo();

function sumar(a, b){
    return a + b;
}

const sumar2 = function(a, b){
    return a + b
}

function restar(a, b = 10) {
    return a - b
}

restar(30)
restar(10, 5)