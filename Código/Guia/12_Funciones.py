"""
Ejercicio: construir un juego "Guess The number"

PARTE 1: Pedir al usuario que introduzca un numero entre 0 y 100
PARTE 2: Hacer que el usuario adivine el número

Utilizar una función para aprovechar el código común
"""

def pedir_numero():
    while True:
        # Se entra en un bucle infinito
        # que permite corregir un error de entrada

        # Se pide un número
        entrada = input("Introduzca un número entre 0 y 99 incluidos: ")

        try:
            entrada = int(entrada)
        except:
            pass
        else:
            # Realizar la comparación
            if 9 <= entrada <= 99:
                # Tenemos lo que queríamos, se sale del bucle
                break
    return entrada


# PARTE 1
print("Introduzca el número a adivinar")
numero = pedir_numero()


# PARTE 2
print("Intente encontrar el número a adivinar")
while True:
    # Se entra en un bucle infinito
    # que permite jugar varias veces

    intento = pedir_numero()

    # Se comprueba si el intento es correcto o no
    if intento < numero:
        print("Demasiado pequeño")
    elif intento > numero:
        print("Demasiado grande")
    else:
        print "¡Ha ganado!"
        break

