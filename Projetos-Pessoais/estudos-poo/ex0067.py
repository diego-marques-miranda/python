def binary_sum(a='', b=''):
    if len(a) > len(b):
        while len(b) != len(a):
            b = '0' + b
    elif len(b) > len(a):
        while len(a) != len(b):
            a = '0' + a
    summ = ''
    carry = ''
    for i in range(len(a) - 1, -1, -1):
        if (a[i] == '1' and b[i] == '0') or (b[i] == '1' and a[i] == '0'):
            if carry == '1':
                summ = '0' + summ
                carry = '1'
            else:
                summ = '1' + summ
                carry = '0'
        elif a[i] == '1' and b[i] == '1':
            if carry == '1':
                summ = '1' + summ
                carry = '1'
            else:
                summ = '0' + summ
                carry = '1'
        elif a[i] == '0' and b[i] == '0':
            if carry == '1':
                summ = '1' + summ
                carry = '0'
            else:
                summ = '0' + summ
                carry = '0'
        if i == 0:
            summ = carry + summ
    return summ



