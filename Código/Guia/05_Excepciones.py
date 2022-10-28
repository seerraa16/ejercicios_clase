"""
Introducción a las excepciones
"""
import sys

# Primer número
numero1 = input("Escriba un primer número: ")
try:
    numero1 = int(numero1)
except:
    print("La conversión de al menos uno de los números no ha tenido éxito",
          file=sys.stderr)
    sys.exit()

# Second numero
try:
    numero2 = int(input("Escriba un segundo número: "))
except ValueError as e:
    print("La conversión de al menos uno de los números no ha tenido éxito",
          file=sys.stderr)
    sys.exit()

# Realizar la comparación
comparacion = numero1 < numero2

print(numero1, "<", numero2, ":", comparacion)

