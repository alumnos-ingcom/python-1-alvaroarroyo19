################
# Álvaro Arroyo - @alvaroarroyo19
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit como un número decimal,
utilice esta formula para calcular los grados centígrados y retorne el resultado obtenido. Y viceversa.
"""



def convertir_a_fahrenheit(centigrados):
    formula_f = (centigrados * 9/5) + 32
    return formula_f

def convertir_a_centigrados(fahrenheit):
    formula_g = (fahrenheit - 32) * 5/9
    return formula_g



def principal():

    """
    Esta función es la que inicia el programa, se encarga de la entrada,
    la llamada al algoritmo y la salida 
    """

    print("----------------------")
    print("Este es el conversor de temperaturas")
    print("")
    print("Pulse 1 si desea convertir centígrados a fahrenheit")
    print("")
    print("Pulse 2 si desea convertir fahrenheit a centígrados")
    print("")
    salida = input("¿Qué desea convertir?: ")
    print("")

    seleccion = salida

    while seleccion != "1" and seleccion !="2":
        print("¡Elección equivocada!")
        principal()

    if seleccion == "1":
        centigrados = float(input("Ingrese un número en centígrados: "))
        print(convertir_a_fahrenheit(centigrados))

    if seleccion == "2":
        fahrenheit = float(input("Ingrese un número en fahrenheit: "))
        print(convertir_a_centigrados(fahrenheit))


if __name__ == "__main__":
    principal()
