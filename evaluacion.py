import numpy as np


# Realice una función que calcule el área de un cuadrado
def get_area_square(side):
    area = side * side
    return area


# Realice una función que calcule la hipotenusa
def get_hypotenuse(side1, side2):
    hypotenuse = (side1 ** 2 + side2 ** 2) ** 0.5
    return hypotenuse


# Obtenga el vector en orden inverso
def reverse_list(vector):
    result = vector[::-1]
    return result


# Obtenga la posición o índice de los elementos
# de una lista mayores a un valor umbral
def get_indexes(vector, threshold):
    indexes = [i for i, value in enumerate(vector) if value > threshold]
    return indexes


# Obtenga el valor máximo de una matriz
def get_max_value_from(matrix):
    flat_matrix = [item for sublist in matrix for item in sublist]
    max_value = max(flat_matrix)
    return max_value


# Obtenga los valores diagonales de una matriz
def get_diagonal_values_from(matrix):
    diagonal_values = [matrix[i][i] for i in range(min(len(matrix), len(matrix[0])))]
    return diagonal_values

# Elimine los valores adyacentes a todo valor NaN
# INPUT = [6 10 5 8 9 NaN 23 9 7 3 21 43 NaN 4 6 7 8]
# OUTPUT = [6 10 5 8 9 7 3 21 6 7 8]

def remove_adjacent_to_nan(input_list):
    result = []
    skip_next = False

    for value in input_list:
        if skip_next:
            skip_next = False
            continue
        
        if not np.isnan(value):
            result.append(value)
        else:
            skip_next = True

    return result

# Replique los elementos de un vector
# n=2, A=[1 2 3] -> [1 1 2 2 3 3]
# n=0, A=[2 1] -> []

def replicate_elements(vector, n):
    if n == 0:
        return []
    
    result = []
    for value in vector:
        result.extend([value] * n)
    return result

# Extraiga el primer digito distinto a cero, de cada valor en un vector
# x = [1 0.3 -2 0.001 -0.0006, 582398, 3020]
# y = [1 3 2 1 6 5 3]

def extract_first_nonzero_digit(vector):
    result = []
    for value in vector:
        # Convertimos el valor a string para poder acceder a cada dígito individualmente
        value_str = str(value)
        # Buscamos el primer dígito distinto de cero
        for char in value_str:
            if char != '0' and char != '.' and char != '-':
                result.append(int(char))
                break
    return result

# Elimine los elementos redundantes en un vector, manteniendo el orden original
# in = [5 3 6 4 7 7 3 5 9]
# out = [5 3 6 4 7 9]
def remove_redundant_elements(vector):
    result = []
    seen = set()
    for value in vector:
        if value not in seen:
            result.append(value)
            seen.add(value)
    return result