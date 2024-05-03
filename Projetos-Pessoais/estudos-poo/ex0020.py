def is_valid(string=''):
    parentheses = closedParen = 0
    brackets = closedBrackets = 0
    keys = closedKeys = 0
    for i in range(len(string)):
        if string[i] == '(':
            parentheses += 1
        elif string[i] == ')':
            closedParen += 1
        elif string[i] == '[':
            brackets += 1
        elif string[i] == ']':
            closedBrackets += 1
        elif string[i] == '{':
            keys += 1
        elif string[i] == '}':
            closedKeys += 1
    if parentheses != closedParen or brackets != closedBrackets or keys != closedKeys:
        return False
    return True
