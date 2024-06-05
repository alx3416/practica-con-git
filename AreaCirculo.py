import math
def calcular_area_circulo(radio):

        area = math.pi * (radio ** 2)
        return area

radio = int(input("Ingrese el radio del circulo: "))
area = calcular_area_circulo(radio)
print("El área del círculo con radio", radio, "es:", area)