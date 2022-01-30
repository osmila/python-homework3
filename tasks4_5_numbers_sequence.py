import random

def generate_number(max_value):
    return random.randrange(1, max_value)


def print_numbers_sequence():
    max = 10
    a = generate_number(max)
    b = generate_number(max)
    print(f'a = {a}')
    print(f'b = {b}')
    if a >= b:
        while a != (b - 1):
            print(a, end=' ')
            a -= 1
    if a < b:
        for i in range(a, b+1):
            print(i, end=' ')