"""
Introducción a los Bloques condicionales.

Un bloque condicional puede comprobar varias condiciones
"""
import sys


numero1 = input("Introduzca un primer número entre 1 y 10: ")
numero2 = input("Introduzca un segundo número entre 1 y 10: ")

try:
    numero1 = int(numero1)
    numero2 = int(numero2)
except:
    print("La conversión de al menos uno de los números no ha tenido éxito",
          file=sys.stderr)
    sys.exit()

# Realizar la comparación
if 0 < numero1 < 11:
    print("El número", numero1, "está comprendido entre 1 y 10")

if 1 <= numero2 <= 10:
    print("El número", numero2, "está comprendido entre 1 y 10")

