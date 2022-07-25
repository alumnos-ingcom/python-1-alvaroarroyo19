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


def principal():
    """
    Esta función es la que inicia el programa, se encarga de la entrada,
    la llamada al algoritmo y la salida 
    """
    numero = int(input("Ingrese un número positivo o negativo "))
    resultado = signo(numero)


if __name__ == "__main__":
    principal()
