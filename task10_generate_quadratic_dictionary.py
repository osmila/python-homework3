def generate_dictionary_quadratic(range_min, range_max):
    dictionary = dict()
    for i in range(range_min, range_max):
        dictionary[i] = i * i
    print(dictionary)