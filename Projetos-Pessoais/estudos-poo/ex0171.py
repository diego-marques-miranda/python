def letter_number(letter=''):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    number = int
    for i in range(len(alphabet)):
        if alphabet[i] == letter:
            number = i + 1
            break
    return number


def column_number(title=''):
    number = 0
    for i in range(len(title) - 1, -1, -1):
        if i != 0:
            number = number + letter_number(title[i])
        if i == 0 and len(title) != 1:
            number = number + (26 * letter_number(title[i]))
    return number



