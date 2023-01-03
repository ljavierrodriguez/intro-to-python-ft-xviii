# loops o ciclos
"""  
for x in collection:
    sentences

while condition:
    sentences

"""
nombres = ['Hugo', 'Paco', 'Luis']


# valores por default en range(start=0, stop=10, step=1)
for i in range(1, 11): # start = 1, stop=11, step=1 
    print(i)

print('#### FOR IN ####')
for nombre in nombres:
    print(nombre)

print('#### FOR IN RANGE ####')
for index in range(len(nombres)):
    print(nombres[index])

print('#### WHILE ####')
index = 0
while index < len(nombres):
    print(nombres[index])
    index+=1
    # index = index + 1


numbers = [1, 2, 3, 4, 5]

result = [number*2 for number in numbers]
print(result)

alumnos = [
    {"id": 1, "name": "Hugo"},
    {"id": 2, "name": "Paco"},
    {"id": 3, "name": "Luis"}
]

ids = [alumno["id"] for alumno in alumnos]
print(ids)

print("IDs using for in:")
ids = []
for alumno in alumnos:
    ids.append(alumno["id"])
print(ids)

matrix = [
    [1, 2, 3], 
    [4, 5, 6],
    [6, 7, 8]
]

print(matrix[0][0])
print(matrix[2][2])

print("----- for in ------")
for row in matrix:
    for col in row:
        print(col)

print("----- for in range ------")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])

print("----- while ------")
i = 0
while(i < len(matrix)):
    j = 0
    while(j < len(matrix[i])):
        print(matrix[i][j])
        j+=1
    i+=1