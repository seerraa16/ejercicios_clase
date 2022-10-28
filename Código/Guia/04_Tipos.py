"""
Conversión a entero y comparación

(probar con una entrada que no sea un número)
"""

# Primer número
numero1 = input("introduzca un primer número: ")
numero1 = int(numero1)

# Segundo número
numero2 = int(input("Introduzca un segundo número: "))

# Realizar la comparación
comparacion = numero1 < numero2

print(numero1, "<", numero2, ":", comparacion)

