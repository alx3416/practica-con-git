import sys

def get_next_fibonacci_number(sequence):
    return sequence[0] + sequence[1]


def get_fibonacci_sequence(target_number):
    sequence = [0, 1]
    next_item = get_next_fibonacci_number(sequence[-1:-3:-1])
    while next_item <= target_number:
        sequence.append(next_item)
        next_item = get_next_fibonacci_number(sequence[-1:-3:-1])
    return sequence


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise RuntimeError("Inserte un numero entero.")
    try:
        target_number = int(sys.argv[1])
    except ValueError:
        print("Error. Solo numeros enteros permitidos.")
        exit()
    fibonacci_sequence = get_fibonacci_sequence(target_number)
    print(fibonacci_sequence)
