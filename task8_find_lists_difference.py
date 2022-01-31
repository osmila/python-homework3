from generate_random_list import generate_list_random


def find_difference():
    list_1 = generate_list_random()
    list_2 = generate_list_random()
    print(f'List 1:\t{list_1}')
    print(f'List 2:\t{list_2}')
    result_list = list_1.copy()

    for x in list_1:
        for y in list_2:
            if x == y:
                result_list.remove(x)
                break
    print(f'Result list:\t{result_list}')