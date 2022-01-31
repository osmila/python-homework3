from generate_random_list import generate_list_random


def delete_duplicates_0():
    initial_list = generate_list_random()
    changed_list = initial_list.copy()
    print(f'Initial list:\t{initial_list}')
    length = len(changed_list)

    for i in range(length):
        for j in range(i+1, length):
            if changed_list[j] == changed_list[i]:
                changed_list[j] = 0

    result_list = list()
    for x in changed_list:
        if x != 0:
            result_list.append(x)
    print(f'Result list:\t{result_list}')


def delete_duplicates():
    initial_list = generate_list_random()
    print(f'Initial list:\t{initial_list}')
    result_list = list(dict.fromkeys(initial_list))
    print(f'Result list:\t{result_list}')
