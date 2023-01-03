// loops o ciclos
/* 

for(counter; condition; increment){
    sentences
}

for(index in collection){
    sentences
}

for(value of collection){
    sentences
}

while(condition){
    sentences
}

do {
    sentences
} while (condition)

*/
let nombres = ['Hugo', 'Paco', 'Luis'];

for(let i = 0; i < nombres.length; i++){
    console.log(nombres[i]);
}

for(let index in nombres){
    console.log(nombres[index]);
}

