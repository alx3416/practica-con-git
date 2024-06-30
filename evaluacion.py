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