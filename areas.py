# Programa para calcular el area de un cuadrado

def get_square_area(lado):
    if lado <= 0:
        square_area = 0
        print("length size must be greater than zero")
    else:
        square_area = lado * lado
    return square_area
