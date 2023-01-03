# Condicionales

""" 
Nota: else es opcional si quiero que se ejecute algo si falla la condicion

if condicion:
    sentencias

if condicion:
    sentencias
else: 
    sentencias

if condicion:
    sentencias
elif condicion:
    sentencias
elif condicion:
    sentencias
else:
    sentencias

and = and
or = or
not = not

"""

a = 5
b = 6
c = 10

if a > b:
    print("Verdadero")

if a == b:
    print("Verdadero")
else:
    print("Falso")


if a > b and a > c:
    print("El mayor es A")
elif b > c:
    print("El mayor es B")
else:
    print("El mayor es C")


""" 
Operadores de Comparacion:

==
!=
>=
<=
>
<

Operadores Logicos:

true and true = true
true and false = false
false and false = false

true or true = true
true or false = true
false or false = false

not true and not true = false
not true and not false = false
not false and not false = true

not true or not true = false
not true or not false = true
not false or not false = true


"""

if a > b and a > c:
    pass

if a > b or a > c:
    pass

if not a > b and not a > c:
    pass
