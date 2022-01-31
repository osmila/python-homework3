def generate_dictionary_value_x10(range_min, range_max):
    dictionary = dict()
    for i in range(range_min, range_max):
        dictionary[i] = i * 10
    return dictionary


def append_dictionaries():
    dict1 = generate_dictionary_value_x10(1, 3)
    dict2 = generate_dictionary_value_x10(3, 5)
    dict3 = generate_dictionary_value_x10(5, 7)
    print(f'dict1 =\t{dict1}')
    print(f'dict2 =\t{dict2}')
    print(f'dict3 =\t{dict3}')
    result_dict = {**dict1, **dict2, **dict3}
    print(f'result_dict =\t{result_dict}')