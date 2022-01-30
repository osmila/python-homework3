import math
import random


def print_asterisks():
    width = random.randrange(1, 20, 2)
    height = width * 2 - 1
    k = 1
    for i in range(height):
        for j in range(k):
            print('* ', end='')
        print('')
        if k < width and i < width:
            k += 1
        else:
            k -= 1


def print_asterisks_bad():
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