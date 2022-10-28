"""
Ejercicio: construir un juego "Guess The number"

PARTE 1: Pedir al usuario que introduzca un número entre 0 y 100
PARTE 2: Hacer que el usuario adivine el número

Utilizar una función para aprovechar el código común
"""

MIN = 0
MAX = 99


def pedir_numero(invitacion, minimo, maximo):
    # Completar la invitación:
    invitacion += " entre " + str(minimo) + " y " + str(maximo) + " incluidos: "

    while True:
        # Se entra en un bucle infinito

        # Se pide un número
        entrada = input(invitacion)

        try:
            entrada = int(entrada)
        except:
            pass
        else:
            # Realizar la comparación
            if minimo <= entrada <= maximo:
                # Tenemos lo que queríamos, se sale del bucle
                break
    return entrada


# PARTE 1
numero = pedir_numero("Introduzca el número a adivinar", MIN, MAX)


# PARTE 2
while True:
    # Se entra en un bucle infinito
    # que permite jugar varias veces

    intento = pedir_numero("Adivine el número", MIN, MAX)

    # Se comprueba si el intento es correcto o no
    if intento < numero:
        print("Demasiado pequeño")
    elif intento > numero:
        print("Demasiado grande")
    else:
        print("¡Ha ganado!")
        break

