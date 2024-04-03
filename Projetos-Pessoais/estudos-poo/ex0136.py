def single_number(numbers):
    duplicates = []
    singles = []
    temp = []
    for i in numbers:
        if i in temp:
            duplicates.append(i)
        temp.append(i)
    for i in numbers:
        if i not in duplicates:
            singles.append(i)
    return singles


print(single_number([1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))
