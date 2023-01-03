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

for(let nombre of nombres){
    console.log(nombre);
}

let index = 0;
while(index < nombres.length){
    console.log(nombres[index]);
    index++;
}

let i = 0;
do {
    console.log(nombres[i]);
    i++;
} while(i < nombres.length);

