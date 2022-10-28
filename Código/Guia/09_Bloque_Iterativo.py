"""
Introducción a los Bloques iterativos.

Un bloque iterativo permite repetir una acción de 0 a n veces.
"""

numero = input("Introduzca un número entre 1 y 10: ")

try:
    numero = int(numero)
except:
    numero = 0

while not 1 <= numero <= 10:
    # El número no es válido

    # Se pide volver a introducir el número
    numero = input("Introduzca un número entre 1 y 10: ")

    try:
        numero = int(numero)
    except:
        numero = 0

print("Estamos seguros de que", numero, "es un número y está comprendido entre 1 y 10 incluidos.")

