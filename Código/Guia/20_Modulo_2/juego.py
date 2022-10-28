"""
Módulo que agrupa las funciones que describen la lógica interna del juego
"""

from entrada import (
    pedir_entrada_numero,
    pedir_entrada_numero_delimitado,
    pedir_entrada_si_o_no,
)


def jugar_una_vez(numero, minimo, maximo):
    intento = pedir_entrada_numero_delimitado("Adivine el numero", minimo, maximo)

    # Se comprueba si el intento es correcto o no
    if intento < numero:
        print("Demasiado pequeño")
        minimo = intento + 1
        victoria = False
    elif intento > numero:
        print("Demasiado grande")
        maximo = intento - 1
        victoria = False
    else:
        print("¡Ha ganado!")
        victoria = True
        minimo = maximo = intento
    return victoria, minimo, maximo


def pedir_entrada_del_numero_incognita(minimo, maximo):
    return pedir_entrada_numero_delimitado("Introduzca el número a adivinar",
                                        minimo, maximo)


def jugar_una_partida(numero, minimo, maximo):
    while True:
        # Se entra en un bucle infinito
        # que permite jugar varias veces

        victoria, minimo, maximo = jugar_una_vez(numero, minimo, maximo)

        if (victoria):
            return


def decidir_limites():
    while True:
        minimo = pedir_entrada_numero("Quelle est la borne minimale ?")
        maximo = pedir_entrada_numero("Quelle est la borne maximale ?")
        if maximo > minimo:
            return minimo, maximo


def jugar():
    minimo, maximo = decidir_limites()
    while True:
        numero = pedir_entrada_del_numero_incognita(minimo, maximo)
        jugar_una_partida(numero, minimo, maximo)
        if not pedir_entrada_si_o_no("¿Desea jugar una nueva partida?"):
            print("¡Hasta pronto!")
            return

