################
# Alvaro Arroyo - @alvaroarroyo19
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que haga la suma entre dos números enteros sin hacer la operación de manera directa. 
Esto quiere decir que para hacer la suma entre 4 y 3, las operaciones resultantes deberán ser 4+1+1+1.
"""


def suma_lenta(numero, otro_numero):

    print(numero)

    for i in range(otro_numero):
        print("+ 1")

        numero = numero + 1

    print(f'= {numero}')

    return numero

def principal():
    """
    Esta función es la que inicia el programa, se encarga de la entrada,
    la llamada al algoritmo y la salida 
    """

    numero = int(input("Ingrese un número "))
    otro_numero = int(input("Ingrese otro número "))

    resultado = suma_lenta(numero, otro_numero)

    return resultado

if __name__ == "__main__":
    principal()
