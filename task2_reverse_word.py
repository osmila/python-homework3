def reverse_word():
    word = input('Enter text to invert: ')

    char_list = list()
    for char in word:
        char_list.append(char)

    char_list.reverse()
    reversed_word = ''.join(char_list)

    print(reversed_word)