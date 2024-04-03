def check_palindrome(input=''):
    check = True
    for i in range(0, len(input)):
        if input[i] != input[len(input) - 1 - i]:
            check = False
    return check


x = 'arara'
if check_palindrome(x):
    print(f'{x} is a palindrome')
else:
    print(f'{x} is not a palindrome')