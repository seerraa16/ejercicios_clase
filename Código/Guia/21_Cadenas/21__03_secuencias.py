frase = input("Introduzca una frase: ")
# Ejemplo con eStE es el abc de b_a_ba

print("Las palabras son las siguientes:")
palabras = frase.split()
for palabra in palabras:
    print(palabra)

# eStE
# es
# el
# abc
# de
# b_a_ba


separador = input("Introduzca una cadena de separación: ")
# _

print("Utilizando este separador, he aquí las palabras encontradas:")
palabras = frase.split(separador)
for palabra in palabras:
    print(palabra)

# Utilizando este separador, he aquí las palabras encontradas:
# eStE el el abd de b
# a
# ba


union = input("Seleccionar con qué unirlas: ")
# *

print("He aquí la palabra unida:")
print(union.join(palabras))

# He aquí la palabra unida:
# eStE es el abc de b*a*ba

