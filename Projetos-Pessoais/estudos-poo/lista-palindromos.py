def check_palindrome(word=''):
    check = True
    for i in range(0, len(word)):
        if word[i] != word[len(word) - 1 - i]:
            check = False
    return check


def palindromes_list(words=list):
    totalPalindromes = 0
    for i in words:
        if check_palindrome(i):
            totalPalindromes += 1
    return totalPalindromes


print(palindromes_list(['arara', '1010101', 'banana', '666', 'ovo', 'logo']))
