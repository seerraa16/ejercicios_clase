"""
Ejercicio: construir un juego "Guess The number"

PARTE 1: Pedir al usuario que introduzca un número entre 0 y 100
PARTE 2: Hacer que el usuario adivine el número

"""

# PARTE 1

# Para el ejercicio del primer capítulo, hay que utilizar lo siguiente:
# import random
# numero = random.randint(0, 100)

# Para la evidencia del segundo capítulo, hay que utilizar lo siguiente:
print("Introduzca el número a adivinar")
while True:
    # Entramos en un bucle infinito

    # Se pide la entrada de un número
    numero = input("Introduzca un número entre 0 y 99 incluidos: ")

    try:
        numero = int(numero)
    except:
        pass
    else:
        # Realizar la comparación
        if 0 <= numero <= 99:
            # Tenemos lo que queremos, salimos del bucle
            break

# PARTE 2
print("Intente encontrar el número a adivinar")
while True:  # BUCLE 1
    # Entramos en un BUCLE infinito
    # que permite jugar varias veces

    while True:  # BUCLE 2
        # Entramos en un BUCLE infinito
        # que permite corregir un error en la entrada

        # Se pide introducir un número
        intento = input("Introduzca un número entre 0 y 99 incluidos: ")

        try:
            intento = int(intento)
        except:
            pass
        else:
            # Realizar la comparación
            if 0 <= intento <= 99:
                # Tenemos lo que queremos, salimos del BUCLE 2
                break

    # Comprobamos si el intento es correcto o no
    if intento < numero:
        print("Demasiado pequeño")
    elif intento > numero:
        print("Demasiado grande")
    else:
        print("¡Ha ganado!")
        # Hemos terminado, salimos del BUCLE 1
        break

