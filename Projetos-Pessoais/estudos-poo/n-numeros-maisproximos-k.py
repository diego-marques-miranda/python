def absolute_value(num=0):
    if num >= 0:
        return num
    return -num


def n_numbers_closest_to_k(numbers, n, k):
    closestNumbers = []
    close = k * 1000
    for i in range(0, len(numbers)):
        if absolute_value(numbers[i] - k) < absolute_value(close - k):
            close = numbers[i]
            closestNumbers.append(numbers[i])
    return closestNumbers


print(n_numbers_closest_to_k([1, 2, 3, 4], 2, 1))
