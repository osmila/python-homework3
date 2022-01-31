from generate_random_list import generate_list_random


def copy_list():
    initial_list = generate_list_random()
    print(f'Initial list:\t{initial_list}')
    result_list = list()

    for x in initial_list:
        result_list.append(x)

    print(f'Result list:\t{result_list}')