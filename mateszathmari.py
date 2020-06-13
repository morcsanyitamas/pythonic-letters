def print_letters(word):
    lst = []
    for letters in word:
        lst.append(letters)
    print(lst)


print_letters('Pythonic letters')


def print_letters(word):
    lst = [letters for letters in word]
    print(lst)


print_letters('Pythonic letters')


def print_letters(word):
    lst = list(word)
    print(lst)


print_letters('Pythonic letters')

def print_letters(word):
    print(list(word))


print_letters('Pythonic letters')
