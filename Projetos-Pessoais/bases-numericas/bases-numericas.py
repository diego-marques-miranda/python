def dec_bin(dec=int(0)):
    binarium = ''
    rest = 0
    while dec > 0:
        rest = dec % 2
        binarium = str(rest) + binarium
        dec = dec // 2
    return binarium


def dec_octal(dec=0):
    octal = ''
    rest = 0
    while dec > 0:
        rest = dec % 8
        octal = str(rest) + octal
        dec = dec // 8
    return octal


dec = int(input('Type a decimal number: '))
print(dec_bin(dec))
print(dec_octal(dec))