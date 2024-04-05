def distance(num, k):
    if k - num < 0:
        return -1*(k-num)
    return k-num

def closest(nums, k):
    close = k * 1000
    for i in nums:
        if distance(i, k) <= close:
            close = distance(i, k)
    return k - close


def n_numbers_closest_to_k(numbers, n, k):
    closestNumbers = []
    singles = []
    i = 0
    while len(closestNumbers) != n:
        closestNumbers.append(closest(numbers, k))
        numbers.remove(closest(numbers, k))
        i += 1
    return closestNumbers


print(n_numbers_closest_to_k([0, 1, 2], 2, 2))
