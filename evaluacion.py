import numpy as np
import math


# Realice una función que calcule el área de un cuadrado
def get_area_square(side):
    area = side*side
    return area


# Realice una función que calcule la hipotenusa
def get_hypotenuse(side1, side2):
    hypotenuse = math.sqrt((side1)**2+(side2)**2)
    return hypotenuse


# Obtenga el vector en orden inverso
def reverse_list(vector):
    result = []
    for i in range(0,len(vector)):
        newid = len(vector)-i
        result.append(vector[newid-1])
    return result


# Obtenga la posición o índice de los elementos
# de una lista mayores a un valor umbral
def get_indexes(vector, threshold):
    indexes = []
    for i in range(0,len(vector)):
        if vector[i] > threshold:
            indexes.append(i)
        else:
            pass
    return indexes


# Obtenga el valor máximo de una matriz
def get_max_value_from(matrix):
    #Se obtiene el valor máximo de la matriz.
    max_value = np.matrix.max(matrix)
    return max_value


# Obtenga los valores diagonales de una matriz
def get_diagonal_values_from(matrix):
    #Se obtienen los valores diagonales de la matriz.
    diagonal_values = np.diagonal(matrix)
    return diagonal_values

# Elimine los valores adyacentes a todo valor NaN
# INPUT = [6 10 5 8 9 NaN 23 9 7 3 21 43 NaN 4 6 7 8]
# OUTPUT = [6 10 5 8 9 7 3 21 6 7 8]
#Se supone que input y output son np.arrays, de igual forma.
def eliminar_NaN(INPUT):
    #Se crea un array de indices con NaN.
    indices = np.where(np.isnan(INPUT))[0]

    #Se genera un array de índices a eliminar.
    eliminar = []
    for i in indices:
        if i >0:
            eliminar.append(i-1)
        if i < len(INPUT):
            eliminar.append(i)
        if i < len(INPUT)-2:
            eliminar.append(i+1)

    eliminar = set(eliminar)

    #Se genera el array de output, sin NaN ni los adyacentes.
    OUTPUT = np.delete(INPUT, list(eliminar))
    return OUTPUT


# Replique los elementos de un vector
# n=2, A=[1 2 3] -> [1 1 2 2 3 3]
# n=0, A=[2 1] -> []
# Se supone que A es un np.array, ej.. A=np.array([a,b,c])
def funcion_Repetir(A,n):
    B = np.array([])
    B = np.repeat(A,n)
    return B



# Extraiga el primer digito distinto a cero, de cada valor en un vector
# x = [1 0.3 -2 0.001 -0.0006, 582398, 3020]
# y = [1 3 2 1 6 5 3]
#Se supone que el vector x es un np.array, x=np.array([1 0.3 -2 0.001 -0.0006, 582398, 3020])
#Se genera una función para discriminar si un valor es distinto de 0, "," o ".".
def primer_Digito(numero):
    num_str = str(abs(numero))
    for digito in num_str:
        if (digito != '0'):
            if (digito != '.'):
                if (digito != ','):
                    return digito
                pass
            pass
        pass

#Se genera una segunda función, que llama a la primera y vectoriza sus resultados.
def vector_Resultado(x):
    y = np.vectorize(primer_Digito)(x)
    return y




# Elimine los elementos redundantes en un vector, manteniendo el orden original
# in = [5 3 6 4 7 7 3 5 9]
# out = [5 3 6 4 7 9]
#Se supone que el vector in es un np.array, es decir. in = np.array([5 3 6 4 7 7 3 5 9])
#Por sintaxis, se cambia in por x, out por y.
def quitar_Redundantes(x):
    #Definimos tuple que almacena los valores de y, así como los índices.
    #Almacenamos sólo valores originales.
    y, indices = np.unique(x, return_index=True)
    #Ordenamos los índices obtenidos.
    indices_acomodados = np.argsort(indices)
    #Regresamos el vector "y" con los valores acomodados en el orden original.
    return y[indices_acomodados]


