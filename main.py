# "Conjetura de goldbach"

# función para detectar numeros pares
def is_even(value):
    resultado = False
    if value % 2 == 0:
        resultado = True
    return resultado


def is_prime(value):
    resultado = False
    if value == 2:
        resultado = True
        return resultado
    else:
        for num in range(2, value):
            if value % num == 0:
                resultado = False
                break
            else:
                resultado = True
    return resultado


def get_primes(value):
    resultado = []
    for num in range(2, value):
        if is_prime(num):
            resultado.append(num)
    return resultado


def goldbach_conjeture(value):
    primes_list = get_primes(value)
    goldbach_list = []
    for num in primes_list:
        difference = value - num
        if is_prime(difference):
            for num2 in primes_list:
                if difference + num2 == value:
                    goldbach_list.append([difference, num2])
    return goldbach_list


print(goldbach_conjeture(100))
