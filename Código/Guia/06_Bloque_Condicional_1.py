"""
Introducción a los Bloques condicionales.

Un bloque es una sección de código intentado de manera diferente

Un bloque condicional se ejecuta si una confición es verdadera
"""
import sys

try:
    numero1 = int(input("Introduzca un primer número: "))
    numero2 = int(input("Introduzca un segundo número: "))
except ValueError as e:
    print("La conversión de al menos uno de los números no ha tenido éxito",
          file=sys.stderr)
    sys.exit()

# Realizar la comparación
if numero1 == numero2:
    print(numero1, "==", numero2)
else:
    print(numero1, "!=", numero2)

