# No usa palabra reservada para definir variables

nombre = "Luis" # 'Luis' '''Luis'''

apellido = 'Rodriguez'

comentario = ''' Lorem ipsum dolor sit amet consectetur adipisicing elit. 
Enim nisi ipsam vitae molestias adipisci repudiandae molestiae illo officia. 
Tempore est sint beatae quibusdam error atque libero temporibus earum dicta sunt! '''

edad = 40
saldo = 10.30
temp = -10.4

active = True
soltero = False

direccion = None # Undefined or Null

person = {
    "name": "",
    "lastname": "",
    "age": 0,
}

person['name'] = 'Luis'

nombres = ["Hugo", "Paco", "Luis"] # list

nombres[0]

nombres.append("Donald")

status = ('active', 'inactive', 'suspended', 'canceled', 'completed') # tuple

status[0]

frutas = { "Pera", "Manzana", "Uva", "Limon", "Chirimoya" } # set

print(type(nombres)) # Saber que tipo de variable es 
print(dir(nombres))