import random


def generate_list_random():
    length = random.randrange(10, 20)
    my_list = list()
    for _ in range(length):
        my_list.append(random.randrange(1, 10))
    return my_list


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
    list_to_delete = generate_list_random()
    print(f'Initial list:\t{list_to_delete}')
    list_to_delete = list(dict.fromkeys(list_to_delete))
    print(f'Result list:\t{list_to_delete}')
