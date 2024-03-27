def arguments_lenght(args=[]):
    return len(args)


x = arguments_lenght(input('Type a list of arguments: ').split())
print(x)