from itertools import chain, product, repeat, cycle

lista = list("abc")

print("1\ Recorrido clásico de una lista")
for letra in lista:
    print(letra)

print("2\ Si necesitamos un índice")
for indice, letra in enumerate(lista):
    print("índice {}, letra {}".format(indice, letra))

print("3\ No hacer esto")
array = [lista, lista]

array[0][0] = "X"
print("array = {}".format(array), "lista = {}".format(lista), sep="\n")

print("4\ Recorrer un array")
lista = list("abc")

array = [lista[:], [c.upper() for c in lista]]

for linea in array:
    for case in linea:
        print(case)

print("5\ Recorrer plano un array")
for case in chain.from_iterable(array):
    print(case)

print("6\ Si necesitamos un índice")
for i, linea in enumerate(array):
    for j, case in enumerate(linea):
        print("array[{}][{}] = {}".format(i, j, case))

print("7\ Recorrido por columna y luego por fila")
transpose = zip(*array)

for j, columna in enumerate(transpose):
    for i, case in enumerate(columna):
        print("array[{}][{}] = {}".format(i, j, case))

print("8\ Arrays creados virtualmente mediante el cruce de dos listas")
lineas = array[1][:]
columnas = [1, 2, 3]

for linea, columna in product(lineas, columnas):
    print("Casilla {}{}".format(linea, columna))

print("9\ Cruzar una lista con un dato único por el producto")
for linea, columna in product("Z", columnas):
    print("Casilla {}{}".format(linea, columna))

print("10\ Cruzar una lista con un dato único por uan repetición")
for linea, columna in zip(repeat("Z"), columnas):
    print("Casilla {}{}".format(linea, columna))

print("11\ Cruzar una lista con otra cíclica")
for numero, letra in zip(range(10), cycle("ABC")):
    print("Casilla {}{}".format(letra, numero))

