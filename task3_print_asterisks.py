import math


def print_asterisks():
    height = 9
    k = 0
    for i in range(height):
        j = 0
        while j != (i+1):
            if i <= (height / 2):
                print('* ', end='')
            j += 1
        if i == math.ceil(height / 2):
            k = i
        if i > (height / 2):
            k -= 1
        p = 0
        while p != k:
            if i > (height / 2):
                print('* ', end='')
            p += 1
        print('')