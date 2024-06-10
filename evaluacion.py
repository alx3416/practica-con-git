import numpy as np


# Realice una función que calcule el área de un cuadrado
def get_area_square(side):
    area = side ** 2
    return area


# Realice una función que calcule la hipotenusa
def get_hypotenuse(side1, side2):
    hypotenuse = sqrt((side1 ** 2) + (side2 ** 2))
    return hypotenuse


# Obtenga el vector en orden inverso
def reverse_list(vector):
    result = vector[::-1]
    return result


# Obtenga la posición o índice de los elementos
# de una lista mayores a un valor umbral
def get_indexes(vector, threshold):
    indexes = []
    indexed_list = enumerate(vector)
    for index, item in indexed_list:
        if item > threshold:
            indexes.append(index)
    return indexes


# Obtenga el valor máximo de una matriz
def get_max_value_from(matrix):
    max_value = matrix.max()
    return max_value


# Obtenga los valores diagonales de una matriz
def get_diagonal_values_from(matrix):
    diagonal_values = matrix.diagonal()
    return diagonal_values

# Elimine los valores adyacentes a todo valor NaN
# INPUT = [6 10 5 8 9 NaN 23 9 7 3 21 43 NaN 4 6 7 8]
# OUTPUT = [6 10 5 8 9 7 3 21 6 7 8]
def get_adyacent_values(input_list, pivot):
    output_list = input_list.copy()
    indexed_list = enumerate(input_list)
    pivot_indices = [index for index, item in indexed_list if item == pivot]
    #print(pivot_indices)
    for index in pivot_indices[::-1]:
        output_list.pop(index + 1)
        output_list.pop(index)
        output_list.pop(index - 1)
    return output_list

# Replique los elementos de un vector
# n=2, A=[1 2 3] -> [1 1 2 2 3 3]
# n=0, A=[2 1] -> []
def replicate_elements(vector, n):
    if n <= 0:
        return []
    else:
        output_list = [item1 for item2 in range(n+1) for item1 in [item2]*n]

# Extraiga el primer digito distinto a cero, de cada valor en un vector
# x = [1 0.3 -2 0.001 -0.0006, 582398, 3020]
# y = [1 3 2 1 6 5 3]

# Elimine los elementos redundantes en un vector, manteniendo el orden original
# in = [5 3 6 4 7 7 3 5 9]
# out = [5 3 6 4 7 9]
