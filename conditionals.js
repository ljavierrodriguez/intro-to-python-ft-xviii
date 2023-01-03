// Condicionales
/* 
Nota: else es opcional si quiero que se ejecute algo si falla la condicion

if(condicion){
    sentencias
}

if(condicion){
    sentencias
} else {
    sentencias
}

if(condicion){
    sentencias
}else if(condicion){
    sentencias
}else if(condicion){
    sentencias
} else {
    sentencias
}

switch(valor){
    case 1: sentencias;
        break;
    default: sentencia;
        break;
}

and = &&
or = ||
not = !

*/

let a = 5;
let b = 6;
let c = 10;

if(a > b){
    console.log("Verdadero");
}

if(a === b){
    console.log("Verdadero")
} else {
    console.log("Falso")
}

if(a > b && a > c){
    console.log("El mayor es A")
} else if (b > c){
    console.log("El mayor es B")
} else {
    console.log("El mayor es C")
}

/* 
Operadores de Comparacion:

===
==
!==
!=
>=
<=
>
<

Operadores Logicos:

true && true = true
true && false = false
false && false = false

true || true = true
true || false = true
false || false = false

!true && !true = false
!true && !false = false
!false && !false = true

!true || !true = false
!true || !false = true
!false || !false = true

*/