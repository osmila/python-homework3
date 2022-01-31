import random


def generate_list_random():
    length = random.randrange(10, 20)
    my_list = list()
    for _ in range(length):
        my_list.append(random.randrange(1, 10))
    return my_list


def delete_duplicates():
    initial_list = generate_list_random()
    changed_list = list()
    changed_list.append(initial_list[0])
    print(f'Initial list: {initial_list}')
    # for i in range(len(initial_list)):
    #     for j in range(len(changed_list)):
    #         if
    #     for
    #     changed_list.append(initial_list[i])
    #     for j in range(i+1, len(initial_list)):
    #         if i == j:
    #             break
    #         elif initial_list[j] == initial_list[i]:
    #             list_to_delete.pop(j)
    # print(f'List after deleting duplicated items: {list_to_delete}')