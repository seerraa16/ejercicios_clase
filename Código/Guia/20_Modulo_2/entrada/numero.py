"""
Módulo que agrupa todas las funcionalidades
que permiten pedir entrada de números
"""


import sys


MIN=0
MAX=100


def pedir_entrada_numero(invitacion):
    """
    Esta función verifica que se ha obtenido un número
    """
    while True:
        # Se entra en un bucle infinito

        # Se pide la entrada de un número
        print(invitacion, end=": ")
        entrada = input()

        try:
            entrada = int(entrada)
        except:
            print("Solo los caracteres [0-9] están autorizados.", file=sys.stderr)
        else:
            # Tenemos lo que queremos, salimos del bucle saliendo de la función
            return entrada

def pedir_entrada_numero_delimitado(invitacion, minimo=MIN, maximo=MAX):
    """
    Esta función utiliza la anterior y agrega una post-condición
    sobre los extremos del número a introducir
    """
    while True:
        # Se entra en un bucle infinito

        # Se pide la entrada de un número
        invitacion = "{} entre {} y {} incluidos".format(invitacion, minimo, maximo)
        entrada = pedir_entrada_numero(invitacion)

        if minimo <= entrada <= maximo:
            # Tenemos lo que queremos, salimos del bucle saliendo de la función
            return entrada

