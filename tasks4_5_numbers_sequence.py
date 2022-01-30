import math
import random


def print_numbers_sequence(a, b):
    print(f'a = {a}')
    print(f'b = {b}')
    if a > b:
        while a >= b:
            print(a, end=' ')
            a -= 1
    else:
        for i in range(a, b+1):
            print(i, end=' ')


def print_sequence_random(max_value):
    a = random.randrange(1, max_value)
    b = random.randrange(1, max_value)
    print_numbers_sequence(a, b)


def print_sequence_a_less_b(max_value):
    a_max = math.ceil(max_value/2)
    a = random.randrange(1, a_max)
    b = random.randrange(a_max, max_value)
    print_numbers_sequence(a, b)