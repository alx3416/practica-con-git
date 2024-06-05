def num_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Agregamos una entrada de valores enteros.
num = int(input("Numero par mayor a 2: "))

if num % 2 == 0 and num > 2:
    encontrado = False
    for a in range(2, num):
        if num_primo(a):
            b = num - a
            if num_primo(b):
                encontrado = True
                if a <= b:
                    print([a, b])
