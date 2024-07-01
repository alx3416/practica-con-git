
import math
import numpy as np

#ealice una funcion que calcule el area de un cuadrado
def get_area_square(side):

        area = side * side
        return area

# side = int(input("Ingrese lado del cuadrado: "))
area = get_area_square(side)
print("El Area del cuadrado con lado", side, "es:", area)
print("\n ")

# Realice una función que calcule la hipotenusa
def get_hypotenuse(side1, side2):

    hipotenusa = math.sqrt(side1 ** 2 + side2 ** 2)
    return hipotenusa

side1 = int(input("Ingrese lado1 del TRect: "))
side2 = int(input("Ingrese lado2 del TRect: "))

hipotenusa = get_hypotenuse(side1, side2)
print("Hypotenus de catetos", side1,side2,  "es:", hipotenusa)
print("\n ")

# Obtenga el vector en orden inverso
def invertir_lista(lista):
    return lista[::-1]

mi_lista = [1, 2, 3, 4, 5]
print(f"Lista Original: {mi_lista}")
lista_invertida = invertir_lista(mi_lista)
print(f"Lista invertida: {lista_invertida}")
print("\n ")

# Obtenga la posición o índice de los elementos
# de una lista mayores a un valor umbral
mi_lista = [10, 25, 30, 45, 15, 50]
umbral = 30

print("Lista original ", mi_lista)
print("umbral ", umbral)
indices_mayores_que_umbral = [i for i, x in enumerate(mi_lista) if x > umbral]
print("lista final",indices_mayores_que_umbral)
print("\n ")

# Obtenga los valores diagonales de una matriz
matrix = [
    [3, 5, 1],
    [2, 9, 4],
    [7, 6, 8]
]
print("matriz original ", matrix)
def get_max_value_from(matrix):
    if not matrix or not matrix[0]:
        return None  # Manejo de casos donde la matriz está vacía o tiene filas vacías

    max_value = matrix[0][0]  # Inicializamos el valor máximo con el primer elemento de la matriz
    for row in matrix:
        for value in row:
            if value > max_value:
                max_value = value  # Actualizamos el valor máximo si encontramos uno mayor
    return max_value

print("Valor max",get_max_value_from(matrix))  # Salida: 9
print("\n ")

# Elimine los valores adyacentes a todo valor NaN
# INPUT = [6 10 5 8 9 NaN 23 9 7 3 21 43 NaN 4 6 7 8]
# OUTPUT = [6 10 5 8 9 7 3 21 6 7 8]

arr = np.array([6, 10, 5, 8, 9, np.nan, 23, 9, 7, 3, 21, 43, np.nan, 4, 6, 7, 8])

print("array original",arr)
def remove_adjacent_nan(arr):
    nan_indices = np.isnan(arr)  # Encuentra los índices de los NaN
    to_remove = nan_indices.copy()  # Copia para marcar elementos a eliminar

    # Marca los elementos adyacentes a los NaN
    to_remove[:-1] |= nan_indices[1:]
    to_remove[1:] |= nan_indices[:-1]

    return arr[~to_remove]

output = remove_adjacent_nan(arr)
print("Array final",output)
print("\n ")

# Replique los elementos de un vector
# n=2, A=[1 2 3] -> [1 1 2 2 3 3]
# n=0, A=[2 1] -> []

def replicar_elementos(n, A):
    if n <= 0:
        return []
    return [elemento for elemento in A for _ in range(n)]

n1 = 2
A1 = [1, 2, 3]
resultado1 = replicar_elementos(n1, A1)
print("Ejemplo 1, Vector 1", A1, "Elemento a replicar",n1)
print("resultado1",resultado1)

n2 = 0
A2 = [2, 1]
resultado2 = replicar_elementos(n2, A2)
print("Ejemplo 2, Vector 2", A2, "Elemento a replicar",n2)
print("resultado1",resultado2)
print("\n ")



# Extraiga el primer digito distinto a cero, de cada valor en un vector
# x = [1 0.3 -2 0.001 -0.0006, 582398, 3020]
# y = [1 3 2 1 6 5 3]

def extraer_primer_digito(vector):
    digitos = []
    for numero in vector:
        str_num = str(numero).lstrip('-')  # Elimina el signo negativo si existe
        for char in str_num:
            if char.isdigit() and char != '0':
                digitos.append(int(char))
                break
    return digitos
x = [1, 0.3, -2, 0.001, -0.0006, 582398, 3020]
y =  [1, 3, 2, 1, 6, 5, 3,]

print("Lista original 1", x)
print("Digito distinto de cero 1", extraer_primer_digito(x))
print("Lista original 2", x)
print("Digito distinto de cero 2", extraer_primer_digito(y))
print("\n ")
# Elimine los elementos redundantes en un vector, manteniendo el orden original
# in = [5 3 6 4 7 7 3 5 9]
# out = [5 3 6 4 7 9]

def eliminar_redundantes(vector):
    resultado = []
    vistos = set()
    for elemento in vector:
        if elemento not in vistos:
            resultado.append(elemento)
            vistos.add(elemento)
    return resultado

vector = [5, 3, 6, 4, 7, 7, 3, 5, 9]
resultado = eliminar_redundantes(vector)
print("Vector original",vector)
print("resultado",resultado)