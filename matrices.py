#multiplicación de matrices algebraicamente de #6

import numpy
import sys

print("Este es un programa de multiplicar matrices 3x3")

r1=int(input("Numero de rengloes de la matriz A:"))
c1=int(input("Numero de columnas de la matriz A:"))

r2=int(input("Numero de rengloes de la matriz B:"))
c2=int(input("Numero de columnas de la matriz B:"))

#Condición para multiplicar matriz

if (c1!= r2):
    print("No se puede hacer la multiplicación de matrices")
    sys.exit()

matriz1=numpy.zeros((r1,c1))
matriz2=numpy.zeros((r2,c2))
matrizr=numpy.zeros((r1,c2)) 
print("Introduce los elementos de la matriz 1")

for r in range(0,r1):
    for c in range(0,c1):
        matriz1[r,c]=input("Elemento A["+str(r+1)+str(c+1)+"]")

print("Introduce los elementos de la matriz 2")

for r in range(0,r2):
    for c in range(0,c2):
        matriz2[r,c]=input("Elemento B["+str(r+1)+str(c+1)+"]")

#Operacion A*B

for r in range (0,r1):
    for c in range(0,c2):
        for k in range(0,r2):
            matrizr[r,c]+=matriz1[r,k]*matriz2[k,c] 
 
print ("La matriz A*B= \n",matrizr)