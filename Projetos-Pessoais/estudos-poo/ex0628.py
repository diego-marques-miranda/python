def threeBiggest(numbers):
    bigst = []
    numbers = sorted(numbers, reverse=True)
    bigst.append(numbers[0])
    bigst.append(numbers[1])
    bigst.append(numbers[2])
    return bigst


def maxProduct(nums):
    biggestnums = threeBiggest(nums)
    return biggestnums[0] * biggestnums[1] * biggestnums[2]


list = [1, 2, 3, 4]
print(maxProduct(list))
