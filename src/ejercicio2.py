################
# Álvaro Arroyo - @alvaroarroyo19
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que reciba un número e
indique si el mismo es positivo,
negativo o cero utilizando sumas y restas.
"""


def signo(numero):

    numero = numero + 1

    if numero == 0:
        print("Neutro")

    elif numero < 0:
        print("Negativo")

    elif numero > 0:
        print("Positivo")

    return numero
