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
