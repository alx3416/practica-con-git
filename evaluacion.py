import numpy as np

# Realice una función que calcule el área de un cuadrado
def get_area_square(side):
    if side <= 0:
        area = 0
        print("Largo debe ser mayor a cero")
    else:
        area = side * side
    return area

print(get_area_square(3))


# Realice una función que calcule la hipotenusa
def get_hypotenuse(side1, side2):
    hypotenuse = np.sqrt(side1**2 + side2**2)
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
    max_value = max(max(row) for row in matrix)
    return max_value


# Obtenga los valores diagonales de una matriz
def get_diagonal_values_from(matrix):
    diagonal_values = [matrix[i][i] for i in range(len(matrix))]
    return diagonal_values

# Elimine los valores adyacentes a todo valor NaN
# INPUT = [6 10 5 8 9 NaN 23 9 7 3 21 43 NaN 4 6 7 8]
# OUTPUT = [6 10 5 8 9 7 3 21 6 7 8]

# Replique los elementos de un vector
# n=2, A=[1 2 3] -> [1 1 2 2 3 3]
# n=0, A=[2 1] -> []

# Extraiga el primer digito distinto a cero, de cada valor en un vector
# x = [1 0.3 -2 0.001 -0.0006, 582398, 3020]
# y = [1 3 2 1 6 5 3]

# Elimine los elementos redundantes en un vector, manteniendo el orden original
# in = [5 3 6 4 7 7 3 5 9]
# out = [5 3 6 4 7 9]
