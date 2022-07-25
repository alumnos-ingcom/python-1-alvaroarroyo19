################
# Álvaro Arroyo - @alvaroarroyo19
# UNRN Andina - Introducción a la Ingenieria en Computación
################

'''
Escribir una función que utilizando sumas y restas,
reciba dos valores y retorne:
'''

def compara(numero, otro_numero):

    numero = numero + 1
    otro_numero = otro_numero + 1

    if numero > otro_numero:
        print("1")

    elif numero < otro_numero:
        print("-1")

    else:
        print("0")

    return numero and otro_numero


def principal():
    """
    Esta función es la que inicia el programa, se encarga de la entrada,
    la llamada al algoritmo y la salida 
    """

    numero = int(input("Ingrese un número "))
    otro_numero = int(input("Ingrese otro número "))

    resultado = compara(numero, otro_numero)
    return resultado

if __name__ == "__main__":
    principal()
